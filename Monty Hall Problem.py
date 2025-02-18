import random
def simulate(N):

    correct_guess_count = 0
    for i in range(0, N):
        door_with_car = select_door()
        guessed_door_no = select_door()

        new_guessed_door_no = switch_door(guessed_door_no, door_with_car)

        if door_with_car == new_guessed_door_no:
            correct_guess_count += 1

    return correct_guess_count
def select_door():

    r = random.random()

    if r < (1.0 / 3.0):
        return "A"

    elif r >= (1.0 / 3.0) and r < (2.0 / 3.0):

        return "B"

    return "C"

def switch_door(guessed_door_no, door_with_car):

    doors = {'A', 'B', 'C'}
    remaining_doors = doors.difference({guessed_door_no, door_with_car})

    host_opening = random.choice(list(remaining_doors))

    new_guessed_door_no = list(doors.difference({guessed_door_no, host_opening}))[0]

    return new_guessed_door_no



for N in [10000,100000, 1000000]:
    hits = simulate(N)

    print("Percentage of times guess was right = %", (100.0 * hits) / N)