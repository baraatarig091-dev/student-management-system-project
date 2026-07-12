student_name = ""
student_email = ""
student_age = 0
student_id = 0
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
          student_id = int(input("Enter Student ID:"))
          student_name = input("Enter Student Name:")
          student_email = input("Enter Student Email:" )
          student_age = int(input("Enter Student Age:"))
          print("successfully added student")
      elif choice == 2:
          print("the student id is: ", student_id)
          print("the student name is: ", student_name)
          print("the student email is: ", student_email)
          print("the student age is: ", student_age)
          print(" display student ")
      elif choice == 3:
           print(" search  Student ")
      elif choice == 4:
           print(" update  Student ")
      elif choice == 5:
           print(" delete  Student ")
      else:
           break