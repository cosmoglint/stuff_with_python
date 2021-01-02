import string
import random


# this is the string to be reached
target = "METHINKS IT IS LIKE A WEASEL"
tester = "METHINKS IT IS LIKE A WEASEL"

# tester = "YETHINKSPITXISHLIKEFA WQYSEY"

# these will be the sample sets for the monkey
alphabets_low = string.ascii_lowercase + " "
alphabets_up = string.ascii_uppercase + " "

def survival_score(current,target):
    score = 0
    for i,val in enumerate(current):
        score += abs(ord(val) - ord(target[i]))
    return score

print(survival_score(tester,target))


print(alphabets_up,alphabets_low)
