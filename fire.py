import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-project-286-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules

ref = db.reference('Attendance Records')
date_today = (str(datetime.now())[0:10])
posts_ref = ref.child(date_today + '/')

# We can also chain the two calls together

# posts_ref.push().set({
#     'Student_Name': 'Palash',
#     'Time': 'time'
# })

# print(ref.get())
