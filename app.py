'''
Projects:
• The user can create a project fund raise campaign which contains:
• Title
• Details
• Total target (i.e 250000 EGP)
• Set start/end time for the campaign (validate the date formula)

. create new project
• User can view all projects
• User can edit his own projects
• User can delete his own project

'''
import re
import Dealingjason as js


data = js.read_data('projects.json')
projects = data['data']

def project_main():
    while True:
        answer = input("""
    choose from 1 to 4
        1) create new project
        2) view all projects
        3) upadate project
        4) delete project
        5) exit
        ur choice : """)
        if answer == '1':
            createProject()
        elif answer == '2':
            viewAll()
        elif answer == '3':
            updateProject()
        elif answer == '4':
            deletProject()
        elif answer == '5':
            break
        else:
            print("Invalid input. Please choose a valid option (1-5).")


def createProject():
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    # ask about some inputs 
    Title = input('Project Title: ')
    details = input('Project details: ')
    totalTarget = input('Total target : ')
    while True:
        startDate = input('Enter the start date (YYYY-MM-DD):')
        endDate = input('Enter the end date (YYYY-MM-DD):')
        if bool(re.match(date_pattern,startDate)) and bool(re.match(date_pattern,startDate)):
            break
        else:
            print('Invalid DAte formula should be YYYY-MM-DD')
    date = startDate,endDate
    project = {'title':Title,'details':details,'totalTarget':totalTarget,'date':date}
    js.save_data_to_json('projects.json',project)
    return project


def viewAll():
    global projects
    # print data
    i = 1
    for project in projects:
        print(f'{i}) {project}')
        i+=1
# viewAll()

def updateProject():
    # if choose 1 will be index 0
    global projects
    viewAll()
    answer = input('choose project num: ')
    try:
        idx = int(answer) -1 
        # data updated throw the array 
        projects[idx] = createProject()
        # should open the file and add
        js.json_to_save('projects.json',data)
        print('data Updated')
    except Exception as e:
        print(e)

# updateProject()


def deletProject():
    # if choose 1 will be index 0
    global projects
    viewAll()
    answer = input('choose project num: ')
    try:
        idx = int(answer) -1 
        # data updated throw the array 
        projects.pop(idx)
        # should open the file and add
        js.json_to_save('projects.json',data)
        print('data Updated')
    except Exception as e:
        print(e)

# deletProject()
# print(bool(re.match(date_pattern,'1111-03-04')))

if __name__ == '__main__':
    project_main()
