"""Randomly pick customer and print customer info"""

from customers import get_customers_from_file
from random import choice

def pick_winner(customers):
    """pick a random winner from customer list"""

    winner = choice(customers)
    print(f'Tell {winner.name} at {winner.email} they are the winner!')


def run_raffle(filename):
    """run the raffle"""

    customers = get_customers_from_file(filename)
    pick_winner(customers)

if __name__ == '__main__':
    run_raffle('customers.txt')