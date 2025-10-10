print("--- Job Eligibility Check ---")
aptitudemarks = int(input("Enter Marks in Aptitude (out of 100): "))
gdmarks = int(input("Enter Marks in GD (out of 100): "))
technicalmarks = int(input("Enter Marks in Technical (out of 100): "))
hrmarks = int(input("Enter Marks in HR (out of 100): "))
if  aptitudemarks >=95:
        print("Congratulations! The candidate is ELIGIBLE for the job")
if gdmarks >=90:
        print("Congratulations! The candidate is ELIGIBLE for the job")
if  technicalmarks >=80:
        print("Congratulations! The candidate is ELIGIBLE for the job")
if  hrmarks >=95:
        print("Congratulations! The candidate is ELIGIBLE for the job")

    
elif aptitudemarks < 95:
            print("The candidate is NOT ELIGIBLE for the job")
elif gdmarks < 90:
            print("The candidate is NOT ELIGIBLE for the job")
elif technicalmarks < 80:
            print("The candidate is NOT ELIGIBLE for the job")
elif hrmarks < 95:
            print("The candidate is NOT ELIGIBLE for the job")

else:
    print("Invalid result")
