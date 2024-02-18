import re
from dateutil import parser



# title validation
def checktitle (title):
    if title.isdigit():
        return(False) 
    else:
        return (True)
    
# target validation
def checktarget (target):
    if target.isdigit():
        return(True) 
    else:
        return (False)
    
    
    
    
    
#date validation:
def check_dates(start_date, end_date):
    format = "%d-%m-%Y"
    
    try:
        start = parser.parse(start_date, dayfirst=True)
        end = parser.parse(end_date, dayfirst=True)
        return end > start
    except:
        return False
    

    
        
        

    
    
    
    

        
