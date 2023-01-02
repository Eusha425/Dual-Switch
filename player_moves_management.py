def return_player_turn_symbol(turn):
    player_turn_symbol = ""
    if turn % 2 != 0:
        player_turn_symbol = "X"
    else:
        player_turn_symbol = "O"
    return player_turn_symbol

def check_button_already_pressed(status_number):
    if status_number == 1:
        return 1
    else:
        return 0
