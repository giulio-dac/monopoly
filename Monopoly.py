import random as rand

# This will be a kickass monopoly game

print('This is a new version of the classic monopoly game. Before you start, we will go over a few changes in this board game. \nThis board game will use the principle of monopoly, but with an extra touch. If you want to buy something,you first need to answer a question. If you get it wrong, then you cannot buy it anymore.')

# All variables and dictionaries.
places = {0: 'START', 1: 'JVB', 2: 'DUWO', 3: 'Nassaulaan', 4: 'Free Parking', 5: 'AE Faculty', 6: '3mE Faculty',
          7: 'TNW Faculty', 8: 'Free Parking',
          9: 'Voorstraat', 10: 'Central Station', 11: 'Oude kerk', 12: 'Go to jail!', 13: 'Prinsenhof',
          14: 'Nieuwe Kerk', 15: 'Oude Delft'}

prices = {1: '50', 2: '100', 3: '150', 5: '200', 6: '250', 7: '300', 9: '350', 10: '400', 11: '450', 13: '500', 14: '550', 15: '1000'}

questions = {1: 'How many people typically live in a JVB house?', 2: 'If you pay 300 euros a month plus 20 per cent of utilities, how much do you pay in one year?', 3: 'What is the name of the supermarket on Nassaulaan?',
             5: 'What is the sum of static and dynamic pressure?', 6: 'What do the 3 Ms stand for (in alphabetic order)?', 7: 'How do you call particles that can be in the same quantum state?',
             9: 'When did Italy become a Republic?', 10: 'When was Willem van Oranje murdered by Balthasar Gerards?', 11: 'What is the name of Enrique Iglesias\' father?',
             13: 'When was Delft granted city rights?', 14: 'When will the construction of the area around the station be done?', 15: 'What are our names (in alphabetical order)?'}

correct_answers = {1: '16', 2: '4320', 3: 'Coop', 5: 'Total pressure', 6: 'Maritime materials mechanical', 7: 'Bosons', 9: '1946', 10: '1584', 11: 'Julio', 13: '1246', 14: '2035', 15: 'Giulio Jose Roos Thijs-Gerrit Tim'}

all_possible_places = ['START', 'JVB', 'DUWO', 'Nassaulaan', 'Free Parking', 'AE Faculty', '3mE Faculty', 'TNW Faculty', 'Free Parking',
                       'Voorstraat', 'Central Station', 'Oude kerk', 'Go to jail!', 'Prinsenhof', 'Nieuwe Kerk', 'Oude Delft']

# defining preliminary boolean variables needed in the game loops
player_naming = True
playing = True
buying = False

# the following list contains lists of properties of the players. Mrs. Hermans, we are aware you would have preferred a dictionay, but we could not figure out how to perform the same operation using dictionaries
property_list = [[], [], [], []]

# open and read the text file containing the board visuals. Also check for errors while opening and reading it
try:
    with open("board.txt") as file:
        board = file.read()
except FileNotFoundError as ex:
    print(ex.args[0])               # print the error message, but continue the program

# Loop used to select the number of players and assign names
while player_naming:
    amount_players = input('\n\nWith how many people do you want to play this game [2 to 4]?  ')

    if amount_players == '2':
        monopoly_player1 = input('Please insert name of player 1:   ')
        monopoly_player2 = input('Please insert name of player 2:   ')
        players = [monopoly_player1, monopoly_player2]
        counter = ['1', '2']
        print_this = ["player {0} --> {1}".format(number, player) for number in counter for player in players]
        input('\n\nThese are the names of the player: \n' + print_this[0] + '\n' + print_this[int(amount_players)+1] + "\nPress enter to pass...")
        player_naming = False

    elif amount_players == '3':
        monopoly_player1 = input('Please insert name of player 1:   ')
        monopoly_player2 = input('Please insert name of player 2:   ')
        monopoly_player3 = input('Please insert name of player 3:   ')
        players = [monopoly_player1, monopoly_player2, monopoly_player3]
        counter = ['1', '2', '3']
        print_this = ["player {0} --> {1}".format(number, player) for number in counter for player in players]
        input('\n\nThese are the names of the player: \n' + print_this[0] + '\n' + print_this[int(amount_players)+1] + '\n' + print_this[int(amount_players) * 2+2] + "\nPress enter to pass...")
        player_naming = False

    elif amount_players == '4':
        monopoly_player1 = input('Please insert name of player 1:   ')
        monopoly_player2 = input('Please insert name of player 2:   ')
        monopoly_player3 = input('Please insert name of player 3:   ')
        monopoly_player4 = input('Please insert name of player 4:   ')
        players = [monopoly_player1, monopoly_player2, monopoly_player3, monopoly_player4]
        counter = ['1', '2', '3', '4']
        print_this = ["player {0} --> {1}".format(number, player) for number in counter for player in players]
        input('\n\nThese are the names of the player: \n' + print_this[0] + '\n' + print_this[int(amount_players)+1] + '\n' + print_this[int(amount_players) * 2+2] + '\n' + print_this[int(amount_players) * 3+3] + "\nPress enter to pass...")
        player_naming = False
    else:
        print("This is no valid input, choose a number between 2 and 4 please!")
        player_naming = True

