import interaction
import slotmachine

prize_mult = {1: 2, 2: 4, 3: 6}  # Multiplication of prize depending on the rows hit

def game(deposit: int) -> int:
    """The game function, to place into while loop for (in)finite play"""
    lines_bet = interaction.get_number_of_lines()
    while True:  # Check if the bet isn't more than the balance
        bet = interaction.get_bet()
        total_bet = bet * lines_bet
        if total_bet > deposit:
            print(f'You do not have enough money to bet! \nYour current balance is: {deposit} '
                  f'and the total bet is {total_bet}. Please place your bet again')
        else:
            break

    print(f'Your deposit is: ${deposit}. You bet on {lines_bet} lines. The total bet is ${total_bet}')
    reels = slotmachine.spin_slot_machine(slotmachine.ROWS, slotmachine.COLUMNS, slotmachine.symbol_count)
    outcome = slotmachine.print_slots(reels)
    game_result = slotmachine.validate_win(outcome, lines_bet)
    if game_result:
        prize = total_bet * prize_mult[lines_bet]
        print(f'You won {prize}')
        deposit = deposit + prize
        print(f'Your deposit totals to: {deposit}')
    if not game_result:
        deposit = deposit - total_bet
        print(f'Bummer! You\'ve lost this time! Your deposit is now: ${deposit}')
    return  deposit  # Return the deposit left

def main():
    deposit = interaction.deposit()  # at the beginning of the game, get the deposit from the player
    while True:  # keep the game until player has money or won't decide to leave the game
        spin = game(deposit)  # one spin of the reel
        deposit = spin
        print(f'Your deposit totals now to: ${deposit}')
        quit_question = input('Do you want to play? Press Y to continue, N to leave\n')
        if deposit <= 0:
            print('Sorry, you have no additional money to lose!')
            quit()
        if quit_question.lower() == "n":
            break
    print(f'Your balance is: ${deposit}')
    return deposit

if __name__ == '__main__':
    main()