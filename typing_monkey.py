import string
import random


# this is the string to be reached
target = "METHINKS IT IS LIKE A WEASEL"


# tester = "METHINKS IT IS LIKE A WEASEL"
tester = "YETHINKSPITXISHLIKEFA WQYSEY"

# these will be the sample sets for the monkey
alphabets_low = string.ascii_lowercase + " "
alphabets_up = string.ascii_uppercase + " "

variables = 27   # "a" - "z" and " "

# this is the highest value of survival you can get
min_survival = len(target) * variables

samples_per_generation = 10



def selection(generation_list):
    pass
def mutate(current,current_variation_list):
    global alphabets_up
    new = ""
    for i,val in enumerate(current_variation_list):
        if not(val):
            new += current[i]
        else:
            new += random.choice(alphabets_up)
    return new
    # pass

def survival_score(current,target):
    score = 0
    current_variation_list = []
    for i,val in enumerate(current):
        cur_score = abs(ord(val) - ord(target[i]))
        current_variation_list.append(cur_score)
        score += cur_score
    return score, current_variation_list




t_score, t_current_variation_list = survival_score(tester,target)
# print(t_score,t_current_variation_list)
print(mutate(tester,t_current_variation_list))
# print(alphabets_up,alphabets_low)
