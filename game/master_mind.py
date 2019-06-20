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
    # Iterarion total option
    for i in range(len(random_choise)):
        if inpunt_value[i] == random_choise[i]:
            correct_color.append('black')
        if inpunt_value[i] != random_choise[i] and inpunt_value[i] in random_choise:
            guessed_color.append('white')
    print(
        'Correct values: {correct_color}'.format(
            correct_color=', '.join(correct_color)
        )
    )
    print(
        "values ​​that exist, but are not in their right "
        "place: {guessed_color}".format(
            guessed_color=', '.join(guessed_color)
        )
    )
    # Validate if the values ​​are correct
    if len(correct_color) == max_chips:
        if attempts == 1:
            print ("Wow! On the first try!")
        else:
            print (
                "Excellent you have achieved in {attempts} attempts".format(
                    attempts=attempts
                )
            )
        can_play = False

    # Validate if there are still attempts
    if attempts >= 1 and attempts < max_attempts and len(correct_color) != max_chips:
        print ("New attempt: ")
    elif attempts >= max_attempts:
        print (
            'You have not reached it in a maximum of {max_attempts} attempts, '
            'the color code is {random_choise}'.format(
                max_attempts=max_attempts,
                random_choise=random_choise
            )
        )
