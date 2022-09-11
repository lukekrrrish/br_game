from mains import *

shots = 3

def start():
    global o_f
    choice = int(
        input("\n1 = End Game\nClick Anything other than 1 to start the game.\n"))
    if choice == 1:
        o_f = False
    else:
        yes_choice = int(
            input("\n1 = Back\nAnything else = Game\n"))
        if yes_choice == 1:
            start()
        else:
            gun_choice = int(
                input(f"\nWhich Gun Do u want to use?\n1 = Sniper\n2 = AR\n3 = Gernade\n4 = ShotGun\n"))
            if gun_choice == 1:
                sniper_choice = int(
                    input(f"\nWhich Sniper Do u want to use?\n1 = Rifle\n2 = bolt\n"))
                if sniper_choice == 1:
                    rifle_color_choice = int(
                        input(f"\nWhich Rifle Color Do u want to use?\n1 = Gray\n2 = Green\n3 = Blue\n4 = purple\n5 = red\n6 = gold\n"))
            if gun_choice == 2:
                sniper_choice = int(
                    input(f"\nWhich AR Do u want to use?\n1 = \n2 = \n3 = "))
                if sniper_choice == 1:
                    rifle_color_choice = int(
                        input(f"\nWhich AR Color Do u want to use?\n1 = Gray\n2 = Green\n3 = Blue\n4 = purple\n5 = red\n6 = gold\n"))
            if gun_choice == 2:
                sniper_choice = int(
                    input(f"\nWhich Gernade Do u want to use?\n1 = \n2 = \n3 = "))
                if sniper_choice == 1:
                    rifle_color_choice = int(
                        input(f"\nWhich  Color Do u want to use?\n1 = Gray\n2 = Green\n3 = Blue\n4 = purple\n5 = red\n6 = gold\n"))
            if gun_choice == 2:
                sniper_choice = int(
                    input(f"\nWhich AR Do u want to use?\n1 = \n2 = \n3 = "))
                if sniper_choice == 1:
                    rifle_color_choice = int(
                        input(f"\nWhich  Color Do u want to use?\n1 = Gray\n2 = Green\n3 = Blue\n4 = purple\n5 = red\n6 = gold\n"))
            if gun_choice == 2:
                sniper_choice = int(
                    input(f"\nWhich AR Do u want to use?\n1 = \n2 = \n3 = "))
                if sniper_choice == 1:
                    rifle_color_choice = int(
                        input(f"\nWhich  Color Do u want to use?\n1 = Gray\n2 = Green\n3 = Blue\n4 = purple\n5 = red\n6 = gold\n"))
            


while o_f:
    start()
