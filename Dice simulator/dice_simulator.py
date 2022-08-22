import random

dice_sides = {1: "|     |\n|  0  |\n|     |",
              2: "|  0  |\n|     |\n|  0  |",
              3: "|  0  |\n|  0  |\n|  0  |",
              4: "|0   0|\n|     |\n|0   0|",
              5: "|0   0|\n|  0  |\n|0   0|",
              6: "|0   0|\n|0   0|\n|0   0|"}
def simulator():
    side = random.randint(1,7)
    print(dice_sides[side])
    choice = input("Do you want to run dice simulator?")
    runner(choice)

def runner(choice="Y"):
    if choice in ['y','yes','Y',"Yes"]:
        simulator()
    elif choice in ['n','no','N',"No"]:
        exit()
    else:
        print("Invalid choice, try again!")
        runner()

runner()
