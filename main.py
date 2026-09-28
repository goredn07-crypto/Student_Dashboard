#project 1.
num=" "
num.lower()
#creates a variable 'num' and initially assigns 0.
while(num!='n'):
#RUNS THE LOOP REPEATEDLY UNTIL  num IS NOT EQUAL TO 4.
#WHEN num BECOMES 4 THE LOOP TERMINATES/STOPS.
    print("\n"+"~"*30)
    print("\tSTUDENT HELPER")
    print("~"*30)
    print(" |1| GRADE EVALUATION.","\n","|2| TRACK YOUR ATTENDANCE.","\n","|3| FFCS")
    print("~"*30)
    #DISPLAYS THE STUDENT HELPER TABLE MENU, PROVIDING THE USER WITH OPTIONS. 
    #FOR GRADE EVALUATION,ATTENDANCE TRACKING,FFCS AND EXIT.
    choice=int(input("ENTER YOUR PREFERENCE=>"))
    #ASKS THE USER TO ENTER THEIR PREFERENCE WHICH IS CONVERTED INTO INETEGER BY 'int'.
    #IMPORTANT CONDITION BECAUSE USERS CHOICE IS GOING TO STOP THE LOOP.
    if choice==1:
    #CHECKS WHETHER USER SELECTED 1 FROM THE STUDENT HELPER MENU.
        num_courses=int(input("ENTER NUMBER OF COURSES REGISTERED=>"))
        #ASKS THE USER TO ENTER THE NUMBER OF COURSES REGISTERED BY THEM.
        all_courses=[] #all courses registered.
        #AN EMPTY LIST TO STORE ALL THE COURSES NAME.
        mis=[]  #marks in subject.
        #AN EMPTY LIST TO STORE MARKS ACHIEVED IN EVERY COURSE.
        ais=[]  #average in subject.
        #AN EMPTY LIST TO STORE THE AVERAGE IN EVERY COURSE.
        grade=[] #grade aquired in subject.
        #AN EMPTY LIST TO STORE THE GRADES ACCORDING TO THE MARKS.

        for i in range(num_courses):
            course=input(f"enter course '{i+1}'=>")
            all_courses.append(course)
            get_m=int(input(f"enter your mark in '{ course }' =>"))
            mis.append(get_m)
            get_a=float(input(f"enter your class avg. in '{ course }'=>"))
            ais.append(get_a)
        for i in range(num_courses):
        #REPEATES THE CODE ONCE FOR EVERY COURSE.
        #IF num_courses=N i WILL RUN N-1 TIMES.
            if mis[i]>=ais[i]+10:
                grade.append("S")
            elif mis[i]>=ais[i]+5 and mis[i]<ais[i]+10:
                grade.append("A")
            elif mis[i]>=ais[i]-5 and mis[i]<ais[i]+5:
                grade.append("B")
            elif mis[i]>=ais[i]-10 and  mis[i]<ais[i]-5:
                grade.append("C")
            elif mis[i]>=ais[i]-15 and mis[i]>ais[i]-10:
                grade.append("D")
            else:
                grade.append("F")
        print("\n"+"~"*80)
        print("\tREPORT CARD")
        print("~"*80)
        for i in range(num_courses):
            print("course is",all_courses[i])
            print("Scored mark=>",mis[i])
            print("Class avg.=>",ais[i])
            print("Grade=>",grade[i])
            print("_"*80)
        print("~"*80)
        #REPORT CARD MENU WITH DETAILS ENTERED BY USER AND CALCULATED.
    elif choice==2:
        #CHECKS WHETHER USER'S PREFERENCE IS 2 FROM USER'S PREFERENCE.
        tl_cl_ad=int(input("ENTER TOTAL NUMBER OF CLASSES ATTENDED =>"))  #TOTAL CLASSES ATTENDED. 
        tl_cl=int(input("ENTER TOTAL NUMBER OF CLASSES SCHEDULED =>"))    #TOTAL NUMBER OF CLASASES SCHEDULED.
        tl_cl_p=int(input("ENTER NUMBER OF UPCOMING CLASSES =>"))         #TOTAL NUMBER OF CLASSES PENDING.
        while (tl_cl!=0):
            a=(tl_cl_ad/tl_cl)*100      #FORMULA FOR ATTENDANCE CALCULATION.
            ase=(75/100)*(tl_cl+tl_cl_p)#TOTAL ATTENDANCE IN SEMESTER END. 
            c=(ase-tl_cl_ad)            #CLASSES LEFT TO COMPLETE 75% ATTENDANCE.
            d=tl_cl_p-c
            b=tl_cl_p-c                 #CLASSES CAN BE BUNKED.
            if(a<75 and d>=0):          
            #CHECKS ATTENDANCE CRITERIA WHETHER ATENDANCE IS LESS THEN 75%.
                print("YOU ARE CURRENTLY BELOW THE CRITERIA WITH:",a,"% ATTENDANCE")
                print(f"YOU HAVE TO ATTEND '{c}' CLASSES TO MAINTAIN 75% ATTENDANCE")
            elif(a>75 and d>=0):
            #CHECKS WHETHER ATTENDANCE IS ABOVE 75%
                print("YOU ARE CURRENTLY ABOVE THE CRITERIA WITH:",a,"% ATTENDANCE")
                print(f"YOU HAVE TO ATTENDed '{c}' CLASSES and MAINTAINED 75% ATTENDANCE")
                print("bunk", b)
            else:
                print("R.I.P")
    elif choice==3:
    #CHECKS WHETHER USER'S PREFERENCE IS 3 FROM USER'S PREFERENCE.
    #AND CALCULATES FFCS SLOT ACCORDING TO TOTAL ATTENDANCE AND GRADE.
        ta=float(input("Enter Your Total attendance=>"))  
        #TO STORE TOTAL ATTENDANCE.
        gd=input("Enter your Grade=>")                    
        #TO STORE GRADE.
        gd.lower()     
        #CONVERTS THE GRADE INTO LOWER CASE.
        if (gd=='s' and ta>=90):
            print("FFCS SLOT => 1")
        elif(gd=='s' and ta>=75 and ta<90):
            print("FFCS SLOT => 2")
        elif(gd=='a' and ta>=95):
            print("FFCS SLOT => 1")
        elif(gd=='a' and ta>=85 and ta<95):
            print("FFCS SLOT => 2")
        elif(gd=='a' and ta>=75 and ta<85):
            print("FFCS SLOT => 3")
        elif(gd=='b' and ta==100):
            print("FFCS SLOT => 1")
        elif(gd=='b' and ta>=95 and ta<100):
            print("FFCS SLOT => 2")
        elif(gd=='b' and ta>=85 and ta<95):
            print("FFCS SLOT => 3")
        elif(gd=='c' and ta>=90 and ta<=100):
            print("FFCS SLOT => 3")
        elif(gd=='c' and ta>=80 and ta<90):
            print("FFCS SLOT => 4")
        elif(gd=='c' and ta>=75 and ta<80):
            print("FFCS SLOT => 5")
        elif(gd=='d' and ta>=90 and ta<=100):
            print("FFCS SLOT => 4")
        elif(gd=='d' and ta>=85 and ta<90):
            print("FFCS SLOT => 5")
        elif(gd=='d' and ta>=80 and ta<85):
            print("FFCS SLOT => 6")
        elif(gd=='d' and ta>=75 and ta<80):
            print("FFCS SLOT => 7")
        elif(gd=='e' and ta>=90 and ta<=100):
            print("FFCS SLOT => 5")
        elif(gd=='e' and ta>=85 and ta<90):
            print("FFCS SLOT => 6")
        elif(gd=='e' and ta>=80 and ta<85):
            print("FFCS SLOT => 7")
        elif(gd=='d' and ta>=75 and ta<80):
            print("FFCS SLOT => 8")
        else:
            print('''YOU ARE DEBARRED
               R.I.P ''')
    else:
        print("Enter Valid Choice!")
    if(num!='n'):
        x=input("PRESS Y/N ENTER TO CONTINUE=>")
        #TO TAKE Y IF USER WANTS TO CONTINUE ELSE N TO STOP
        num=x
        if(x=="y" or x=="Y"):
             continue
print("THANK YOU")
#PRINTS "THANK YOU" WHEN USER ENDS 