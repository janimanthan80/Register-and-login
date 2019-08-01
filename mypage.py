            # how to register and login


                      #registration
print("\t\t\t\t\t\t\\\\\\\\Welcome To My Registration Page\\\\\\\\")

class myreg():
  name = input("Enter Your Name : ")

  email1 = input("\nEnter Your Email : ")
  password1 = input("\nEnter Your Password : ")

  msg = print("\nWelcome To MyPage " + name.upper() + "\n\nYou Have Successfully Registered.")

 
                      #login

  print("\nLogin")

  while True:
    email2 = input("\nEnter your Email : ")
    password2 = input("\nEnter Your Password : ")
    if email1 == email2 and password1 == password2:
      print("\nLogin Successful\n\nWelcome To Our Page")
      break
    else:
      print("\nYou Have Entered Wrong Email Or Password Please Try Again") 

myreg()
     



