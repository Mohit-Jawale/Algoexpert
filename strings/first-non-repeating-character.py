import collections
def firstNonRepeatingCharacter(string):
    # Write your code here.

    counter_dict = collections.defaultdict(int)
    for i in string:
        counter_dict[i]+=1

    for j in range(len(string)):
        if counter_dict[string[j]] == 1:
            return j
            
    return -1
