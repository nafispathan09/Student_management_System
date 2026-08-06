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

print("-------------  Student list ---------------")

#for student in students:
#    print("Name",student["Name"])
#    print("Roll No.",student["Roll"])
#    print("Marks ",student["Marks"])

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
upd=input("Press 'ENTER' for updating Roll no " +search_str +"'s details, ('n') for exit")
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



    
    