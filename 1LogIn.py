import time


attempt = 3
password = ""
while password != 'secret':
    
    password = input('Enter Your Password: ')
    if password != 'secret':
        attempt -= 1
        print(attempt)
        if attempt == 0:
            time.sleep(5)
    
    if password == 'secret':
        print('Succesfull Login.....!')
    else:
        print('Access Denied')
