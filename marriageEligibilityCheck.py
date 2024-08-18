class marriageEligibilityCheck () :

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
