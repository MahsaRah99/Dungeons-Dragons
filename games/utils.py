from random import randint


def roll_dice(dice_type):
    if dice_type == "d%":
        return randint(1, 10) * 10
    else:
        return randint(1, int(dice_type[1:]))


def roll_dices(dice_dict):
    result = {}
    for dice_type, num_rolls in dice_dict.items():
        if num_rolls > 0:
            result[dice_type] = [roll_dice(dice_type) for _ in range(num_rolls)]
        else:
            result[dice_type] = []
    return result
