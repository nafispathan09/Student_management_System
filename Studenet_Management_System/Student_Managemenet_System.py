
students=[]
def add_student():
        
        while True:
            while True:
                name=input("Enter Student Name     :  ")
                if name.strip()=="":
                     print("name cant be empty")
                     continue
                else :
                     break
            while True:      
                try :
         
                    while True:
                        duplicate=False          
                        roll=int(input("Enter Student Roll No :   "))
                        for student in students:
                            if student["Roll"]==roll:
                                print("this roll no already exists ")
                                duplicate=True
                                break

                        if duplicate==True:
                          continue
                        else:
                             break
                          
                    break
                except ValueError:
                     print("invalid input pleae enter valid input")         









            while True:
                try:
                    while True:
                        pymarks=int(input("Enter python marks"))
                        if pymarks<0 or pymarks>100:
                             print(" enter marks beetween 1 to 100")
                             continue
                        else:
                            break
                    while True:                           
                            dbmsmarks=int(input("Enter database marks"))                            
                            if dbmsmarks<0 or dbmsmarks>100:
                                 print(" enter marks beetween 1 to 100")
                                 continue
                            else:                               
                                break
                    while True:               
                            javamarks=int(input("Enter java marks"))
                            if javamarks<0 or javamarks>100:
                                 print(" enter marks beetween 1 to 100")
                                 continue
                            else:                                
                                break
                    break
                
                
                except ValueError :
                     print ("invalid input pleae enter valid input")
            marks=pymarks+dbmsmarks+javamarks
            percentage=marks/300*100
            grade,result=calculate_grade(percentage)
            student={"Name":name,"Roll":roll,"Marks":marks,"Grade":grade,"Result":result,
                     "py":pymarks,"dbms":dbmsmarks,"java":javamarks,"Percentage":percentage
                     }
            students.append(student)
            again=input('"Press "ENTER" for new entry "n" for Exit"').lower()
            if again=="n":
                break










def student_list(students):
        print()
        print("-------------  Student list ---------------")
        
        for student in students :
             display_student(student)
        print("------------------------------------------")
def student_search(students):    
        search=int(input("Enter a Roll No to search a student record :- "))
       
        found=False

        for student in students :
            if student["Roll"]==search:
                print()
                print("---------- FOUND -----------------")
                
                display_student(student)
                
                print("-----------------------------")
                
                found=True
        if found == False:
            print("Student not found !! ") 
def student_update(students):
        updating=int(input("Enter a number for updaating "))
        found=False
        for student in students :
            if updating==student["Roll"]:
                found=True
                name=student["Name"]
            
                search_str=str(updating)
                upd=input("Press 'ENTER' for updating Roll no " + search_str+"  "+name+" 's details, ('n') for exit").lower()
                if upd=="n":
                    return
                else:

                    while True:
                         newname=input("Enter new name :- ")
                         if newname.strip()=="":
                              print(" Name cant be empty !!!!")
                              continue
                         else :
                              break
                         
                    



                    
                    while True:
                         found=False
                         newroll=int(input("Enter new roll no :- "))
                         for student in students:
                              if student["Roll"]==newroll:
                                   found=True
                                   print(newroll,"this roll no is already exists enter other number !!!!")
                                   break
                         if found==False:
                              break   
                             
                        


                    




                    while True:
                        newmarks=int(input("Enter new marks"))
                        if newmarks<0 or newmarks>100:
                             print("enter marks between 0 to 100")
                             continue
                        else:
                             break
                        


                   
            
                  
                student["Roll"]=newroll
                student["Name"]=newname
                student["Marks"]=newmarks
                upd_student=student
                       
                       
                    
                if found:
                    print("updated student is ",upd_student)
               
        if found==False:
             print("Student didnt found")           
def delete_student(students):
        dele=input("Press 'ENTER' for deleate a student from record ('n') for exit :- ")
        found=False
        if dele !="n":
            delnum=int(input("Enter student number for deleate :- "))
            for student in students:
                if student["Roll"]==delnum:
                    student_to_del=student
                    found=True
                    break
            if found:
                 students.remove(student_to_del)
                 print(" Student ",delnum," deleted successfully !!!")
            else:
                 print("Student didnt found !!!!")
         
        else:
            return
def display_student(student):
    
        print("Name",student["Name"])
        print("Roll No.",student["Roll"])
        print()
        print("Python Marks ",student["py"]) 
        print("D.B.M.S. Marks ",student["dbms"])
        print("Java Marks ",student["java"])
        print("Grade ",student["Grade"])
        print("Total Marks ",student["Marks"])
        print("Percentage ",student["Percentage"])
        print("Result ",student["Result"])
        
        print()
         
    

def calculate_grade(percentage):
    result="pass"
    

    if percentage>=90:
        grade="A"
    elif percentage>=75:
         grade="B"
    elif percentage>=50:
        grade="C"
    elif percentage>=33:
        grade="D"
    else:
        grade="F"
        result="fail"
    

    return grade , result




while True:
    print()
    print("hello nafis khan ")
    print("==============ENTER================")
    print("1 for add students\n" \
    "2 for see student list\n3 for search student \n4 for update student\n5 for delete student \n6 for 'EXIT'"   )
    print("===================================")
    
    while True:
         try :
                   call=int(input("add choice   :  "))
                   break
         except ValueError :
                  print("enter valid choice")
                  
         
    
    
    
    
    if call==6:
           break
    elif call==1:
        print("welcome to add student function ")
        add_student()
    elif call==2:
        print("welcome to see student ")
        student_list(students)
    elif call==3:
        print("welcome to search student ")
        student_search(students)
    elif call==4:
        print("welcome to update ")
        student_update(students)
    elif call==5:
          print("welcome to delete student ")
          delete_student(students)
          
    else:
        print("Please enter valid input !!! ")

