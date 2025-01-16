# BwTask
Brain Wise evaluation task

## Features TODO list:

1. ~~created required data models: User, Company, Department,~~ ...:fa-check-square: 
2. workflow :fa-gear:
3. Security & Permissions :fa-gear:
4. ~~APIs: created required rest APIs~~ :fa-check-square:
5. Testing & LOGGING :fa-gear:

## Project setup:
1. create and activate virtual environment

2. nstall requirements:
`$ pip3 install -r requirements.txt`

3. add SECRET_KEY TO environment vars, use this key instead of generating new one:
`django-insecure-q2ajqcu6^epsbwwii6wug2suz22*^qrjj^+!u$yq=m$#i3h9as`
&
`GOOGLE_API_KEY = 'AIzaSyD--your-google-maps-key-SjQBE'`

4. make and run migrations:
`python3 manage.py makemigrations`
`python3 manage.py migrate`

5. run the server locally:
`python3 manage.py runserver`
