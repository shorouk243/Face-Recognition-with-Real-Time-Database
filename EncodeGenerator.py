from firebase_admin import credentials
from google.cloud import storage
from firebase_admin import db
import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime

cred = credentials.Certificate("/face r/face-recognition-ef957-firebase-adminsdk-7192c-fcf3ede913.json")
firebase_admin.initialize_app(cred ,{
     "databaseURL":"https://face-recognition-ef957-default-rtdb.firebaseio.com/" ,
     "storageBucket": "face-recognition-ef957.appspot.com"

})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)


fileName = f'{folderPath}/{path}'
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)


#we want to encode every single image
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # first step is changing the color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGR open-cv TO RGB face-recognition
        # second step is find the encoding
        encode = face_recognition.face_encodings(img)[0]
        # put it in the list
        encodeList.append(encode)

    return encodeList

encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print(encodeListKnown)

# file to put the encoding data into it
file = open("EncodeFile.p", 'wb')
# process of converting a Python object into a byte stream to
#store it in a file/database
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
