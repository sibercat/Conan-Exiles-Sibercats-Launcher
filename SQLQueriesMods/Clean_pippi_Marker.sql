-- Delete all Marker from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Blueprints/PippiTools/Marker/BP_Marker%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8966');

DELETE FROM properties
WHERE properties.name LIKE '%BP_Marker%';