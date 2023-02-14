########################################################################
###
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Ask for bank, return integer
##      2. Ask for wager. Must be greater than 0, less than or equal to bank. return int.
##      3. Get tuple of slot results. 3 results, each between 1 and 10
##      4. Find matches in tuple. Return amount of matching results (3, 2, or 0)
##      5. Get payout and apply to bank
##      6. Ask to play again
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    ans = input('Do you want to play again? ==> ')
    while ans not in ['Y', 'YES', 'N', 'NO']:
        print('You must enter Y/YES/N/NO to continue. Please try again')
        ans = input('Do you want to play again? ==> ')
    if ans == 'Y' or ans == 'YES':
        return True
    elif ans == 'N' or ans == 'NO':
         return False

def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    gamble = int(input('How many chips do you want to wager? ==> '))
    while gamble <= 0 or gamble > bank:
        if gamble <= 0:
            gamble = int(input('The wager amount must be greater than 0. Please enter again. \nHow many chips do you want to wager? ==> '))
        elif gamble > bank:
            print(f'The wager amount cannot be greater than how much you have.  {bank}\nHow many chips do you want to wager? ==> ')
    return gamble           

def get_slot_results():
    ''' Returns the result of the slot pull '''
    a = random.randrange(1, 10, 1)
    b = random.randrange(1, 10, 1)
    c = random.randrange(1, 10, 1)
    return a, b, c

def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    reels = [reela, reelb, reelc]
    unique = []
    for value in reels:
        if value not in unique:
            unique.append(value)
    if len(unique) == 3:
        return 0
    elif len(unique) == 2:
        return 2
    elif len(unique) == 1:
        return 3

def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    stacks = int(input('How many chips do you want to start with? ==> '))
    while stacks <= 0 or stacks > 100:
        if stacks <= 0:
            stacks = int(input('Too low a value, you can only choose 1 - 100 chips \nHow many chips do you want to start with? ==> '))
        elif stacks > 100:
            stacks = int(input('Too high a value, you can only choose 1 - 100 chips \nHow many chips do you want to start with? ==> '))
    return stacks

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 0:
        payout = -(wager)
    elif matches == 2:
        payout = wager * 2
    elif matches == 3:
        payout = wager * 9
    return payout    


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        original_bank = bank

        while bank > 0:  # Replace with condition for if they still have money.

            max_bank = bank

            spins = 0
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > max_bank:
                max_bank = bank
            spins += 1

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print(f'You lost all {original_bank} in {spins} spins')
        print("The most chips you had was", max_bank)
        playing = play_again()
