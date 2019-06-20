import random

max_chips = 4
# Set base color
base_color = ['R', 'B', 'Y', 'G', 'W', 'O']
attempts = 0
can_play = True
max_attempts = 10
while can_play:
    correct_color = []
    color_code = ''
    guessed_color = []
    # Convert input to uppercase
    print(
        'Available values {}'.format(
            ', '.join(base_color)
        )
    )
    inpunt_value = input().upper()
    # Convert String to List
    inpunt_value = [x for x in inpunt_value]
    attempts += 1
    # create random base of colors
    random_choise = random.sample(base_color, max_chips)
    if len(random_choise) != len(inpunt_value):
        print('Only four values ​​can be added')
        continue

