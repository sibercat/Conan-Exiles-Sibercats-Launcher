-- Delete all Cryptex Note from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Blueprints/PippiTools/Cryptex/BP_Cryptex%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8965');

DELETE FROM properties
WHERE properties.name LIKE '%BP_Cryptex%';