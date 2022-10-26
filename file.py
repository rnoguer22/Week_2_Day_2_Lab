from vikingsClasses import (
    Soldier,
    Saxon,
    Viking,
    War
)

Pelayo = Saxon(100, 99)
Maria = Viking("Polliqui", 100, 200)

guerra = War()
guerra.addSaxon(Pelayo)
guerra.addViking(Maria)
print(guerra.saxonAttack())
print(guerra.vikingAttack())
print(guerra.showStatus())