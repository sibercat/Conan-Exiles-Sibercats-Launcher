import os
import sys
import subprocess
import requests
import sqlite3
import chardet
import socket
import csv
import threading
import psutil
import re
import time
from layout import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar, QFileDialog
from PyQt6.QtCore import QMetaObject, QThread, pyqtSignal

# Define constants for file paths
TEXT_FILE_PATH = r"DedicatedServerLauncher\ConanExilesDedicatedServer\ConanSandbox\Mods\modlist.txt"
LOG_FOLDER_PATH = r"DedicatedServerLauncher\ConanExilesDedicatedServer\ConanSandbox\Saved\Logs"

# Define get_external_ip function to retrieve the external IP
def get_external_ip(timeout=10):
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=timeout)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        data = response.json()
        return data['ip']
    except requests.exceptions.RequestException as e:
        return f"Error retrieving external IP: {str(e)}"
        
        
class DatabaseRecoveryThread(QThread):
    recovery_finished = pyqtSignal(str)

    def __init__(self, db_file_path):
        super().__init__()
        self.db_file_path = db_file_path

    def run(self):
        try:
            print("Starting database recovery process...")

            # Run the SQLite recovery command
            process = subprocess.run(["sqlite3.exe", self.db_file_path, ".recover"], capture_output=True, text=True, encoding='utf-8', errors='replace')

            if process.returncode != 0:
                raise subprocess.CalledProcessError(process.returncode, "sqlite3.exe", output=process.stderr)

            result = process.stdout
            print("Recovery command output:")
            print(result)

            self.recovery_finished.emit("Database recovery completed successfully.")
        except FileNotFoundError:
            print("Error: sqlite3.exe not found.")
            self.recovery_finished.emit("Error: sqlite3.exe not found. Please ensure it is installed and in your system PATH.")
        except subprocess.CalledProcessError as e:
            print(f"Error: An error occurred during the recovery process.")
            print(e.stderr)
            self.recovery_finished.emit(f"Error: An error occurred during the recovery process: {e.stderr}")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect button signals to their respective slots
        self.pushButton1.clicked.connect(self.openDedicatedServer)
        self.pushButton2.clicked.connect(self.checkDatabaseIntegrity)
        self.pushButton3.clicked.connect(self.openTextFile)
        self.pushButton4.clicked.connect(self.deleteLogFiles)
        self.pushButton7.clicked.connect(self.cleanEE)
        self.pushButton8.clicked.connect(self.cleanAOC)
        self.pushButton9.clicked.connect(self.clean_eewa)
        self.pushButton10.clicked.connect(self.optimize_database)
        self.pushButton11.clicked.connect(self.clean_emberlight)
        self.pushButton12.clicked.connect(self.confirm_database_recovery)
        self.pushButton13.clicked.connect(self.id_stripper_txt)
        self.pushButton14.clicked.connect(self.id_stripper_encoded)
        self.pushButton16.clicked.connect(self.id_stripper_csv)
        self.pushButton15.clicked.connect(self.clean_savage_wilds)
        self.pushButton17.clicked.connect(self.clean_shimas_compendium)
        self.pushButton18.clicked.connect(self.check_port)
        self.pushButton19.clicked.connect(self.clean_warrior_mutator)
        self.pushButton20.clicked.connect(self.submit_pippi)
        
        # Set object names for checkbox widgets
        self.checkBoxWallpaper_R.setObjectName("checkBoxWallpaper_R")
        self.checkBoxGlorb_R.setObjectName("checkBoxGlorb_R")
        self.checkBoxNPCSpawn_R.setObjectName("checkBoxNPCSpawn_R")
        self.checkBoxLootSpawner_R.setObjectName("checkBoxLootSpawner_R")
        self.checkBoxPortal_R.setObjectName("checkBoxPortal_R")
        self.checkBoxFlaggi_R.setObjectName("checkBoxFlaggi_R")
        self.checkBoxThespian_R.setObjectName("checkBoxThespian_R")
        self.checkBoxEgress_R.setObjectName("checkBoxEgress_R")
        self.checkBoxCamLoc_R.setObjectName("checkBoxCamLoc_R")
        self.checkBoxPippijack_R.setObjectName("checkBoxPippijack_R")
        self.checkBoxTZone_R.setObjectName("checkBoxTZone_R")
        self.checkBoxTTime_R.setObjectName("checkBoxTTime_R")
        self.checkBoxTControl_R.setObjectName("checkBoxTControl_R")
        self.checkBoxTPlatform_R.setObjectName("checkBoxTPlatform_R")
        self.checkBoxTSeq_R.setObjectName("checkBoxTSeq_R")
        self.checkBoxTRand_R.setObjectName("checkBoxTRand_R")
        self.checkBoxTPlate_R.setObjectName("checkBoxTPlate_R")
        self.checkBoxTCombiner_R.setObjectName("checkBoxTCombiner_R")
        self.checkBoxMarker_R.setObjectName("checkBoxMarker_R")
        self.checkBoxRePlaceable_R.setObjectName("checkBoxRePlaceable_R")
        self.checkBoxPippiNote_R.setObjectName("checkBoxPippiNote_R")
        self.checkBoxNPCSummoner_R.setObjectName("checkBoxNPCSummoner_R")
        self.checkBoxEasel_R.setObjectName("checkBoxEasel_R")
        self.checkBoxMusiqBox_R.setObjectName("checkBoxMusiqBox_R")
        self.checkBoxLazor_R.setObjectName("checkBoxLazor_R")
        self.checkBoxCryptex_R.setObjectName("checkBoxCryptex_R")
        self.checkBoxCheckpoint_R.setObjectName("checkBoxCheckpoint_R")
        
        # Set object name for line edit widget
        self.lineEditIPv4addressLocal.setObjectName("lineEditIPv4addressLocal")
        self.lineEditExternaliP.setObjectName("lineEditExternaliP")
        self.linePortProtocalbeingUsed.setObjectName("linePortProtocalbeingUsed")
        
        # Hide the progress bar initially
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()  # Hide the progress bar initially

        # Set the IPv4 address of the local host to lineEditIPv4addressLocal when the app starts
        self.set_local_ipv4_address()

        #update external IP field
        self.update_external_ip()
        

    #Find if the given ports and protocol are being used, optionally filtered by a specific IP address.
    def find_ports(self, ports, protocol, ip_address=None):
        try:
           netstat_output = subprocess.check_output(['netstat', '-an'], text=True)
           port_info = []
           protocol = protocol.upper()
           search_patterns = [f"{ip_address}:{port}" if ip_address else f":{port} " for port in ports]
        
           for line in netstat_output.splitlines():
               if protocol in line:
                   for pattern in search_patterns:
                       if pattern in line:
                           port_info.append(line)
                           break
        
           return port_info or None
        except subprocess.CalledProcessError as e:
           QMessageBox.critical(self, "Error", f"Failed to run netstat: {e}")
           return None

    def check_port(self):
        protocol = 'UDP'  # This can be adjusted or taken from a user input
        ip_address = socket.gethostbyname(socket.gethostname())  # Automatically gets the host IP
        ports_string = self.linePortProtocalbeingUsed.text().strip()  # Get and trim user input for ports
    
        if not ports_string:
            QMessageBox.warning(self, "Input Error", "Please enter at least one port number.")
            return
    
        ports_to_search = [port.strip() for port in ports_string.split(',')]  # Split the input by comma to handle multiple ports
    
        if not all(port.isdigit() for port in ports_to_search):
            QMessageBox.warning(self, "Input Error", "Please enter only numeric port values.")
            return
    
        ports_to_search = [int(port) for port in ports_to_search]  # Convert ports to integers
    
        used_ports, unused_ports = [], []
    
        for port in ports_to_search:
            if self.is_port_used(port, protocol, ip_address):
                used_ports.append(str(port))
            else:
                unused_ports.append(str(port))
    
        if used_ports:
            QMessageBox.information(self, "UDP Ports Used", f"The following ports are being used: {', '.join(used_ports)}")
        if unused_ports:
            QMessageBox.information(self, "UDP Ports Not Used", f"The following ports are not being used: {', '.join(unused_ports)}")

    def is_port_used(self, port, protocol, ip_address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt
    
        try:
           sock.bind((ip_address, port))
           sock.close()
           return False
        except socket.error:
            return True


    # Get Local ipv4 address Start of block
    def set_local_ipv4_address(self):
        try:
            # Get the IPv4 address of the local host
            host = socket.gethostbyname(socket.gethostname())
            
            # Assign the IPv4 address to lineEditIPv4addressLocal
            self.lineEditIPv4addressLocal.setText(host)
        except socket.error as e:
            # If an error occurs, display it in the console
            print("Error:", e)
    
    def update_external_ip(self):
        # Update the externa IP field
        external_ip = get_external_ip()
        self.lineEditExternaliP.setText(external_ip)

    def recover_database(self, db_file_path):
        self.recovery_thread = DatabaseRecoveryThread(db_file_path)
        self.recovery_thread.recovery_finished.connect(self.show_recovery_result)
        self.recovery_thread.start()

        self.progressBar.setRange(0, 0)  # Set the progress bar to indeterminate mode
        self.progressBar.show()

    def show_recovery_result(self, result):
        self.progressBar.hide()
        QMessageBox.information(self, "Recovery Process Finished", result)

    def openDedicatedServer(self):
        try:
            subprocess.Popen("DedicatedServerLauncher.exe")
            print("Opened DedicatedServerLauncher.exe")
        except FileNotFoundError:
            print("Error: Could not find DedicatedServerLauncher.exe")
            QMessageBox.critical(self, "Error", "Could not find DedicatedServerLauncher.exe. Make sure it's in the same directory as this program, and make sure you have removed versioning number at the end of Launcher should be 'DedicatedServerLauncher.exe'")
        
    # Start Data Base Code Block
    def checkDatabaseIntegrity(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()
            
                # Execute pragma integrity_check command
                cursor.execute("pragma integrity_check;")
            
                result = cursor.fetchone()[0]  # Fetch the result
            
                conn.commit()
                conn.close()
            
                if result == 'ok':
                    QMessageBox.information(self, "Database Integrity Check", "The database integrity is OK.")
                else:
                    QMessageBox.critical(self, "Database Integrity Check", f"The database integrity is compromised. Error: {result}")
            except sqlite3.Error as e:
                QMessageBox.warning(self, "Error", f"Error connecting to the database: {e}")
                
    def optimize_database(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Execute PRAGMA optimize and VACUUM commands
                cursor.execute("PRAGMA optimize;")
                cursor.execute("VACUUM;")

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Database Optimized", "The database has been optimized successfully.")
            except sqlite3.DatabaseError as e:
                QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
               
    def confirm_database_recovery(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select Database File", "", "Database files (*.db)")
        if db_file_path:
            # Ask the user for confirmation before proceeding
            confirmation = QMessageBox.question(self, "Confirm Database Recovery", "This action is very taxing especially on big DB. Are you sure you want to attempt database recovery?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            # Check if the user confirmed the action
            if confirmation == QMessageBox.StandardButton.Yes:
                # Run the recovery process in a separate thread
                threading.Thread(target=self.recover_database, args=(db_file_path,)).start()
        else:
            QMessageBox.information(self, "Action Cancelled", "No database file selected.")
            
    # End Data Base Code Block


    def openTextFile(self):
        if os.path.exists(TEXT_FILE_PATH):
            subprocess.Popen(["notepad.exe", TEXT_FILE_PATH])
        else:
            QMessageBox.critical(self, "Error", "modlist.txt file does not exist.")

    def deleteLogFiles(self):
        if os.path.exists(LOG_FOLDER_PATH):
            for proc in psutil.process_iter():
                if "ConanSandboxServer.exe" in proc.name():
                    QMessageBox.critical(self, "Error", "ConanSandboxServer.exe is running. Cannot delete log files.")
                    return

            for file in os.listdir(LOG_FOLDER_PATH):
                if file.endswith(".log"):
                    os.remove(os.path.join(LOG_FOLDER_PATH, file))
            QMessageBox.information(self, "Log Files Deleted", "Log files deleted successfully.")
        else:
            QMessageBox.critical(self, "Error", "The specified log folder does not exist.")
                
    def cleanEE(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_EE_.sql file
                with open(r"SQLQueriesMods\Clean_EE_.sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")
                
    def cleanAOC(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_AOC_.sql file
                with open(r"SQLQueriesMods\Clean_AOC_.sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")
                
    def clean_eewa(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_EEWA_.sql file
                with open(r"SQLQueriesMods\Clean_EEWA_.sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")
               
    def clean_emberlight(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_Emberlight_.sql file
                with open(r"SQLQueriesMods\Clean_Emberlight_.sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")
                
    def clean_savage_wilds(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select savagewilds_game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_SavageWilds.sql file
                with open(r"SQLQueriesMods\Clean_SavageWilds.sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")
                
    def clean_shimas_compendium(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_ShimasCompendium .sql file
                with open(r"SQLQueriesMods\Clean_ShimasCompendium .sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")
                
    def clean_warrior_mutator(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if db_file_path:
            try:
                conn = sqlite3.connect(db_file_path)
                cursor = conn.cursor()

                # Read SQL queries from Clean_WarriorMutator.sql file
                with open(r"SQLQueriesMods\Clean_WarriorMutator.sql", "r") as sql_file:
                    sql_queries = sql_file.read()

                # Split SQL queries by semicolon
                queries = sql_queries.split(";")

                # Execute each query
                for query in queries:
                    if query.strip():
                        cursor.execute(query.strip())

                conn.commit()
                conn.close()
                QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vaccum afterwards.")
            except sqlite3.Error as e:
                QMessageBox.showerror("Error", f"An error occurred: {e}")

    # Pippi Clean Up
    def submit_pippi(self):
        db_file_path, _ = QFileDialog.getOpenFileName(self, "Select game.db File", "", "Database files (*.db)")
        if not db_file_path:
            QMessageBox.warning(self, "No Database Selected", "Please select a database file before submitting.")
            return

        try:
            conn = sqlite3.connect(db_file_path)
            cursor = conn.cursor()
            
            checkbox_to_sql_file = {
                self.checkBoxWallpaper_R: r"SQLQueriesMods\Clean_pippi_Wallpaper.sql",
                self.checkBoxGlorb_R: r"SQLQueriesMods\Clean_pippi_Glorb.sql",
                self.checkBoxNPCSpawn_R: r"SQLQueriesMods\Clean_pippi_NPCSpawner.sql",
                self.checkBoxLootSpawner_R: r"SQLQueriesMods\Clean_pippi_LootSpawner.sql",
                self.checkBoxPortal_R: r"SQLQueriesMods\Clean_pippi_Portal.sql",
                self.checkBoxFlaggi_R: r"SQLQueriesMods\Clean_pippi_Flaggi.sql",
                self.checkBoxThespian_R: r"SQLQueriesMods\Clean_pippi_Thespian.sql",
                self.checkBoxEgress_R: r"SQLQueriesMods\Clean_pippi_Egress.sql",
                self.checkBoxCamLoc_R: r"SQLQueriesMods\Clean_pippi_CamLoc.sql",
                self.checkBoxPippijack_R: r"SQLQueriesMods\Clean_pippi_Pippijack.sql",
                self.checkBoxTZone_R: r"SQLQueriesMods\Clean_pippi_TZone.sql",
                self.checkBoxTTime_R: r"SQLQueriesMods\Clean_pippi_TTime.sql",
                self.checkBoxTControl_R: r"SQLQueriesMods\Clean_pippi_TControl.sql",
                self.checkBoxTPlatform_R: r"SQLQueriesMods\Clean_pippi_TPlatform.sql",
                self.checkBoxTSeq_R: r"SQLQueriesMods\Clean_pippi_TSeq.sql",
                self.checkBoxTRand_R: r"SQLQueriesMods\Clean_pippi_TRand.sql",
                self.checkBoxTPlate_R: r"SQLQueriesMods\Clean_pippi_TPlate.sql",
                self.checkBoxTCombiner_R: r"SQLQueriesMods\Clean_pippi_TCombiner.sql",
                self.checkBoxMarker_R: r"SQLQueriesMods\Clean_pippi_Marker.sql",
                self.checkBoxRePlaceable_R: r"SQLQueriesMods\Clean_pippi_RePlaceable.sql",
                self.checkBoxPippiNote_R: r"SQLQueriesMods\Clean_pippi_PippiNote.sql",
                self.checkBoxNPCSummoner_R: r"SQLQueriesMods\Clean_pippi_NPCSummoner.sql",
                self.checkBoxEasel_R: r"SQLQueriesMods\Clean_pippi_Easel.sql",
                self.checkBoxMusiqBox_R: r"SQLQueriesMods\Clean_pippi_MusiqBox.sql",
                self.checkBoxLazor_R: r"SQLQueriesMods\Clean_pippi_Lazor.sql",
                self.checkBoxCryptex_R: r"SQLQueriesMods\Clean_pippi_Cryptex.sql",
                self.checkBoxCheckpoint_R: r"SQLQueriesMods\Clean_pippi_Checkpoint.sql"
            }

            selected_checkboxes = [checkbox for checkbox, _ in checkbox_to_sql_file.items() if checkbox.isChecked()]
            if not selected_checkboxes:
                QMessageBox.warning(self, "No Checkbox Selected", "Please select a checkbox before submitting.")
                return

            for checkbox in selected_checkboxes:
                sql_file_path = checkbox_to_sql_file[checkbox]
                with open(sql_file_path, "r") as sql_file:
                    sql_queries = sql_file.read()

                for query in sql_queries.split(";"):
                    if query.strip():
                        cursor.execute(query.strip())
                conn.commit()

            conn.close()
            QMessageBox.information(self, "Records Deleted", "Records have been deleted successfully. It's best to run Optimize/Vacuum afterwards.")

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred while accessing the database: {e}")
        except IOError as e:
            QMessageBox.critical(self, "File Error", f"An error occurred while reading the SQL file: {e}")            
    # Pippi Clean Up
            
    def id_stripper_txt(self):
        try:
            # Prompt user to select input file
            input_file = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text files (*.txt)")[0]
            if not input_file:
                # User canceled file selection
                return

            output_file = 'outputIDs.txt'

            # Read the content of the file
            with open(input_file, "r") as file:
                content = file.read()

            # Find all numbers in the content
            numbers = re.findall(r"\d+", content)

            # Convert each number to the desired format
            formatted_numbers = [f"'{number}'" for number in numbers]

            # Join the formatted numbers with commas
            result = ",".join(formatted_numbers)

            # Write the result to the output file
            with open(output_file, "w") as file:
                file.write(result)

            print("Extraction and formatting complete.")  # This will print in the console
            QMessageBox.information(self, "Extraction Complete", "Numbers have been extracted and saved to outputIDs.txt")
        except Exception as e:
            print(f"Error occurred: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            
    def id_stripper_encoded(self):
        try:
            # Prompt user to select .json file
            input_file = QFileDialog.getOpenFileName(self, "Select JSON File", "", "JSON files (*.json)")[0]
            if not input_file:
                # User canceled file selection
                return

            output_file = 'output.txt'
            keyword = 'RowName'

            # Call the function to extract numbers from the file
            self.extract_numbers_from_file(input_file, output_file, keyword)

            print("Done!")  # This will print "Done!" in the console
            QMessageBox.information(self, "Extraction Complete", "Numbers have been extracted and saved to output.txt")
        except Exception as e:
            print(f"Error occurred: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def extract_numbers_from_file(self, input_file, output_file, keyword):
        # Read file into memory
        output = "("
        with open(input_file, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        with open(input_file, 'r', encoding=encoding) as f_in:
            while True:
                line = f_in.readline()
                if line:
                    if not line.find(keyword) == -1:
                        splitLine = line.strip().split(": ")
                        parsedRowName = splitLine[1][1:-2]
                        output += ("'" + parsedRowName + "',")
                else:
                    break
            output = output[:-2] + ")"
        # Write output to file
        with open(output_file, 'w') as f_out:
            f_out.write(output)
           
    def id_stripper_csv(self):
        # Prompt user to select CSV file
        input_file = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV files (*.csv)")[0]
        if not input_file:
            # User canceled file selection
            return

        output_file = 'output.txt'  # Change output file name to 'output.txt'

        # Read the content of the CSV file
        try:
            with open(input_file, 'rb') as file:
                # Detect the encoding of the file
                result = chardet.detect(file.read())
                encoding = result['encoding']

            with open(input_file, 'r', newline='', encoding=encoding) as file:
                reader = csv.reader(file)
                data = [row for row in reader]

        except FileNotFoundError:
            print(f"Error: {input_file} not found.")
            QMessageBox.critical(self, "File Error", f"Error: {input_file} not found.")
            return
        except csv.Error as e:
            print(f"Error reading {input_file}: {e}")
            QMessageBox.critical(self, "File Error", f"Error reading {input_file}: {e}")
            return

        # Extract the numbers from the first column
        numbers = []
        for row in data:
            if row:
                match = re.search(r'^\d+', row[0])
                if match:
                    numbers.append(f"'{match.group()}'")

        if not numbers:
            print(f"Warning: No numeric data found at the start of the first column in {input_file}.")
            QMessageBox.warning(self, "Warning", f"No numeric data found at the start of the first column in {input_file}.")

        # Write the numbers to the output text file
        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as file:
                file.write(','.join(numbers))
        except IOError as e:
            print(f"Error writing to {output_file}: {e}")
            QMessageBox.critical(self, "File Error", f"Error writing to {output_file}: {e}")
            return

        QMessageBox.information(self, "Extraction Complete", f"Numbers extracted from the first column of {input_file} and saved to {output_file}.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
