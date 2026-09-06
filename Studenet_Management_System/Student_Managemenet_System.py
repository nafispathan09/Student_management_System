
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
                     print("invalid input pleae enter calid input")         
            while True:
                try:
                    while True:
                        marks=int(input("Enter Student Marks    : "))
                        if marks<0 or marks>100:
                             print(" enter marks beetween 1 to 100")
                             continue
                        else:
                            break
                    break
                except ValueError :
                     print ("invalid input pleae enter calid input")

            grade,result=calculate_grade(marks)
            student={"Name":name,"Roll":roll,"Marks":marks,"Grade":grade,"Result":result}
            students.append(student)
            again=input('"Press "ENTER" for new entry "n" for Exit"').lower()
            if again=="n":
                break
def student_list(students):
        print("-------------  Student list ---------------")
        for student in students :
             display_student(student)
        print("------------------------------------------")
def student_search(students):    
        search=int(input("Enter a Roll No to search a student record :- "))
       
        found=False

        for student in students :
            if student["Roll"]==search:
                display_student(student)
                
                found=True
        if found == False:
            print("Student not found !! ") 
def student_update(students):
        updating=int(input("Enter a number for updaating "))
        found=False
        for student in students :
            if updating==student["Roll"]:
                found=True
            
                search_str=str(updating)
                upd=input("Press 'ENTER' for updating Roll no " + search_str +"'s details, ('n') for exit").lower()
                if upd=="n":
                    return
                else:
                    newname=input("Enter new name :- ")


                    
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
                             
                        


                    





                    newmarks=int(input("Enter new marks"))
                   
            
                  
                student["Roll"]=newroll
                student["Name"]=newname
                student["Marks"]=newmarks
                upd_student=student
                       
                       
                    
                if found:
                    print("updated student is ",upd_student)
               
        if found!=True:
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
        print("Marks ",student["Marks"]) 
        print("Grade ",student["Grade"])
        print("Result ",student["Result"])
        print()
         
    

def calculate_grade(marks):
    result="pass"

    if marks>=90:
        grade="A"
    elif marks>=75:
         grade="B"
    elif marks>=50:
        grade="C"
    elif marks>=33:
        grade="D"
    else:
        grade="F"
        result="fail"
    

    return grade , result




while True:

    print("hello nafis khan ")
    print("===ENTER=====")
    print("1 for add students\n" \
    "2 for see student list\n3 for search student \n4 for update student\n5 for delete student \n6 for 'EXIT'"   )
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

