students=[]
while True:

    name=input("Enter Student Name     :- ")
    roll=input("Enter Student Roll No  :- ")
    marks=input("Enter Student Marks    :-")
    again=input('"Press "ENTER" for new entry "n" for Exit"')
    student={"Name":name,"Roll":roll,"Marks":marks}
    students.append(student)
    
    if again=="n":
        break

print(students)

