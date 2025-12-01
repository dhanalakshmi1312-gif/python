print("--- Job Eligibility Check ---")
aptitudemarks = int(input("Enter Marks in Aptitude (out of 100): "))
gdmarks = int(input("Enter Marks in gd (out of 100): "))
technicalmarks = int(input("Enter Marks in technical (out of 100): "))
hrmarks = int(input("Enter Marks in hr (out of 100): "))


if aptitudemarks >=85 and gdmarks >=90 and technicalmarks >= 80 and hrmarks >=95:
    total = aptitudemarks + gdmarks +technicalmarks + hrmarks
    print("the total marks=",total)
        
    if total >=390 :
         print("Congratulations! The candidate is ELIGIBLE for the job for RS.30000")
             
    elif total >=380 :
        print("Congratulations! The candidate is ELIGIBLE for the job for RS.28000")
           
    elif total >=370 :
        print("Congratulations! The candidate is ELIGIBLE for the job for RS.25000")
    elif total >=350:
        print("Congratulations! The candidate is ELIGIBLE for the job for RS.20000")


else:
    print("not eligible")   

