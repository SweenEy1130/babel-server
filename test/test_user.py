# test_events.py
import requests

base_url = 'http://192.168.1.88:80'

def TestCaseForLogin(usrn, psw=''):
    data = dict(username = usrn, password = psw)
    url = base_url + "/login"
    r = requests.post(url, data = data)
    global login_cookies
    login_cookies = r.cookies
    print r.text

def TestCaseForEditUser(status, description):
    # Test for apply event
    data = dict(status = status, description = description)
    url = base_url + "/edit_user"
    r = requests.post(url, data=data, cookies = login_cookies)
    print r.text

if __name__ == '__main__':
    login_cookies = ''

    print "Test for Login"
    TestCaseForLogin('bob')

    # print "Test for editing user profile"
    # TestCaseForEditUser('status', 'description')
