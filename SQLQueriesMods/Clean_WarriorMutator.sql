-- Clean up all Warrior Mutator placables/Building/Items - 4/9/2024

DELETE FROM actor_position 
WHERE actor_position.class LIKE '%/Game/Mods/Warrior_mutator_mod%';

DELETE FROM building_instances 
WHERE building_instances.class LIKE '%/Game/Mods/Warrior_mutator_mod%';

--DELETE FROM properties
--WHERE properties.name LIKE '%BP_CA_Sw%';

--DELETE FROM static_buildables 
--WHERE static_buildables.name LIKE '%/Game/Mods/Warrior_mutator_mod%';

--DELETE FROM item_inventory WHERE item_inventory.template_id IN ();
