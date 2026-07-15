students = []
def add_student ():
          student_name = input("Enter Student Name:")
          student_email = input("Enter Student Email:" )
          student_age = int(input("Enter Student Age:"))
          print("successfully added student") 
          students_data (student_name, student_email, student_age ) 
          students.append(students_data) 
def display_student ():
          for std in students:
                    
              print("the student id is: ",std[0])
              print("the student name is: ",std[1])
              print("the student email is: ", std[2])
              print("the student age is: ", std[3])
              print(" display student ") 
def search_student ():
      

while(True):
      print("\n\n====THE STUDENT NAME IS====")
      print("1: Add Student ")
      print("2: display student ")
      print("3: search  Student ")
      print("4: update  Student ")
      print("5: delete  Student ")
      print("6: Exit")
      choice =int(input("Enter your choice:"))
      if choice == 1:
            add_student() 
          
      elif choice == 2:
          display_student ()
      elif choice == 3:
           search_student () 
      elif choice == 4:
       update_Studen() 
      elif choice == 5:
            delete_Student() 
      else:
           break
