import random
def rock_papper_scissors():
        moves=['r','p','s']

        while True:
            value=input('Enetr a Choice Of rock(r) or papper(p) scissors(s): ')
            if value not in moves:
                print( "please Eneter only 'P' for Papper 's' for scissors 'r' for Rock")
            break
        print("Invalid input! Please enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.")

        computer=random.choice(moves)
        print(f'Computer Choice: {computer}')
  

        if value == computer:
            return 'Tie'

        elif is_win(value,computer):
            return 'You Won!'
        else:
            return "You Lost!"
            

def is_win(player,opponents):
    if(player == 'r' and opponents == 's') or \
        (player == 's' and opponents == 'p') or \
        (player == 'p' and opponents == 'r'):
        return True 
    
a=rock_papper_scissors()
print(a)