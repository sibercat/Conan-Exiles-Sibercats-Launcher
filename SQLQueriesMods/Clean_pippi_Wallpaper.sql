-- Delete all Wallpapers from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Pippi_Wallpaper%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8990');

DELETE FROM properties
WHERE properties.name LIKE '%Pippi_Wallpaper%';