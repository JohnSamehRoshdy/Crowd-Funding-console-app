import userfunctions as uf
import dealwithdata as dl


usersdata = dl.readdata('users.json')

usersdata = usersdata['data']
# print (usersdata,type(usersdata)) this is for your test as a developer


    
cuserdata = uf.login(usersdata)
print('Welcome !!',cuserdata['fname'] , ' has logged in')
    
    
    
projectdata = dl.readdata('projects.json')
projectdata = projectdata['data']
# print(projectdata,type(projectdata))
projectlist = []
for project in projectdata:
    projectlist.append(project['title'])
    
uf.viewprojects(projectlist)

def addprojects():
    print('Enter the title of projects and when you finish Enter done')
    while True :
        projecttitle = input('Enter project title : ')
        if projecttitle in projectlist and projecttitle not in cuserdata['projects']:
            cuserdata['projects'].append(projecttitle)
        elif projecttitle in cuserdata['projects']:
            print(cuserdata['fname'],' is already in this project')
        elif projecttitle == 'done':
            break
        else:
            print('this project is not available')
            
addprojects()
# print(usersdata,type(usersdata))
usersdata = {"data":usersdata}
dl.updatedata('users.json',usersdata)




