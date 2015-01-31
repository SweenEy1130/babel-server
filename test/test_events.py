# test_events.py
import requests

base_url = 'http://127.0.0.1:80'
# Login part
url = base_url + "/login?username=adams"
r = requests.get(url)
login_cookies = r.cookies

# Test for listing events
data = dict(action = '1')
url = base_url + "/get_event_list"
r = requests.post(url, data=data, cookies = login_cookies)
print r.text

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