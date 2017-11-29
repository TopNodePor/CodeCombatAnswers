# https://codecombat.com/play/level/return-to-thornbush-farm
# The function maybeBuildTrap defines TWO parameters!
def maybeBuildTrap(x, y):
    # Use x and y as the coordinates to move to.
    hero.moveXY(x, y)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.buildXY('fire-trap', x, y)
        # Use buildXY to build a "fire-trap" at the given x and y


while True:
    # This calls maybeBuildTrap, with the coordinates of the top entrance
    maybeBuildTrap(43, 50)
    # Now use maybeBuildTrap at the left entrance!
    maybeBuildTrap(25, 34)
    # Not use maybeBuildTrap at the bottom entrance!
    maybeBuildTrap(43, 19)
