string = input('Please enter your word: ').lower()

def isPalindrome(string): 
    for i in range(0, len(string)//2):  
        if string[i] != string[len(string)-i-1]: 
            return False
    return True

print(isPalindrome(string))
