def create_players():
    success = False

    while success == False:
        playerNo = input('How many players will be playing?  ')
        print()

        try:
            playerNo = int(playerNo)
            success = True
            

        except TypeError:
            print('Please enter an integer')

        except:
            print('Unexpected issue, please try again')
            print()

    players = []

    for i in range (playerNo):
        print(i)

        print(players)
        
    

create_players()