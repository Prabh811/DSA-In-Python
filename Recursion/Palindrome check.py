def palindrome(string, start, end):
    if start >= end:
       return True
       
    return string[start] == string[end] and palindrome(string, start + 1, end - 1) 
    
user_input = input()
print(palindrome(user_input, 0, len(user_input) - 1))