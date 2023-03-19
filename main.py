#! /usr/bin/env python3
"""
UK Income tax calculator
created by User3xample
find the source:
https://github.com/user3xample/uk_income_tax_check

licence:
https://github.com/user3xample/uk_income_tax_check/blob/main/LICENSE

I hope you find this useful.
"""

import os


def ask_exit():
    """function to just break out the while loop and end the program"""
    choice = input("Would you like to use again? [y,n]: ").lower()
    if choice == "n" or choice == "no":
        print("Ok, goodbye!")
        exit(0)


def clear_screen():
    """function for clearing the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


keep_running = True
while keep_running:  # a continuous while loop we use ask_exit() to break out of it.
    clear_screen()
    # Ask how much the user earns a year.
    user_income = int(input("How much is your yearly income? :£ "))
    clear_screen()
    print(f"\nAmount of yearly income entered: £ {user_income}\n")

    header = "BAND                  Taxable Income        Tax Rate"
    line = "_"*len(header)
    print(f"{header}\n{line}")
    personal_allowance = 12570
    print(f"Personal Allowance    Up to £12,570               0%")
    print(f"Basic Rate            £12,571 to £50270          20%")
    print(f"Higher Rate           £50,271 to £150,000        40%")
    print(f"Additional rate       Over £150,000              45%")
    print(line)

    if user_income <= personal_allowance:
        print("\nYou fall bellow the personal allowance and you will not pay tax on your income.")
        ask_exit()

    # rate of tax calc

    if user_income <= 50270:  # basic tax rate
        basic_rate = ((user_income - personal_allowance)/100)*20
        print(f"\nBasic rate               20%       £{basic_rate:.2f}")
        print(line)
        print(f"Total tax to pay yearly £ {basic_rate:.2f}")
        print(f"Total tax to pay monthly £ {((basic_rate)/12):.2f}")
        ask_exit()

    else:  # we know the user pays the max for this band and can move to the next band.
        basic_rate = ((50270-12571)/100)*20  # the max in this band
        print(f"\nBasic rate               20%       £{basic_rate:.2f}")

    if (user_income >= 50271) and (user_income <= 150000): # This is the higher rate tax band

        higher_rate = ((user_income - 50270)/100)*40  # we remove all the income under this band, dont want tax twice.

        print(f"Higher rate              40%       £{higher_rate:.2f}")
        print(line)
        print(f"Total tax to pay yearly £ {basic_rate + higher_rate:.2f}")
        print(f"Total tax to pay monthly £ {((basic_rate + higher_rate)/12):.2f}")
        ask_exit()

    if user_income >= 150001:  # anyone in the additional rate
        higher_rate = (150000/100)*40
        print(f"Higher rate              40%       £{higher_rate:.2f}")
        additional_rate = ((user_income - 150000)/100)*45  # The max for this band
        print(f"Additional rate          45%       £{additional_rate:.2f}")
        print(line)
        print(f"Total tax to pay yearly £ {basic_rate + higher_rate + additional_rate:.2f}")
        print(f"Total tax to pay monthly £ {((basic_rate + higher_rate + additional_rate)/12):.2f}")

        ask_exit()
