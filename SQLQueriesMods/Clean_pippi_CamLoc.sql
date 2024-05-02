-- Delete all CamLoc from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Pippi_CamLoc%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8992');

DELETE FROM properties
WHERE properties.name LIKE '%Pippi_CamLoc%';