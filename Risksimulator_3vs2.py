print("This simulator calculates the probability for any possible combination of attacker and defender dice in the game of Risk.")
import random

random.seed(1234)

# simulates rolling of 6-sided dice n times depending on number of dice
def dice_roll_simulator(dicecount):
    result = []
    for i in range(dicecount):
        result.append(random.randint(1, 6))
    result.sort(reverse=True)
    # sorts with in descending order to easily compare highest value later
    return result

# simulates one round of battle for a certain number of attacker and defender dice
def battle(a, d):
    attacker_result = dice_roll_simulator(a)
    defender_result = dice_roll_simulator(d)
    a_wins_per_round = 0
    # compare highest value of attacker and defender dice multiple times
    # and counts number of times attacker wins for this combination of dice results
    for i in range(d):
        if attacker_result[i] > defender_result[i]:
            a_wins_per_round = a_wins_per_round + 1
    return a_wins_per_round

# taking values for number of dice attacker and defender rolls
takeinput = True
while takeinput == True:
    attacker_dicecount = int(input("Attacker, do you want to roll with 1, 2, or 3 dice: "))
    # checking if input values satisfy conditions and repeat until it does
    # condition: attacker dice count value cannot be 0 or negative, or more than 3 in the situation of Risk
    if attacker_dicecount >= 1 and attacker_dicecount <= 3:
        takeinput = False
    else:
        print("Attacker dice count values not within range. Repeat.")
    defender_dicecount = int(input("Defender, do you want to roll with 1 or 2 dice: "))
    # condition: defender dice count value cannot be 0 or negative, or more than 2 in the situation of Risk
    if defender_dicecount >= 1 and defender_dicecount <= 2:
        takeinput = False
    else:
        print("Defender dice count values not within range. Repeat.")
    # condition: Number of dice attacker rolls cannot be less than defender
    if attacker_dicecount >= defender_dicecount:
        takeinput = False
    else:
        print("Attacker dice count value must be more or equal than defender dice count value. Repeat.")

# taking value for number of rounds to simulate
roundcount = int(input("How many rounds do you want to simulate? "))


att_win0 = 0
att_win1 = 0
att_win2 = 0
att_win3 = 0
# for n rounds, count total number of times attacker wins 0, 1, 2 times
for i in range(roundcount):
    single_battle = battle(attacker_dicecount, defender_dicecount)
    if single_battle == 0:
        att_win0 = att_win0 + 1
    if single_battle == 1:
        att_win1 = att_win1 + 1
    if single_battle == 2:
        att_win2 = att_win2 + 1
# calculating probability
prob_att_win0 = att_win0 / roundcount
prob_att_win1 = att_win1 / roundcount
prob_att_win2 = att_win2 / roundcount

print("Prob of Attacker winning 0 army: ", str(prob_att_win0))
print("Prob of Attacker winning 1 army: ", str(prob_att_win1))
print("Prob of Attacker winning 2 army: ", str(prob_att_win2))

if prob_att_win0 + prob_att_win1 + prob_att_win2 == 1:
    print("Simulation successful")
