import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendance-79194-default-rtdb.firebaseio.com/",
    'storageBucket':"faceattendance-79194.appspot.com"
})

ref = db.reference('Students')

data = {
    "123457":
        {
            "Name": "Venus Solanki",
            "Class": "BE-1",
            "Starting_year":2021,
            "Total Attendance":6,
            "Standing": "G",
            "Years": 4,
            "Last attendance time": "2024-04-25 00:54:34"
        },
    "234567":
        {
            "Name": "Smit Sardhara",
            "Class": "BE-2",
            "Starting_year":2021,
            "Total Attendance":19,
            "Standing": "G",
            "Years": 4,
            "Last attendance time": "2024-04-25 00:34:34"
        },

}

# Corrected typo from itmes() to items()
for key,value in data.items():
    ref.child(key).set(value)
