"""
python game Treasure Island
"""
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")


game_is_running = True

while True:
    got_to = input(
        "You're at a cross road. Where do you want to go?\nType \"left\" or \"right\"\n")
    if got_to.lower() == "right":
        print("You fell into a hole. Game Over.")
        break
    elif got_to.lower() == "left":
        lake_decision = input(
            "You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")

        if lake_decision.lower() == "swim":
            print("You get attacked by an angry trout. Game Over.")
            break

        elif lake_decision.lower() == "wait":
            house_decision = input(
                "You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?\n")

            if house_decision.lower() == "red":
                print("It's a room full of fire. Game Over")
                break
            elif house_decision.lower() == "yellow":
                print("You found the treasure! You Win!")
                break
            elif house_decision.lower() == "blue":
                print("You enter a room of beasts. Game Over.")
                break
            else:
                print("Yor decision was bad game over")
                break

        else:
            print("Yor decision was bad game over")
            break

    else:
        print("Yor decision was bad game over")
        break
