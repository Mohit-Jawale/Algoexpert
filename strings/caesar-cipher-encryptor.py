def caesarCipherEncryptor(string, key):
    # Write your code here.
 
    ans = []
    for j in range(len(string)):
        i = ord(string[j])+(key%26)
        if i>96 and i<123:
            ans.append(chr(i))
        else:
            i = i%123+97
            ans.append(chr(i))        
    return("".join(ans))     
