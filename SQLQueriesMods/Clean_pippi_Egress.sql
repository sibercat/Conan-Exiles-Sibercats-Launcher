-- Delete all Egress from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Pippi_Egress%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8993');

DELETE FROM properties
WHERE properties.name LIKE '%Pippi_Egress%';