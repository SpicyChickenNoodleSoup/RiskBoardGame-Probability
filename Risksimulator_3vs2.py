print("rolldice 3 vs 2")
import random

random.seed(1234)


def dice_roll_simulator(dicecount):
    result = []
    for i in range(dicecount):
        result.append(random.randint(1, 6))
    result.sort(reverse=True)
    return result


def battle(a, d):
    attacker_result = dice_roll_simulator(a)
    defender_result = dice_roll_simulator(d)
    a_wins_per_round = 0
    for i in range(d):
        if attacker_result[i] > defender_result[i]:
            a_wins_per_round = a_wins_per_round + 1
    return a_wins_per_round


takeinput = True
while takeinput == True:
    attacker_dicecount = int(input("Attacker, do you want to roll with 1, 2, or 3 dice: "))
    if attacker_dicecount >= 1 and attacker_dicecount <= 3:
        takeinput = False
    else:
        print("Attacker dice count values not within range. Repeat.")

    defender_dicecount = int(input("Defender, do you want to roll with 1 or 2 dice: "))
    if defender_dicecount >= 1 and defender_dicecount <= 2:
        takeinput = False
    else:
        print("Defender dice count values not within range. Repeat.")

roundcount = int(input("How many rounds do you want to simulate? "))

att_win0 = 0
att_win1 = 0
att_win2 = 0
att_win3 = 0

for i in range(roundcount):
    single_battle = battle(attacker_dicecount, defender_dicecount)
    if single_battle == 0:
        att_win0 = att_win0 + 1
    if single_battle == 1:
        att_win1 = att_win1 + 1
    if single_battle == 2:
        att_win2 = att_win2 + 1

prob_att_win0 = att_win0 / roundcount
prob_att_win1 = att_win1 / roundcount
prob_att_win2 = att_win2 / roundcount

print("Prob of Attacker winning 0 army: ", str(prob_att_win0))
print("Prob of Attacker winning 1 army: ", str(prob_att_win1))
print("Prob of Attacker winning 2 army: ", str(prob_att_win2))

if prob_att_win0 + prob_att_win1 + prob_att_win2 == 1:
    print("Simulation successful")


# def dice_roll_simulator(dicecount):
#     result = []
#     for i in range(dicecount):
#         result.append(random.randint(1, 6))
#     result.sort(reverse=True)
#     return result

# big=100000
# count_attackerwins1=0
# count_attackerwins2=0
#
# for i in range(big):
#     Attacker_result = dice_roll_simulator(3)
#     Defender_result = dice_roll_simulator(2)
#     wins1 = False
#     wins2 = False
#     if Attacker_result[0] > Defender_result[0]:
#         wins1 = True
#     del Attacker_result[0]
#     del Defender_result[0]
#     if Attacker_result[0] > Defender_result[0]:
#         wins1 = False
#         wins2 = True
#     if wins1:
#         count_attackerwins1 = count_attackerwins1 + 1
#     if wins2:
#         count_attackerwins2 = count_attackerwins2 + 1
#
#
# prob_attackerwins1 = count_attackerwins1 / big
# print(prob_attackerwins1)
#
# prob_attackerwins2 = count_attackerwins2 / big
# print(prob_attackerwins2)