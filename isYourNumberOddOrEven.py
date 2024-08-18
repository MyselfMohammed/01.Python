class isYourNumberOddOrEven () :

# Create a function that checks whether the given number is Odd or Even
    def isYourNumberOddOrEven ():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")
