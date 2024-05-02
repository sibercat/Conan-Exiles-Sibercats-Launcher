-- Delete all Pippi Note from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Pippi_Note%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8989');

DELETE FROM properties
WHERE properties.name LIKE '%Pippi_Note%';