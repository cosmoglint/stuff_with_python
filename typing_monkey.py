import string
import random


# this is the string to be reached
target = "METHINKS IT IS LIKE A WEASEL"


# tester = "METHINKS IT IS LIKE A WEASEL"
tester = "YETHINKSAITXISHLIKEFA WQYSEY"
# tester = "SETHINKSRITHISXLIKEEA WBDSEP"


# these will be the sample sets for the monkey
alphabets_low = string.ascii_lowercase + " "
alphabets_up = string.ascii_uppercase + " "

alphabets_sample = alphabets_up

variables = 27   # "a" - "z" and " "

# this is the highest value of survival you can get
min_survival = len(target) * variables

samples_per_generation = 3
generation_list = ["".join(random.choices(alphabets_sample,k=len(target))) for i in range(samples_per_generation)]



def selection(generation_list):
    global target
    selected_org = min([tuple(survival_score(org,target)) + (org,)  for org in generation_list])
    return selected_org

def mutate(current,current_variation_list):
    global alphabets_sample
    new = ""
    for i,val in enumerate(current_variation_list):
        if not(val):
            new += current[i]
        else:
            rand_change = random.randint(min(current_variation_list[i],0),max(current_variation_list[i],0))
            rand_ind = alphabets_sample.index(current[i]) + rand_change
            # new += random.choice(alphabets_sample)
            new += alphabets_sample[rand_ind]
    return new


def survival_score(current,target):
    global alphabets_sample
    score = 0
    current_variation_list = []
    for i,val in enumerate(current):
        # cur_score = ord(val) - ord(target[i])
        cur_score =  - alphabets_sample.index(val) + alphabets_sample.index(target[i])

        current_variation_list.append(cur_score)
        score += abs(cur_score)
    return score, current_variation_list

def test(tester,target):
    global samples_per_generation
    t_score, t_current_variation_list = survival_score(tester,target)
    new = tester
    for i in range(samples_per_generation):
        new = mutate(new,t_current_variation_list)
        t_score, t_current_variation_list = survival_score(new,target)
    return new


# print(test(tester,target))
# print(selection(generation_list))

def main():
    global generation_list, samples_per_generation

    generation = 0
    org_score, org_var_list, org = selection(generation_list)
    generation_list = [mutate(org,org_var_list) for i in range(samples_per_generation)]
    while (org != target):
        generation += 1
        org_score, org_var_list, org = selection(generation_list)
        generation_list = [mutate(org,org_var_list) for i in range(samples_per_generation)]
        print(generation_list)
    return generation

print(main())

# t_score, t_current_variation_list = survival_score(tester,target)
# print(t_score,t_current_variation_list)
# print(mutate(tester,t_current_variation_list))
# print(alphabets_up,alphabets_low)
