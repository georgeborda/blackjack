from os import system, name as nm
import utils.art as art

def reset_screen():
    """Clear the console"""
    # for windows
    if nm == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

    print(art.logo)

def farewell():
    """Clear the console"""
    # for windows
    if nm == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

    print(art.logo)
    print(f"\n  {art.byebye}")

