-- Delete all Portals from DB - 4/10/2024

DELETE FROM actor_position
WHERE actor_position.class LIKE '%/Game/Mods/Pippi/Pippi_Warper%';

DELETE FROM item_inventory
WHERE item_inventory.template_id IN ('-8996');

DELETE FROM properties
WHERE properties.name LIKE '%Pippi_Warper%' OR properties.name LIKE '%Pippi_SystemConfigs_C.WarpSettings%';