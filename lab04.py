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


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    ans = input('Do you want to play again? ==> ')
    while ans not in ('Y', 'YES', 'N', 'NO'):
        print('You must enter Y/YES/N/NO to continue. Please try again')
        ans = input('Do you want to play again? ==> ')
    if ans in ('Y', 'YES'):
        return True
     Elif ans in ('N', 'NO'):
         return False

def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''

    return 1            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''

    return 1, 2, 3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''

    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''

    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
