# test_events.py
import requests

base_url = 'http://192.168.1.88:80'

def TestCaseForLogin(usrn):
    # Login part
    url = base_url + "/login?username=%s" % usrn
    r = requests.get(url)
    global login_cookies
    login_cookies = r.cookies
    print r.text

def TestCaseForEventDisplay(action_code):
    # Test for listing events
    data = dict(action = action_code)
    url = base_url + "/get_event_list"
    r = requests.post(url, data=data, cookies = login_cookies)
    print r.text

def TestCaseForEvents():
    # Test for creating events
    data = dict(title = 'Microsoft', description = 'Microsoft round trip', capacity = '10', available = '4', price = '>1000',
                    location = '2133 Norwood St', destination = 'UCLA', event_date = '11/30/1991 10:20:12')
    url = base_url + "/create_event"
    r = requests.post(url, data = data, cookies = login_cookies)
    print r.text

    # Test for editing events
    data = dict(eid = 2, title = 'Google', description = 'Mountain View', capacity = '15', available = '4', price = '>500',
                location = '2133 Norwood St', destination = 'UCLA', event_date = '11/30/1991 10:20:12')
    url = base_url + "/edit_event"
    r = requests.post(url, data = data, cookies = login_cookies)
    print r.text

    # Test for deleting events
    data = dict(eid = 3)
    url = base_url + "/delete_event"
    r = requests.post(url, data = data, cookies = login_cookies)
    print r.text

def TestCaseForEventApply(eid):
    # Test for apply event
    data = dict(eid = )
    url = base_url + "/apply_event"
    r = requests.post(url, data=data, cookies = login_cookies)
    print r.text

def TestCaseForCancelEventApply(eid):
    data = dict(eid = eid)
    url = base_url + "/cancel_apply_event"
    r = requests.post(url, data=data, cookies = login_cookies)
    print r.text

def TestCaseForApplicationApprove(eid, uid):
    data = dict(eid = eid, uid = uid)
    url = base_url + "/approve_apply"
    r = requests.post(url, data=data, cookies = login_cookies)
    print r.text

def TestCaseForCancelApplicationApprove(eid, uid):
    data = dict(eid = eid, uid = uid)
    url = base_url + "/cancel_approve_apply"
    r = requests.post(url, data=data, cookies = login_cookies)
    print r.text

if __name__ == '__main__':
    login_cookies = ''

    print "Test for Login"
    TestCaseForLogin('adams')
    # TestCaseForLogin('bob')
    # TestCaseForLogin('celia')
    # TestCaseForLogin('david')

    # print "Test for event application"
    # TestCaseForEventApply(2)
    # print "Test for canceling event application"
    # TestCaseForCancelEventApply(1, 4)

    # print "Test for application approve"
    # TestCaseForApplicationApprove(1, 4)
    print "Test for canceling application approve"
    TestCaseForCancelApplicationApprove(1, 4)

    # print "Test for EventDisplay"
    # TestCaseForEventDisplay(4)

