"""Module for interactions with user"""

MAX_LINES = 3  # Restrict the number of lines in slot machine up to 3
MAX_BET = 100  # Maximum individual bet
MIN_BET = 1  # Min individual bet

def deposit() -> int:
    """Receive the deposit from the user - do it continously as long as customer won't decline"""
    while True:
        amount: str = input('Please place your deposit \n$')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f'Your deposit is ${amount}')
                return amount
            else:
                print('The deposit must be higher than 0')
        else:
            print('Please enter your deposit as a number')  # Also for input deposit < 0
            
def get_number_of_lines() -> int:
    """Receive from the user the number of lines that he wants to bet on"""
    while True:
        no_lines: str = input(f'Please place number of lines you would like to bet on (1 - {MAX_LINES})\n')
        if no_lines.isdigit():
            no_lines = int(no_lines)
            if no_lines > 0 and no_lines <= MAX_LINES:  # Check if no of lines is in betwwen the range
                print(f'You bet on {no_lines} lines')
                return no_lines
            else:
                print('Number of lines must be higher than 0 but not higher than number of lines')
        else:
            print('Please enter number of lines as the number')  # Also for input < 0

def get_bet() -> int:
    """Receive from the user the number of lines that he wants to bet on"""
    while True:
        bet: str = input(f'How much would you like to bet? \n$')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:  # Check if bet is within the range
                print(f'You bet {bet}$')
                return bet
            else:
                print(f'Bet must be between ${MIN_BET} and ${MAX_BET}')
        else:
            print('Please enter the money that you want to bet')  # Also for input < 0


if __name__ == '__main__':
    deposit()
    get_number_of_lines()
    get_bet()

