def longestPalindromicSubstring(string):
    # Write your code here.
    left = 0
    right = len(string)-1
    start = 0
    end = right
    flag = 0
    def check_palindrome(l,r):
        ans = True
        while l<r:
            if string[l]== string[r]:
                ans = True
                l+=1
                r-=1
            else:
                ans = False
                break
        return ans   
        
    ans = 0
    left =0
    right = 0
    for i in range(len(string)):
        for j in reversed(range(len(string))):
           if ans < j+1-i:
               print(string[i:j+1])
               if check_palindrome(i,j):
                   ans = max(ans,j+1-i)
                   if ans == len(string[i:j+1]):
                       left = i
                       right = j+1
                   
              
            

    return string[left:right]
