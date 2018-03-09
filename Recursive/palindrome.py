def palindrome(userinput):
    reverseString = userinput[::-1]
    if userinput == reverseString:
        return True
    else:
        return False


print(palindrome('kayak'))
print(palindrome('i am here'))