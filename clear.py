from os import system, name as nm
import art

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

# def check_type(expected_type, question):
#     check = False
#     options = {
#         int : "number"
#     }
#     while check == False:
#         user_input = input(f"{question}: ")
#         if type(expected_type) == type(user_input):
#             check = True
#         else: 
#             print()
#     return user_input 