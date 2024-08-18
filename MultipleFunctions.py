class multipleFunctionedClass () :
    def isYourNumberOddOrEven ():
        num=int(input("Enter any Number to Check that It is Odd or Even :"))
        if((num%2)==0):
            print("Entered Number is Even")
            message="Returned Value is Even"
        else:
            print("Entered Number is Odd")
            message="Returned Value is Odd"
        return message


    def BMI():
        bmi=int(input("Enter the Your BMI Index :"))
        if (bmi<16.5):
         print("Severely Underweight")
         message="Severely Underweight"
        elif(bmi<18.5):
         print("Underweight")
         message="Underweight"
        elif(bmi<25):
         print("Normal")
         message="Normal"
        elif(bmi<30):
         print("Overweight")
         message="Overweight"
        elif(bmi<35):
         print("Obese Class - 01")
         message="Obese Class - 01"
        elif(bmi<40):
         print("Obese Class - 02")
         message="Obese Class - 02"
        elif(bmi<45):
         print("Severely Obese")
         message="Severely Obese"
        elif(bmi<50):
         print("Morbidly Obese")
         message="Morbidly Obese"
        elif(bmi<60):
         print("Super Obese")
         message="Super Obese"
        else:
         print("Hyper Obese")
         message="Hyper Obese"
        return message

#Create a function and list out the items in the list

    def topicsInAI():
        
        topics=["Sub-fields in AI are:","Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        verticalString=''
        
        for eachTopic in topics :
         verticalString+= eachTopic + "\n"
                
        print(str(verticalString))

# Create a function that checks whether the given number is Odd or Even
    def isYourNumberOddOrEven ():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num,"is Even Number")
        else:
            print(num,"is Odd Number")

# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def marriageEligibilityCheck(gender,age):
          
          if gender == ("Male") and age>=21:
              print("Your Gender :", gender)
              print("Your Age :", age)
              print ("Eligible For Marriage")
          elif gender == ("Male") and age<21:
              print("Your Gender :", gender)
              print("Your Age :", age)
              print ("Not Eligible For Marriage")
          elif gender == ("Female") and age>=18:
              print("Your Gender :", gender)
              print("Your Age :", age)
              print ("Eligible For Marriage")
          else: #gender == ("Female") and age<18:
              print("Your Gender :", gender)
              print("Your Age :", age)
              print ("Not Eligible For Marriage")


# calculate the percentage of your 10th mark

    def calculateMarkPercentage(Tamil,English,Maths,Science,SocialScience):
        print("Subject-01 :",Tamil)
        print("Subject-02 :",English)
        print("Subject-03 :",Maths)
        print("Subject-04 :",Science)
        print("Subject-05 :",SocialScience)
        total=(Tamil+English+Maths+Science+SocialScience)
        print("Total :", total)
        print("Percentage :",((float(total / 500)) * 100))

#print area of triangle using functions

    def areaOfTriangle(Height,Breadth):
        print("Height :",Height)
        print("Breadh :",Breadth)
        print("Area of Triangle :",(Height*Breadth)/2)

#print perimeter of triangle using functions

    def perimeterOfTriangle(Height1,Height2,Breadth):
        print("Height-01 :",Height1)
        print("Height-02 :",Height2)
        print("Breadh :",Breadth)
        print("Perimeter of Triangle :",(Height1 + Height2 + Breadth))