# The following three if-statements define the initial conditions of each player
if amount_players == '2':
    player1_money = 1500
    player2_money = 1500
    money = [player1_money, player2_money]
    player_place = [0, 0]

    input("\nYou're playing with 2 players, Press enter to start...")

elif amount_players == '3':
    player1_money = 1500
    player2_money = 1500
    player3_money = 1500
    money = [player1_money, player2_money, player3_money]
    player_place = [0, 0, 0]

    input("\nYou're playing with 3 players, Press enter to start...")

elif amount_players == '4':
    player1_money = 1500
    player2_money = 1500
    player3_money = 1500
    player4_money = 1500
    money = [player1_money, player2_money, player3_money, player4_money]
    player_place = [0, 0, 0, 0]

    input("\nYou're playing with 4 players, Press enter to start...")


# print(players)
# This is the game loop
while playing:
    player_range = range(len(players))

    for i in player_range:

        # Bankruptcy check
        if money[i] < 0:                    # check the current amount of money for player i

            # if money is equal or below zero, remove all data belonging to this player
            money.pop(i)
            players.pop(i)
            player_place.pop(i)
            player_range = range(len(players))
            
        # Actual game loop
        else:
            try:
                # check whether the board should update 1 or 2 characters
                if len(str(player_place[i])) == 2:
                    updated_board = board.replace(str(player_place[i]), " X")

                else:
                    updated_board = board.replace(str(player_place[i]), "X")

                print(updated_board)

            except NameError as ex:
                print(ex.args[0])

            input("player " + str(i+1) + ": " + players[i] + "\nYou're currently at " + places[player_place[i]] + "\n\nYou have: \n  " + str(money[i]) + " Euro's" + "\n\nThese are the properties you own:\n  " + str(property_list[i]) + "\n\nPlease roll the dice by pressing enter... \n\n")

            dice_count = rand.randint(1, 6)  # throwing the dice
            player_place[i] += dice_count    # player position in the board

            if player_place[i] > 16:
                player_place[i] = player_place[i] - 16      # resetting the position after every complete loop
                money[i] += 250                             # every time you go through start you earn 250

                try:
                    # check whether the board should update 1 or 2 characters
                    if len(str(player_place[i])) == 2:
                        updated_board = board.replace(str(player_place[i]), " X")

                    else:
                        updated_board = board.replace(str(player_place[i]), "X")

                    print(updated_board)

                except NameError as ex:
                    print(ex.args[0])

                input("You threw " + str(dice_count) + ", now you are at " + places[player_place[i]]+ "\n You passed start, you get 250 euros")

                if places[player_place[i]] not in all_possible_places:      # if you end up on a property which was already bought, you pay a fine to the owner
                    fine = int(prices[player_place[i]])/3
                    money[i] -= fine
                    player_receiver = [property_list.index(sub_list)for sub_list in property_list if places[player_place[i]] in sub_list]  # looking for the owner
                    money[player_receiver[0]] += fine  #player_receiver indexed as list due to comprehension. Since the list will only have one element, we take just the 0th one
                    input('It\'s already bought, you need to pay ' + str(fine) + " euro's\nYou're balance is " + str(money[i]) + "\nplayer " + str(players[player_receiver[0]]) + " now has " + str(money[player_receiver[0]]) + "euro's")

                else:       # if it is not already owned, you are allowed to decide whether to buy or not
                    decision = input('Do you want to buy this property? [Y] to confirm or any other key to cancel')
                    if decision.upper() == 'Y':
                        buying = True
                        while buying:
                            if player_place[i] % 4 != 0:  # the % operator returns the remainder of the division. Here we are checking whether the position is not divisible by 4. A.k.a are we on a corner?

                                print(questions[player_place[i]])
                                answer = str(input('What is the correct answer?'))
                                answer = answer.lower()

                                if answer == correct_answers[player_place[i]].lower(): # your answer is correct

                                    property_list[i].append(places[player_place[i]])
                                    money[i] -= int(prices[player_place[i]])
                                    all_possible_places.pop(all_possible_places.index(places[player_place[i]]))
                                    input('You have bought the property!\nYou have ' + str(money[i]) + " euro's left")
                                    buying = False

                                else:                                                   # your answer is wrong
                                    print('Sorry, you cannot buy anything here')
                                    input('The correct answer is: ' + correct_answers[player_place[i]].lower())
                                    buying = False

                            else:                                                       # this is printed in the case in which you fail the question
                                print('Sorry, you cannot buy anything here')
                                buying = False

                    elif decision.lower() == 'n':
                        input('Ok, then roll the dice again')

            elif player_place[i] == 12:   # Jail brings you back to the free parking
                try:
                    # check whether the board should update 1 or 2 characters
                    if len(str(player_place[i])) == 2:
                        updated_board = board.replace(str(player_place[i]), " X")

                    else:
                        updated_board = board.replace(str(player_place[i]), "X")

                    print(updated_board)

                except NameError as ex:
                    print(ex.args[0])

                input("You threw " + str(dice_count) + ", now you are at " + str(player_place[i]) + "\n" + "\nYou will go back to the park")
                player_place[i] = 4

            elif player_place[i] == 16:  # when you end up exactly at the start
                player_place[i] = player_place[i] - 16
                money[i] += 500

                try:
                    # check whether the board should update 1 or 2 characters
                    if len(str(player_place[i])) == 2:
                        updated_board = board.replace(str(player_place[i]), " X")

                    else:
                        updated_board = board.replace(str(player_place[i]), "X")

                    print(updated_board)

                except NameError as ex:
                    print(ex.args[0])

                input("You threw " + str(dice_count) + ", now you are at " + places[player_place[i]] + "\n You get 500 euros")

            elif player_place[i] == 4 or player_place[i] == 8:
                try:
                    # check whether the board should update 1 or 2 characters
                    if len(str(player_place[i])) == 2:
                        updated_board = board.replace(str(player_place[i]), " X")

                    else:
                        updated_board = board.replace(str(player_place[i]), "X")

                    print(updated_board)

                except NameError as ex:
                    print(ex.args[0])

                input("You threw " + str(dice_count) + ", now you are at " + places[player_place[i]] + "\nNothing happens. Please continue")
            else:
                try:
                    # check whether the board should update 1 or 2 characters
                    if len(str(player_place[i])) == 2:
                        updated_board = board.replace(str(player_place[i]), " X")

                    else:
                        updated_board = board.replace(str(player_place[i]), "X")

                    print(updated_board)

                except NameError as ex:
                    print(ex.args[0])

                input("You threw " + str(dice_count) + ", now you are at " + places[player_place[i]] + "\n" + ' It costs ' + prices[player_place[i]] +' euro\'s')
                if places[player_place[i]] not in all_possible_places:
                    fine = int(prices[player_place[i]])/3
                    money[i] -= fine
                    player_receiver = [property_list.index(sub_list)for sub_list in property_list if places[player_place[i]] in sub_list]
                    money[player_receiver[0]] += fine
                    input('It\'s already bought, you need to pay ' + str(fine) + " euro's\nYour balance is " + str(money[i]) + "\nplayer " + str(players[player_receiver[0]]) + " now has " + str(money[player_receiver[0]]) + " euro's")

                else:
                    decision = input('Do you want to buy this property? [Y] to confirm or any other key to cancel')
                    if decision.upper() == 'Y':
                        buying = True
                        while buying:
                            if money[i] >= int(prices[player_place[i]]):
                                if player_place[i] % 4 != 0:  # the % operator returns the remainder of the division. Here we are checking whether the position isnot divisible by 4
                                    print(questions[player_place[i]])
                                    answer = str(input('What is the correct answer?'))
                                    answer = answer.lower()

                                    if answer == correct_answers[player_place[i]].lower():

                                        property_list[i].append(places[player_place[i]])
                                        money[i] -= int(prices[player_place[i]])
                                        all_possible_places.pop(all_possible_places.index(places[player_place[i]]))
                                        input('You have bought the property!\nYou have ' + str(money[i]) + " euro's left")
                                        buying = False

                                    else:
                                        print('Sorry, you cannot buy anything here')
                                        input('The correct answer is: ' + correct_answers[player_place[i]].lower())
                                        buying = False

                                else:
                                    input('Sorry, you cannot buy anything here')
                                    buying = False
                            else:
                                input('Sorry, you cannot afford this property. Please continue.')
                                buying = False

                    elif decision.upper() == 'N':
                        input('Ok, then roll the dice again')