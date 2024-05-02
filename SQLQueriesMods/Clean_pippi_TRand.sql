-- Delete all TRand from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Blueprints/PippiTools/TRand/BP_TRand%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8971');

DELETE FROM properties
WHERE properties.name LIKE '%BP_TRand%';