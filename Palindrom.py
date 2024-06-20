def paldrm(string):
    s = string[ : :-1]
    if string == s:
        return True
    else:
        print(f"{string} is  not a palindrome")      
string = input("Please Enter the word to check if it is a palindrome: ")
paldrm(string)
