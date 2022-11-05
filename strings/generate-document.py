import collections
def generateDocument(characters, document):
    # Write your code here.
    counter_dict = collections.defaultdict(int)

    for i in characters:
        counter_dict[i]+=1
    ans  = True
    
    for j in document:
        if counter_dict.get(j):
            counter_dict[j]-=1
        else:
            ans = False
            break
    return ans        
    
