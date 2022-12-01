# Algorithm for a Palindrome

def isPalindrome(str):
    startIndex =-1
    endIndex= (len(str))

    for x in str:
        startIndex +=1
        endIndex -=1
        if str[startIndex] != str[endIndex]:
          return False
    return True

print(isPalindrome('racecar'))
