"""Print out all the melons"""


from melons import melons


def print_all_melons(melons):
    """Print each melon with with all additional information."""

    for melon_name, melon_characteristics in melons.items():
        print(melon_name)

        for melon_characteristic, value in melon_characteristics.items():
            print(f'{melon_characteristic}: {value}')
       
       print('')

print_all_melons(melons)

