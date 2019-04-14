import random as rn
import time
import numpy as np


def simulation(spins, items, picked_number):
    """This method simulates a roulette wheel. It calculates how often, on average, the roulette lands on the same
     number in a row twice and three times. It calculates the amount of time it takes for the roulette to land on
     a specific number. Lastly, it calculates the longest run of even and odd numbers."""

    last_num_list = []
    spins_to_pick_a_number = 0
    spins_to_pick_list = []

    match_three = 0
    match_two = 0

    even_numbers = 0
    max_even_numbers = 0
    odd_numbers = 0
    max_odd_numbers = 0

    for spin in range(0, spins):


        number = items[rn.randint(0, len(items)-1)]
        last_num_list.append(number)
        spins_to_pick_a_number += 1

        # if two subsequent numbers match, increment
        if len(last_num_list) > 1 and number == last_num_list[-2]:
            match_two += 1

            # if three subsequent numbers match, increment
            if len(last_num_list) > 2 and number == last_num_list[-3]:
                match_three += 1

            #calculate the number of spins required to land on a number
            spins_to_pick_a_number = spins_to_match_number(number, picked_number, spins_to_pick_list, spins_to_pick_a_number)

            #find the longest run of even number
            even_numbers, max_even_numbers = increment_longest_run(number, even_numbers, max_even_numbers, even=True)

            #find the longest run of odd number
            odd_numbers, max_odd_numbers = increment_longest_run(number, odd_numbers, max_odd_numbers, even=False)

        else:
            last_num_list = last_num_list[-2::]

    avg_spins_to_land_on_number = np.nanmean(spins_to_pick_list) if len(spins_to_pick_list) > 0 else 0
    avg_match_on_two =  match_two/spins
    avg_match_on_three =  match_three/spins
    max_even_numbers = max_even_numbers+1
    max_odd_numbers = max_odd_numbers+1

    return avg_spins_to_land_on_number, avg_match_on_two, avg_match_on_three, max_even_numbers, max_odd_numbers

def increment_longest_run( number, increment, max_number, even=True):
    """Find the longest run of even and odd numbers."""

    x = 0 if even else 1

    if number % 2 == x and number > 0:
        increment += 1
        if increment > max_number:
            max_number = increment
    else:
        increment = 0

    return increment, max_number


def spins_to_match_number(number,picked_number, spins_to_pick_list, spins_to_pick_a_number):
    """Calculate the number of spins to pick the number specified"""

    if number == picked_number:
        spins_to_pick_list.append(spins_to_pick_a_number)
        spins_to_pick_a_number = 0

    return spins_to_pick_a_number


if __name__ == "__main__":
    """This is a European roulette wheel simulation. This simulation uses a random number generator to represent each spin
    of the roulette wheel. Four simulations are performed with increasing number of spins in each simulation.
    Statistics on the average number of spins required to land on a number, the average double matches, average, triple 
    matches, and longest run of even and odd numbers are recorded. This is to demonstrate that the probabilities of a 
    roulette wheel can be calculated empirically with the law of large numbers."""


    pick_a_number = 13
    items = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
             23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

    trials = [10000, 1000000, 100000000, 10000000000]

    for spins in trials:
        start = time.time()

        avg_spins_to_land_on_number, avg_match_on_two , avg_match_on_three, max_even_numbers, max_odd_numbers = simulation(spins, items, pick_a_number)

        print(
            "Spins: {} \nAvg Spins to Land on Number: {} \nAvg Match Two: {} \nAvg Match Three: {} \nLongest Run of Evens: {} \nLongest Run of Odd: {}".format(
                spins, avg_spins_to_land_on_number, avg_match_on_two, avg_match_on_three, max_even_numbers, max_odd_numbers))


        print("\n{}\n".format(time.time() - start))
