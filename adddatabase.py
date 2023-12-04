import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("face-recognition-ef957-firebase-adminsdk-7192c-fcf3ede913.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-ef957-default-rtdb.firebaseio.com/",
})

ref = db.reference('Students')

data = {
    "191032":
        {
            "name": "Geoffrey hinton",
            "major": "Robotics",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "191910":
        {
            "name": "Andrew Ng",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "192012":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)