type = "passive"
def handler(fit, ship, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Heavy Drone Operation"),
                                 "shieldCapacity", ship.getModifiedItemAttr("shipBonusPirateFaction"))
