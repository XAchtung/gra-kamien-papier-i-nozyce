from random import randint

''' Krystian Berg i Hubert Ambrożewicz'''

def user_interface(options):
    for index, option in enumerate(options):
        print(f'{index} = {option}')

    user_input = int(input('Co wybierasz?'))
    return user_input

def computer_choice(content):
    computer_chose = randint(0, len(content)-1)
    return computer_chose

def check_results(choices,player,computer):
    if player == computer:
        return 'remis'
    elif (player == 0 and computer == len(choices)-1) or (player>computer and not (player == len(choices)-1 and computer==0)):
        return 'wygrałeś'
    return 'przegrałeś'
    
def play():
    print('witaj w grze kamień i papier wybierz swój atut')
    options_list = ['kamień', 'papier', 'nożyczki', 'topór', 'drewno', 'nóż']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)

    print(f' player chose: {options_list[player_result]}')
    print(f' computer chose: {options_list[computer_result]}')

    results = check_results(options_list, player_result, computer_result)

    print(f'\n{results}')

def main():

    play_again = ''
    while play_again.lower()  != 'n':
        play()
        print (f'Chcesz zagrać ponownie?')
        play_again = input('napisz \'t\' dla tak albo \'n\' dla nie :')

main()