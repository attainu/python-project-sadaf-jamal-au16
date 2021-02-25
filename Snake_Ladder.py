# Text based snake and ladder game
import time
import random
import sys

# just of effects. add a delay of 1 second before performing any action
TIME_BETWEEN_ACTIONS = 1
MAX_VAL = 100
DICE_FACE = 6

# snake takes you down from 'key' to 'value'
snakes = {
    31:14,
    41:20,
    59:37,
    67:49,
    83:80,
    92:76,
    99:5
}

# ladder takes you up from 'key' to 'value'
ladders = {
    2:23,
    8:12,
    17:93,
    29:54,
    32:51,
    39:80,
    62:78,
    70:89,
    75:96
}

player_turn_message = [
    "Your turn.",
    "Go.",
    "Please proceed.",
    "Lets win this.",
    "Are you ready?",
    "",
]

snake_bite_message = [
    "hishhhh",
    "bite bite now no fight",
    "Ab tu toh gyaaaa",
    "Alas,You lost",
    "Yellow Yellow I am the dirty fellow"
]

ladder_jump_message = [
    "hurray",
    "Congrats,you jumped up",
    "Hip Hip Hurray",
    "oh my God...",
    "Maza Agyaaa"
]


def welcome_message():
    message = """
    Welcome to Snake and Ladder Game
    
    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
    
    """
    print(message)


def get_player_names():
    Warrior1_name = None
    while not Warrior1_name:
        Warrior1_name = input("Please enter a valid name for first player: ").strip()

    Warrior2_name = None
    while not Warrior2_name:
        Warrior2_name = input("Please enter a valid name for second player: ").strip()

    print("\nMatch will be played between '" + Warrior1_name + "' and '" + Warrior2_name + "'\n")
    return Warrior1_name,Warrior2_name


def get_dice_random_value():
    time.sleep(TIME_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(previous_value, current_value, get_player_name):
    print("\n" + random.choice(snake_bite_message).upper() + " ~~~~~~~~>")
    print("\n" + get_player_name + " got a snake bite. Down from " + str(previous_value) + " to " + str(current_value))


def got_ladder_jump(previous_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump_message).upper() + "########")
    print("\n" + player_name + " climbed the ladder from " + str(previous_value) + " to " + str(current_value))


def snake_ladder(get_player_name, current_value, dice_value):
    time.sleep(TIME_BETWEEN_ACTIONS)
    previous_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - previous_value) + " to win this game. Keep trying.")
        return previous_value

    print("\n" + get_player_name + " moved from " + str(previous_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, get_player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, get_player_name)

    else:
        final_value = current_value

    return final_value


def check_win(get_player_name, position):
    time.sleep(TIME_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + get_player_name + " won the game.")
        print("Congratulations " + get_player_name)
        print("\nThank you for playing the game\n\n")
        sys.exit(1)


def start():
    welcome_message()
    time.sleep(TIME_BETWEEN_ACTIONS)
    Warrior1_name, Warrior2_name = get_player_names()
    time.sleep(TIME_BETWEEN_ACTIONS)

    Warrior1_current_position = 0
    Warrior2_current_position = 0

    while True:
        time.sleep(TIME_BETWEEN_ACTIONS)
        input_one = input("\n" + Warrior1_name + ": " + random.choice(player_turn_message) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_random_value()
        time.sleep(TIME_BETWEEN_ACTIONS)
        print(Warrior1_name  + " moving....")
        Warrior1_current_position = snake_ladder(Warrior1_name , Warrior1_current_position, dice_value)

        check_win(Warrior1_name , Warrior2_current_position)

        input_two = input("\n" + Warrior2_name  + ": " + random.choice(player_turn_message) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_random_value()
        time.sleep(TIME_BETWEEN_ACTIONS)
        print(Warrior2_name  + " moving....")
        Warrior2_current_position = snake_ladder(Warrior2_name, Warrior2_current_position, dice_value)

        check_win(Warrior2_name, Warrior2_current_position)


if __name__ == "__main__":
    start()