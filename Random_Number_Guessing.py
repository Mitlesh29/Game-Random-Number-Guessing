import random as re
import math
print("Click 1 to start| 0 to exit")
ch=int(input())
while(ch==1):
    print("Enter number range")
    lo,up=map(int,input().split())
    n=re.randint(lo,up)
    chances=math.log((up-lo)+1)   #guessing depending upon the range using log
    chances=int(chances)
    print("You have",chances,"chances")
    while(chances!=0):
        chances=chances-1
        guess=int(input())
        if(guess==n):
            print("Number found in %d chance ",chances)
        elif(guess>n):
            print("Guessing too high")
        else:
            print("Guessing too low")
    if(chances==0):
        print("Random number",n)
        print("Better luck next time")
    print('Click 1 to play again| 0 to exit')
    ch=int(input())
print("Thank you!")
