import UserDataValidation as ch
import dealwithdata as dl
import MainScript as ms
import uuid
import getpass

################################################################################################################################################################
# This is a function to login to the account of a user
current_user_data = {}
def login():
    global current_user_data 
    usersdata = dl.readdata('users.json')
    usersdata = usersdata['data']
    while True:
        username = input('Please Enter your Email : ')
        password = getpass.getpass('Please Enter Your Password: ')
        authenticated = False  
        for user in usersdata:
            if username == user['email'] and password == user['password']:
                print (f'Welcome {user["fname"]}')
                authenticated = True
                current_user_data = user
                break
        if authenticated:
            break
        else:  
            print('Email or Password is Incorrect please try again!!')
    

    ms.after_login()
        
 
################################################################################################################################################################        

    
        
# This is a function to register a new user

def registeration():
    userdata = {"id":"","fname":"","lname":"","email":"","password":"","confirmpass":"","phone":"","projects":[]}
    userdata["id"] = str(uuid.uuid1())

    #Enter First name
    while True:
        fname = input('Please Enter Your First Name : ')
        result = ch.checkfname(fname)
        if result:
            # print(result)
            userdata["fname"] = fname
            break
        else:
            # print(result)
            print('Invalid Name')
            
            
    #Enter Last name    
    while True:
        lname = input('Please Enter Your Last Name : ')
        result = ch.checkfname(lname)
        if result:
            # print(result)
            userdata["lname"] = lname
            break
        else:
            # print(result)
            print('Invalid Name')
            
            
            

    #Enter  Email       
    while True:
        email = input('Please Enter Your Email : ')
        result = ch.checkmail(email)
        if result:
            # print(result)
            userdata["email"] = email
            break
        else:
            # print(result)
            print('Invalid Email')
            


    #Enter  Password
    while True:
        password = getpass.getpass('Please Enter Your Password: ')
        result = ch.checkpassword(password)
        if result:
            # print(result)
            userdata["password"] = password
            break
        else:
            # print(result)
            print('Invalid Password')
            
    #Confirm Password
    while True:
        confirm_password = getpass.getpass('Please Rewrite Your Password: ')
        result = ch.check_confirm_password(confirm_password,userdata["password"])
        if result:
            # print(result)
            userdata["confirmpass"] = confirm_password
            break
        else:
            # print(result)
            print('Invalid Password')
    
    
    
    #Enter Phon Number       
    while True:
        phone = input('Please Rewrite Your Phone Number : ')
        result = ch.checkphone(phone)
        if result:
            # print(result)
            userdata["phone"] = phone
            break
        else:
            # print(result)
            print('Invalid Phone Number')
        

    dl.savedata('users.json',userdata) 
    print('You have registered Sucessfully')
    ms.Choices()           

################################################################################################################################################################

# This is a function to view the projects that a user is involved in
                
def view_user_projects():
    global current_user_data
    if current_user_data['projects']:
        print(f""" {current_user_data['fname']} is involved in the projects  """)
        for project in current_user_data['projects']:
            print (project)
    else:
         print(f""" {current_user_data['fname']} is not involved in any of our projects""")

    ms.after_login()
################################################################################################################################################################

# This is a function to add project for some user 
     

# def Subscribe_to_projects():
#     global current_user_data
#     all_projects = dl.readdata('projects.json')
#     all_projects_data = all_projects['data']
#     projectlist = []
#     for project in all_projects_data:
#         projectlist.append(project['title'])     
#     print('Enter the title of projects you want to subscribe and when you finish Enter done')
#     while True :
#         projecttitle = input('Enter project title : ')
#         if projecttitle in projectlist and projecttitle not in current_user_data['projects']:
#             current_user_data['projects'].append(projecttitle)
#             print('project added successfully')
#         elif projecttitle in current_user_data['projects']:
#             print(current_user_data['fname'],' is already involved in this project')
#         elif projecttitle == 'done':
#             break
#         else:
#             print('this project is not available')

    

    
#     ms.after_login()

###################################################################################################################################
def Subscribe_to_projects():
    global current_user_data
    all_users_data = dl.readdata('users.json')
    all_users = all_users_data['data']

    # Find the index of the current user in the list of all users
    user_index = None
    for i, user in enumerate(all_users):
        if user['id'] == current_user_data['id']:
            user_index = i
            break

    
    all_projects = dl.readdata('projects.json')
    all_projects_data = all_projects['data']
    projectlist = [project['title'] for project in all_projects_data]

    print('Enter the title of projects you want to subscribe to. When you finish, enter "done".')

    while True:
        projecttitle = input('Enter project title: ')

        if projecttitle in projectlist and projecttitle not in current_user_data['projects']:
            current_user_data['projects'].append(projecttitle)
            print('Project added successfully.')
        elif projecttitle in current_user_data['projects']:
            print(f'{current_user_data["fname"]} is already involved in this project.')
        elif projecttitle == 'done':
            break
        else:
            print('This project is not available.')

    # Update the user's data in the list of all users
    all_users[user_index] = current_user_data

    # Save the updated list of users back to the JSON file
    all_users_data['data'] = all_users
    dl.updatedata('users.json', all_users_data)
    ms.after_login()


























































################################################################################################################################################################
# This function is used to logout from the user account
def logout():
    global current_user_data
    current_user_data = {}
    ms.Interface()