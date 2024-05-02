-- Delete all TPlate from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Blueprints/PippiTools/TPlate/BP_TPlate%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8979');

DELETE FROM properties
WHERE properties.name LIKE '%BP_TPlate%';