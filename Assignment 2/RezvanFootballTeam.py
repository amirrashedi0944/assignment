rezvanWins = 0
rezvanTied = 0
rezvanLosses = 0
rezvanPoints = 0
numberOfGames = 1
while numberOfGames != 9:
    if numberOfGames % 2 == 0:
        homeAway = "Away game"
    else:
        homeAway = "Home game"
    print(f'Game {numberOfGames} \t{homeAway}')
    game = input("""*****************
    Win     ---> +3 points
    Tied    ---> +1 points
    Lose    ---> +0 points
    Enter the team point in this match: """)
    if game == "3" or game == "Win" or game == "win":
        rezvanWins += 1
        rezvanPoints += 3
    elif game == "1" or game == "Tied" or game == "tied":
        rezvanTied += 1
        rezvanPoints += 1
    elif game == "0" or game == "Lose" or game == "lose" :
        rezvanLosses += 1
    else:
        print("Invalid input.")
        numberOfGames -= 1
    numberOfGames += 1


print(f'Number of rezvan team wins = {rezvanWins}')
print(f'Number of rezvan team losses = {rezvanLosses}')
print(f'Number of rezvan team tied games = {rezvanTied}')
print(f'Points of rezvan team = {rezvanPoints}')
