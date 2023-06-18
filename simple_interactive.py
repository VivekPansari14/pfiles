game_list=[0,1,2]

def display_game(game_list):
    print('current list: ')
    print(game_list)

def position_choice():
    choice="wrong"
    
    while choice not in ['0','1','2']:
        choice= input('enter number in (0,1,2):')
        
        if choice not in ['0','1','2']:
            print('invalid choice')
            
    return int(choice)

def replacement_choice(game_list, position):
    user_choice= input('type a string in here: ')
    
    game_list[position]= user_choice
    
    return game_list


def gameon_choice():
    choice="wrong"
    
    while choice not in ['Y', 'N']:
        choice= input('ENter your choice (Y,N): ')
        
        if choice not in ['Y', 'N']:
            print('invalid choice')
            
    return choice=='Y'

game_on = True
game_list = [0,1,2]

while game_on:
	display_game(game_list)
	position = position_choice()
	game_list = replacement_choice(game_list, position)
	display_game(game_list)

	game_on = gameon_choice()

    
if game_on==False:
    print('Thank u for playin')