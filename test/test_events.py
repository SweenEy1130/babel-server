# test_events.py
import requests

base_url = 'http://192.168.1.88:80'
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
data = dict(description = 'Microsoft', capacity = '10', available = '4', price = '>1000', location = '2133 Norwood St')
url = base_url + "/create_event"
r = requests.post(url, data = data, cookies = login_cookies)
print r.text

# Test for editing events
data = dict(eid = 2, description = 'Google', capacity = '5', available = '4', price = '>500', location = '2133 Norwood St')
url = base_url + "/edit_event"
r = requests.post(url, data = data, cookies = login_cookies)
print r.text

# Test for deleting events
data = dict(eid = 4)
url = base_url + "/delete_event"
r = requests.post(url, data = data, cookies = login_cookies)
print r.text