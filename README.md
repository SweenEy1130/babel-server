Babel
================
A social carpool application server based on Python flask framework for the backend.

### Environment:
- Python 2.7
- Flask 0.10.1


### API Documentation
#### Login

`GET /login?username=adams&password=123`

#### Logout

`GET /logout`

-------------------------

#### Create User

`GET	/create_user	@parameter [username:zhangsan, password:123]`

#### Delete User

`GET	/delete_user	@parameter [username:adams]`

#### Edit User

`GET	/edit_user		@parameter [status: String, description: String]`

#### View User

`GET	/view_user		@parameter [username:String]`

---------------

#### Get Event lists

`POST    /get_event_list`

###### @parameter:
- action: Int
	- 1 for owned events
	- 2 for applied events
    - 3 for participated events
    - 4 for all events relating to me


###### @response:
- result: model.Event JSON

#### Create Event

`POST    /create_event`

###### @parameter:
- description: String
- capacity: Int
- available: Int
- price: String
- location: String


###### @response:
- status:
    - 0  for success
    - -1 for error

#### Edit event

`POST    /edit_event`
###### @parameter:
- eid: Int
- description: String
- capacity: Int
- available: Int
- price: String
- location: String


###### @response:
- status:
    - 0  for success
    - 1 for error

#### Delete Event

`POST    /delete_event`
###### @parameter:
- eid: Int


###### @response:
- status:
    - 0  for success
    - -1 for error

#### Apply event

`POST    /apply_event`
###### @parameter:
- eid: Int


###### @response:
- status:
    - 0 for success
    - -1 for
    - -2 for duplicated application

#### Cancel Application

`POST    /cancel_apply_event`
###### @parameter:
- eid: Int


###### @response:
- status:
    - 0 for success
    - -1 for SQL Error

#### Approve application

`POST    /approve_apply`
###### @parameter:
- eid: Int
- uid: Int


###### @response:
- status:
    - 0 for success
    - -1 for already approved
    - -2 for not authorized
    - -3 for not an applicants
    - -4 for user doesn't exists
    - -5 for SQL error

#### Cancel application approvement

`POST    /cancel_approve_apply`
###### @parameter:
- eid: Int
- uid: Int


###### @response:
- status:
    - 0 for success
    - -1 for already approved
    - -2 for not authorized
    - -3 for not an applicants
    - -4 for user doesn't exists
    - -5 for SQL error
