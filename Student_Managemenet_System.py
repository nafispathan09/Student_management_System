while True:
    print("hello nafis khan ")
    print("===ENTER=====")
    call=int(input("1 for add students\n" \
    "2 for see student list\n3 for search student \n4 for update student\n5 for deleate student \n6 for 'EXIT'"   ))
    


    def add_student():
        students=[]
        while True:

            name=input("Enter Student Name     :- ")
            roll=int(input("Enter Student Roll No  :- "))
            marks=int(input("Enter Student Marks    :-"))
            again=input('"Press "ENTER" for new entry "n" for Exit"')
            student={"Name":name,"Roll":roll,"Marks":marks}
            students.append(student)

            if again=="n":
                break
        return students
    def student_list(students):
        print("-------------  Student list ---------------")
        for student in students:
            print("Name",student["Name"])
            print("Roll No.",student["Roll"])
            print("Marks ",student["Marks"])
    def student_search():    
        search=int(input("Enter a Roll No to search a student record :- "))
        search_str=str(search)
        found="a"

        for student in students :
            if student["Roll"]==search:
                print("Student Name :-",student["Name"])
                print("Student ROll :-",student["Roll"])
                print("Student Marks :-",student["Marks"])
                found="b"
        if found =="a":
            print("Student not found !! ")
        print("end")
        return search
    def student_update():
        search_str=str(search)
        upd=input("Press 'ENTER' for updating Roll no " + search_str +"'s details, ('n') for exit")
        if upd!="n":
            newname=input("Enter new name :- ")
            newroll=int(input("Enter new roll no :- "))
            newmarks=int(input("Enter new marks"))
        for student in students :
            if student["Roll"]==search:
                student["Roll"]=newroll
                student["Name"]=newname
                student["Marks"]=newmarks
                upd_student=student
                a=10

                break
        print("updated student is ",upd_student)
        print ("end",a)
    def deleate_student():
        dele=input("Press 'ENTER' for deleate a student from record ('n') for exit :- ")
        found=False
        if dele !="n":
            delnum=int(input("Enter student number for deleate :- "))
            for student in students:
                if student["Roll"]==delnum:
                    students.remove(student)
                    print(" Student ",delnum," deleted successfully !!!")
                    found=True
                    break
        if found==False:
            print("Student not found !!!")

    
    if call==6:
           break
    elif call==1:
        print("welcome to add student function ")
        add_student()
    elif call==2:
        print("welcome to see student ")
        student_list()
    elif call==3:
        print("welcome to search student ")
        student_search()
    elif call==4:
        print("welcome to update ")
        student_update()
    elif call==5:
          print("welcome to delete student ")
          deleate_student()
          
    else:
        print("Please enter valid input !!! ")

