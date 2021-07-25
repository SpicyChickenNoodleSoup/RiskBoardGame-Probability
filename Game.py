# Program to simulate an interactive simple game in which attacker wins if the highest dice they roll is higher than that of the defender.
# An accidental creation when I did not really understand the rules of Risk. As you can tell, this code formed the foundation of the rest.
import random

takeinput = True
while takeinput == True:
    Attacker_dicecount = int(input("Attacker, do you want to roll with 1, 2, or 3 dice: "))
    # checking if input values satisfy conditions and repeat until it does
    # condition: attacker dice count value cannot be 0 or negative, or more than 3 in the situation of Risk
    if Attacker_dicecount >= 1 and Attacker_dicecount <= 3:
        takeinput = False
    else:
        print("Attacker dice count values not within range. Repeat.")
    Defender_dicecount = int(input("Defender, do you want to roll with 1 or 2 dice: "))
    # condition: defender dice count value cannot be 0 or negative, or more than 2 in the situation of Risk
    if Defender_dicecount >= 1 and Defender_dicecount <= 2:
        takeinput = False
    else:
        print("Defender dice count values not within range. Repeat.")
    # condition: Number of dice attacker rolls cannot be less than defender
    if Attacker_dicecount >= Defender_dicecount:
        takeinput = False
    else:
        print("Attacker dice count value must be more or equal than defender dice count value. Repeat.")


def dice_roll_simulator(dicecount):
    result = []
    for i in range(dicecount):
        result.append(random.randint(1, 6))
    result.sort()
    return result

Attacker_result = dice_roll_simulator(Attacker_dicecount)
Defender_result = dice_roll_simulator(Defender_dicecount)

print("Attacker rolls: "+ str(Attacker_result))
print("Defender rolls: "+ str(Defender_result))

# Begin comparison of results
no_conclusion = True
while no_conclusion == True:
    if Attacker_result[-1] > Defender_result[-1]:
    # can also use max(list) method
        print("Attacker wins this round")
        no_conclusion = False
    elif Attacker_result[-1] < Defender_result[-1]:
        print("Defender wins this round")
        no_conclusion = False
    elif Attacker_result[-1] == Defender_result[-1]:
        no_conclusion = True

        del Attacker_result[-1]
        if len(Attacker_result) == 0:
            print("Tie.Defender wins this round")
            no_conclusion = False
        # can make function to get rid of repetition
        del Defender_result[-1]
        if len(Defender_result) == 0:
            print("Tie.Defender wins this round")
            no_conclusion = False
