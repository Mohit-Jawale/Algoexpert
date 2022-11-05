def runLengthEncoding(string):
    # Write your code here.
    
    ans = []
    count = 1
    for i in range(1,len(string)):
        if count < 10 and string[i-1]==string[i]:
            count+=1
        else:
            if count<10:
                 ans.append(str(count)+string[i-1])
                 count = 1
            else:
                ans.append('9'+string[i-1])
                count = 2
            
    if count<10:
        ans.append(str(count)+string[len(string)-1])        
    else:
        ans.append('9'+string[i-1])
        ans.append(str(count-9)+string[i-1])
        
    return("".join(ans))    
            
