import json
def readdata (filename):
    try:
        fileobject = open(filename,'r')
    except Exception as e :
        print('sorry',e)
    else:
        userdata = fileobject.read()
        userdata = json.loads(userdata)
        return userdata
    
    
# print(readdata('students.json'),type(readdata('students.json')))

def savedata (filename,ins_data):
    old_data = readdata(filename)
    old_data['data'].append(ins_data)
    try:
        fileobject = open(filename,'w')
    except Exception as e:
        print('sorry',e)
        return False
    else:
        str_data = json.dumps(old_data,indent=4)
        fileobject.write(str_data)
        fileobject.close()
        return True
    
    
def updatedata (filename,newdata):
    try:
        fileobject = open(filename,'w')
    except Exception as e:
        print('sorry',e)
        return False
    else:
        str_data = json.dumps(newdata,indent=4)
        fileobject.write(str_data)
        fileobject.close()
        return True




    




        
        
    