import UserDataValidation as ch
import dealwithdata as dl
import uuid
def registeration():
    userdata = {"id":"","fname":"","lname":"","email":"","password":"","confirmpass":"","phone":"","projects":[]}
    userdata["id"] = str(uuid.uuid1())

    #Enter First name
    while True:
        fname = input('Please Enter Your First Name : ')
        result = ch.checkfname(fname)
        if result:
            print(result)
            userdata["fname"] = fname
            break
        else:
            print(result)
            print('Invalid Name')
            
            
    #Enter Last name    
    while True:
        lname = input('Please Enter Your Last Name : ')
        result = ch.checkfname(lname)
        if result:
            print(result)
            userdata["lname"] = lname
            break
        else:
            print(result)
            print('Invalid Name')
            
            
            

    #Enter  Email       
    while True:
        email = input('Please Enter Your Email : ')
        result = ch.checkmail(email)
        if result:
            print(result)
            userdata["email"] = email
            break
        else:
            print(result)
            print('Invalid Email')
            


    #Enter  Password
    while True:
        password = input('Please Enter Your Password : ')
        result = ch.checkpassword(password)
        if result:
            print(result)
            userdata["password"] = password
            break
        else:
            print(result)
            print('Invalid Password')
            
    #Confirm Password
    while True:
        confirm_password = input('Please Rewrite Your Password : ')
        result = ch.check_confirm_password(confirm_password,userdata["password"])
        if result:
            print(result)
            userdata["confirmpass"] = confirm_password
            break
        else:
            print(result)
            print('Invalid Password')
    
    
    
    #Enter Phon Number       
    while True:
        phone = input('Please Rewrite Your Phone Number : ')
        result = ch.checkphone(phone)
        if result:
            print(result)
            userdata["phone"] = phone
            break
        else:
            print(result)
            print('Wrong Entry')
        

    dl.savedata('users.json',userdata)



        

        

