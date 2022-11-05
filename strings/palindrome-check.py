def isPalindrome(string):
    # Write your code here.
    left = 0
    right = len(string)-1
    ans  = True
    while left< right:
        if string[left] == string[right]:
            ans = True
            left +=1
            right -=1
        else:
            ans = False
            break
    return ans        
            
