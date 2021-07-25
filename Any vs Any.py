
print("This simulator calculates the probability for any possible combination of attacker and defender dice not limited to the game of Risk. Can freely set number of attacker and defender dice and number of sides of dice."))
import random


random.seed(1234)


def dice_roll_simulator(dicecount,n):
    result = []
    for i in range(dicecount):
        result.append(random.randint(1, n))
    result.sort(reverse=True)
    return result


def battle(a, d, n):
    attacker_result = dice_roll_simulator(a,n)
    defender_result = dice_roll_simulator(d,n)
    a_wins_per_round = 0
    for i in range(d):
        if attacker_result[i] > defender_result[i]:
            a_wins_per_round = a_wins_per_round + 1
    return a_wins_per_round


takeinput = True
while takeinput == True:
    attacker_dicecount = int(input("Attacker, how many dice do you want to roll: "))
    if attacker_dicecount >= 1:
        takeinput = False
    else:
        print("Attacker dice count values cannot be less than 1. Repeat.")

    defender_dicecount = int(input("Defender, how many dice do you want to roll: "))
    if defender_dicecount >= 1:
        takeinput = False
    else:
        print("Defender dice count values cannot be less than 1. Repeat.")
    if attacker_dicecount >= defender_dicecount:
        takeinput = False
    else:
        print("Attacker dice count value must be more or equal than defender dice count value. Repeat.")

dicesides = int(input("How many sides does your dice have? "))

roundcount = int(input("How many rounds do you want to simulate? "))


att_win_k = {}
for i in range(0,defender_dicecount+1):
    key = i
    value = 0
    att_win_k[key] = value


for i in range(roundcount):
    single_battle = battle(attacker_dicecount, defender_dicecount, dicesides)
    for i in range(0,defender_dicecount+1):
        if single_battle == i:
            att_win_k[i] += 1


prob_att_win_k = {}
for i in range(0,defender_dicecount+1):
    key1 = i
    value1 = att_win_k[i] / roundcount
    prob_att_win_k[key1] = value1

print(prob_att_win_k)


prob_sum = 0
for i in range(0,defender_dicecount+1):
    prob_sum += prob_att_win_k[i]
if prob_sum == 1:
    print("Simulation successful")




