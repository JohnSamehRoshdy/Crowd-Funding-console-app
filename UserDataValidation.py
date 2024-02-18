import re




# first name validation
def checkfname (name):
    if name.isdigit():
        return(False) 
    else:
        return (True)

        
#mail validation:

def checkmail(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    valid_email = re.fullmatch(pattern,email)
    if valid_email:
        return(True)
    else:
        return(False)



#Password validation:

def checkpassword(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    valid_password = re.fullmatch(pattern,password)
    if valid_password:
        return(True)
    else:
        return(False)
        

#confirm Password validation:

def check_confirm_password(confirmpassword,password):
    if confirmpassword == password:
        return(True)
    else:
        return(False)

    
    
#Egyptian Phone Number validation:
def checkphone(number):
    pattern = "^((010)\d{8}|(011)\d{8}|(012)\d{8})$"
    valid_number = re.fullmatch(pattern,number)
    if valid_number:
        return(True)
    else:
        return(False)
        
