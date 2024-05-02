-- Delete all NPCSpawners from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Pippi_NPCSpawner%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8999');

DELETE FROM properties
WHERE properties.name LIKE '%Pippi_NPCSpawner%';