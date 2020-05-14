import keyboard
import Drone_navigation_unit.Client.constants as movement_constants
import Drone_navigation_unit.Client.command_generator as CMD


def get_two_dimension_code():
    if keyboard.is_pressed(movement_constants.KEY_FORWARD):
        if keyboard.is_pressed(movement_constants.KEY_LEFT):
            return movement_constants.KEY_COMBO_WA
        if keyboard.is_pressed(movement_constants.KEY_RIGHT):
            return movement_constants.KEY_COMBO_WD
        return movement_constants.KEY_FORWARD

    if keyboard.is_pressed(movement_constants.KEY_REVERSE):
        if keyboard.is_pressed(movement_constants.KEY_LEFT):
            return movement_constants.KEY_COMBO_SA
        if keyboard.is_pressed(movement_constants.KEY_RIGHT):
            return movement_constants.KEY_COMBO_SD
        return movement_constants.KEY_REVERSE

    if keyboard.is_pressed(movement_constants.KEY_LEFT):
        return movement_constants.KEY_LEFT

    if keyboard.is_pressed(movement_constants.KEY_RIGHT):
        return movement_constants.KEY_RIGHT


def get_three_dimension_code():
    if keyboard.is_pressed(movement_constants.KEY_ASCEND):
        return movement_constants.KEY_ASCEND
    elif keyboard.is_pressed(movement_constants.KEY_DESCEND):
        return movement_constants.KEY_DESCEND
    else:
        return 'na'


def get_key_pressed():
    mov_2_d = get_two_dimension_code()
    mov_3_d = get_three_dimension_code()
    return CMD.generate(mov_2_d, mov_3_d)