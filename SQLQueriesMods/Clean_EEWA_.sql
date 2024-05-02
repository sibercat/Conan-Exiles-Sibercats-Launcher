-- Clean up all EEWA placables/Building/Items - 4/6/2024
-- The server will try and clean itself needs two restarts. after two restarts run Remove All [EEWA] to clean everything up.
-- EEWA: 320KB
-- EEWA Removed = 1. Restart: 312KB | 2. Restart: 308KB
-- Remove All [EEWA]: 260KB - same as vanilla values
--Based on vanilla + EEWA

DELETE FROM actor_position 
WHERE actor_position.class LIKE '%/Game/Mods/Tutorial%';

--DELETE FROM building_instances    EEWA has no instanced buildings
--WHERE building_instances.class LIKE '%___%';

DELETE FROM properties 
WHERE properties.name LIKE '%_EEWA_%';

DELETE FROM static_buildables 
WHERE static_buildables.name LIKE '%EEWA%';

--Did not get IDs Yet   DELETE FROM item_inventory WHERE item_inventory.template_id IN ();