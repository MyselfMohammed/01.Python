class calculateMarkPercentage () :
   
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