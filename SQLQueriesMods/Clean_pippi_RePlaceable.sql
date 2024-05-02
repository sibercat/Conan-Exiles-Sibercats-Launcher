-- Delete all RePlaceable from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Blueprints/PippiTools/Replaceable/BP_RePlaceable%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8968');

DELETE FROM properties
WHERE properties.name LIKE '%BP_RePlaceable%';