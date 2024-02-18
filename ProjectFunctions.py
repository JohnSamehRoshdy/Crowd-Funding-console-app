import ProjectDataValidation as pch
import dealwithdata as dl
import MainScript as ms
import uuid




def newproject():
    project_data = {"id":"","title":"","details":"","totaltarget":"","start":"","end":""}

    project_data["id"] = str(uuid.uuid1())


    #Enter title of the project
    while True:
        title = input('Please Enter Project Title : ')
        result = pch.checktitle(title)
        if result:
            # print(result)
            project_data["title"] = title
            break
        else:
            # print(result)
            print('Invalid Title')
            
            
            
            
            
            
    #Enter details of the project
    while True:
        details = input('Please Enter Project details : ')
        result = pch.checktitle(details)
        if result:
            # print(result)
            project_data["details"] = details
            break
        else:
            # print(result)
            print('Invalid Entry')
            
            
            
            
            
    #Enter Total Target of the project
    while True:
        target = input('Please Enter Total Target of the Project : ')
        result = pch.checktarget(target)
        if result:
            # print(result)
            project_data["totaltarget"] = target
            break
        else:
            # print(result)
            print('Invalid Number')
            
            
            
            
            
    #Enter start date and end date of the project         
    while True:
        start_date = input('Please Enter the start Date of the project (dd-mm-yyyy): ')
        end_date = input('Please Enter the end Date of the project (dd-mm-yyyy): ')

        if pch.check_dates(start_date, end_date):
            project_data["start"] = start_date
            project_data["end"] = end_date
            break
        else:
            print('Please enter valid dates. also check if the start date is after the end date')
            
            
    dl.savedata('projects.json',project_data)
    print(f'''Your new project {project_data["title"]} is added successfully''')
    ms.Choices()      
        
        
def ViewAllProjects():
    projectdata = dl.readdata('projects.json')
    projectdata = projectdata['data']
    for project in projectdata:
        print(project['title'])
    print("""==================================================================================================================================""")
    ms.Choices()



def view_all_projects_after_login():
    projectdata = dl.readdata('projects.json')
    projectdata = projectdata['data']
    for project in projectdata:
        print(project['title'])
    print("""==================================================================================================================================""")
    ms.after_login()



def ViewProjectDetails():
    while True:
        project_title = input('Please Enter project title : ')
        projectdata = dl.readdata('projects.json')
        projectdata = projectdata['data']
        for project in projectdata:
            if project_title == project['title']:
                print(f"""

                        Project Title : {project['title']}
                        Project Details : {project['details']}
                        Project Total Target : {project['totaltarget']}
                        Project starts on {project['start']} and ends on {project['end']} 
                    """)
                break
        else:
            print('There is no project with this title !!! ')
            continue
        break

    print("""==================================================================================================================================""")    
    ms.Choices()
