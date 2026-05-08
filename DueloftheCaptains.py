import random
from Player_class import Player
from Enemy_class import Enemy

print("[DUEL OF THE CAPTAINS]\n\nWelcome to the seven seas! All the glory and gold in the world just a voyage away!")
print("But you aren't alone in these waters...\nAnother frigate holding similar ambitions closes in on your location.")
print("The ocean isn't big enough for the two of you to coexist, and the other crew knows it.")
action=None
player = Player(action)
enemy = Enemy(0)

while True:
    print("\nYour health:",str(player.health) + ". Cannons loaded?:", str(player.loaded) + ". Bowsprit intact?:",  str(player.bowsprit))
    print("Enemy health:", str(enemy.health) + ". Enemy cannons loaded?:", str(enemy.loaded) + ". Enemy bowsprit intact?:", (enemy.bowsprit))
    print("You have 5 options:\n(1) Fire your cannons\n(2) Reload your cannons\n(3) Evade an attack\n(4) Charge your ship into the enemy\n(5) Escape/Quit")
    player.action = input()
    enemy.decision = random.randint(1,4)
    player.turn()
    if player.action == "5":
        print("\nOthers may consider you a coward, but cowards survive.")
        print("You escaped with", player.health, "health left.")
        print("\n[GAME OVER]")
        break
    if player.action == "1":
        if enemy.decision != 3 and player.loaded == True:
            print("Your attack landed! Enemy has taken 20 damage!")
            enemy.health -= 20
            player.loaded = False
        elif player.action == "1" and player.loaded == False:
            print("You need to reload your cannons first!")
            pass
    if player.action == "4":
        if enemy.decision != 3 and player.bowsprit == True:
            print("You crashed into the enemy ship!!! Enemy has taken 60 damage, but you've lost your evade option and taken 20 damage!")
            enemy.health -= 60
            player.health -= 20
            player.bowsprit = False
        else:
            pass

    enemy.enemy_turn()
    if enemy.decision == 1 and enemy.loaded == False:
        print("The enemy blundered!")
        pass
    if enemy.decision == 1 and enemy.loaded == True:
        if player.action != "3":
            print("The enemy's attack landed! You've taken 20 damage!")
            player.health -= 20
            enemy.loaded = False
        elif player.action == 3:
            enemy.loaded = False
    if enemy.decision == 4 and enemy.bowsprit == False:
        print("The enemy blundered!")
    if enemy.decision == 4 and enemy.bowsprit == True:
        if player.action != "3":
            print("The enemy crashed into your ship!!! You've taken 60 damage, but the enemy has lost their ability to evade and took 20 damage!")
            player.health -= 60
            enemy.health -= 20
            enemy.bowsprit = False

    if player.health <= 0 and enemy.health > 0:
        print("\nYou've lost all your health! Abandon ship!!!")
        print("The enemy survived with", enemy.health, "health left.")
        print("\n[GAME OVER]")
        break
    if player.health <= 0 and enemy.health <= 0:
        print("\nBoth ships lost all their health! Dead men tell no tales I suppose...")
        print("\n[STALEMATE]")
        break
    elif player.health > 0 and enemy.health <= 0:
        print("\nThe enemy lost all their health! Cheers to the captain!!!")
        print("You survived with", player.health, "health left.")
        print("\n[YOU WIN]")
        break
    
          
    
