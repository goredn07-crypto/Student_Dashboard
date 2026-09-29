# Creates a variable 'num' and initially assigns a space.
num = " "

# Runs the loop repeatedly until num is equal to 'n'.
while num.lower() != 'n':
    print("\n" + "~" * 30)
    print("\tSTUDENT HELPER")
    print("~" * 30)
    print(" |1| GRADE EVALUATION.\n |2| TRACK YOUR ATTENDANCE.\n |3| FFCS")
    print("~" * 30)
    
    # Asks the user to enter their preference
    choice = int(input("ENTER YOUR PREFERENCE=> "))
    
    if choice == 1:
        num_courses = int(input("ENTER NUMBER OF COURSES REGISTERED=> "))
        all_courses = [] # all courses registered.
        mis = []  # marks in subject.
        ais = []  # average in subject.
        grade = [] # grade acquired in subject.

        for i in range(num_courses):
            course = input(f"Enter course '{i+1}'=> ")
            all_courses.append(course)
            get_m = int(input(f"Enter your mark in '{course}'=> "))
            mis.append(get_m)
            get_a = float(input(f"Enter your class avg. in '{course}'=> "))
            ais.append(get_a)
            
        for i in range(num_courses):
            if mis[i] >= ais[i] + 10:
                grade.append("S")
            elif mis[i] >= ais[i] + 5 and mis[i] < ais[i] + 10:
                grade.append("A")
            elif mis[i] >= ais[i] - 5 and mis[i] < ais[i] + 5:
                grade.append("B")
            elif mis[i] >= ais[i] - 10 and mis[i] < ais[i] - 5:
                grade.append("C")
            elif mis[i] >= ais[i] - 15 and mis[i] > ais[i] - 10:
                grade.append("D")
            else:
                grade.append("F")
                
        print("\n" + "~" * 80)
        print("\tREPORT CARD")
        print("~" * 80)
        for i in range(num_courses):
            print("Course is:", all_courses[i])
            print("Scored mark=>", mis[i])
            print("Class avg.=>", ais[i])
            print("Grade=>", grade[i])
            print("_" * 80)
        print("~" * 80)
        
    elif choice == 2:
        tl_cl_ad = int(input("ENTER TOTAL NUMBER OF CLASSES ATTENDED => "))
        tl_cl = int(input("ENTER TOTAL NUMBER OF CLASSES SCHEDULED => "))
        tl_cl_p = int(input("ENTER NUMBER OF UPCOMING CLASSES => "))
        
        if tl_cl != 0:
            a = (tl_cl_ad / tl_cl) * 100        # Current attendance percentage
            ase = (75 / 100) * (tl_cl + tl_cl_p)# Classes needed for 75% overall
            c = ase - tl_cl_ad                  # Classes left to attend to reach 75%
            b = tl_cl_p - c                     # Classes that can be bunked
            
            if a < 75 and b >= 0:  
                print(f"YOU ARE CURRENTLY BELOW THE CRITERIA WITH: {a:.2f}% ATTENDANCE")
                print(f"YOU HAVE TO ATTEND '{c}' MORE CLASSES TO MAINTAIN 75% ATTENDANCE")
            elif a >= 75 and b >= 0:
                print(f"YOU ARE CURRENTLY ABOVE THE CRITERIA WITH: {a:.2f}% ATTENDANCE")
                print(f"YOU HAVE MAINTAINED 75% ATTENDANCE.")
                print(f"You can bunk {b} upcoming classes.")
            else:
                print("R.I.P - Mathematically impossible to reach 75%.")
        else:
            print("No classes scheduled yet.")
            
    elif choice == 3:
        ta = float(input("Enter Your Total attendance=> "))  
        gd = input("Enter your Grade=> ")
        # Properly reassign the lowercase string back to the variable
        gd = gd.lower()      
        
        if gd == 's' and ta >= 90:
            print("FFCS SLOT => 1")
        elif gd == 's' and ta >= 75 and ta < 90:
            print("FFCS SLOT => 2")
        elif gd == 'a' and ta >= 95:
            print("FFCS SLOT => 1")
        elif gd == 'a' and ta >= 85 and ta < 95:
            print("FFCS SLOT => 2")
        elif gd == 'a' and ta >= 75 and ta < 85:
            print("FFCS SLOT => 3")
        elif gd == 'b' and ta == 100:
            print("FFCS SLOT => 1")
        elif gd == 'b' and ta >= 95 and ta < 100:
            print("FFCS SLOT => 2")
        elif gd == 'b' and ta >= 85 and ta < 95:
            print("FFCS SLOT => 3")
        elif gd == 'c' and ta >= 90 and ta <= 100:
            print("FFCS SLOT => 3")
        elif gd == 'c' and ta >= 80 and ta < 90:
            print("FFCS SLOT => 4")
        elif gd == 'c' and ta >= 75 and ta < 80:
            print("FFCS SLOT => 5")
        elif gd == 'd' and ta >= 90 and ta <= 100:
            print("FFCS SLOT => 4")
        elif gd == 'd' and ta >= 85 and ta < 90:
            print("FFCS SLOT => 5")
        elif gd == 'd' and ta >= 80 and ta < 85:
            print("FFCS SLOT => 6")
        elif gd == 'd' and ta >= 75 and ta < 80:
            print("FFCS SLOT => 7")
        elif gd == 'e' and ta >= 90 and ta <= 100:
            print("FFCS SLOT => 5")
        elif gd == 'e' and ta >= 85 and ta < 90:
            print("FFCS SLOT => 6")
        elif gd == 'e' and ta >= 80 and ta < 85:
            print("FFCS SLOT => 7")
        elif gd == 'e' and ta >= 75 and ta < 80: # Fixed typo from 'd' to 'e'
            print("FFCS SLOT => 8")
        else:
            print("YOU ARE DEBARRED\nR.I.P")
            
    else:
        print("Enter Valid Choice!")
        
    x = input("\nPRESS Y TO CONTINUE OR N TO EXIT=> ")
    num = x
    
print("THANK YOU")
