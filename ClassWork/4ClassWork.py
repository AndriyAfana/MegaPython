from Character import Character

player1 = Character("Luffy", 1500, 200, 50)
player1.print_stats()

player2 = Character("Katakuri", 2400, 300, 0)
player2.print_stats()

while True:
    if player1.health == 0:
        exit()
    if player2.health == 0:
        exit()
    player1.attack(player2)
    player2.attack(player1)
    print("\n\n")
    player1.print_stats()
    player2.print_stats()