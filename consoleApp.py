## 
import Dealingjason as js
# function for validation 
import re
import app 


egy_num_pattern = r'^01[0125][0-9]{8}$'
# email 
email_pattern = r'\w+@\w+\.\w+'

def main():
    answer = input('Do you have an acount Y/N ?')
    if answer.lower() == 'y':
        login()
        app.project_main()
    else:
        user_info= register()
        js.save_data_to_json('users.json',user_info)
        app.project_main()


def register():
    # fname
    fname = input('ur fname:')
    # lname
    lname = input('ur lname:')
    # email
    email = input('ur email:')
    # password
    password = input('ur password:')
    # confirm password
    while True:
        confirmPassword = input('confirm password:')
        if confirmPassword == password:
            break
        else:
            print('password doesnot match!!!')
    # mobile number validation
    while True:
        mobileNUm = input('ur mobile num:')
        if bool(re.match(egy_num_pattern,mobileNUm)):
            break
        else:
            print('Invalid phone number!!')
    user_info = {'fname':fname,'lname':lname,'email':email,'password':password,'mobile':mobileNUm}
    print('Welcome to our app')
    return  user_info

# login 
def login():
    # geting the array inside the object 
    data = js.read_data('users.json')
    # checking if is a email is exists
    email = input('ur email:')
    password = input('ur password: ')
    for user in data['data']:
        temp_info = {'email':email,'password':password}
        if temp_info['email'] == user['email'] and temp_info['password'] == user['password']:
            print('================')
            print('Welcome to our app')
            print('================')
            return
    print('Invalid mail or password')

# login()

main()

