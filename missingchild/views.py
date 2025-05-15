import datetime

from missingchild.models import MissingPersonModel,RecordModel,UserModel
from missingchild.forms import MissingPersons,LoginForm,UserForm
from django.shortcuts import render
from django.utils import timezone

import cv2
import numpy as np
import face_recognition
import os

from missingchild.service import getmissingpersons


def userregistration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = UserForm(request.POST)

        if registrationForm.is_valid():

            regModel = UserModel()

            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.gender = registrationForm.cleaned_data["gender"]
            regModel.age = registrationForm.cleaned_data["age"]

            user = UserModel.objects.filter(username=regModel.username).first()
            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'index.html', locals())
    else:
        response = render(request, 'registration.html', {"message": "User All Ready Exist"})

    return response

def addmissingchild(request):

    if request.method == "POST":

        missingchildForm = MissingPersons(request.POST,request.FILES)

        if missingchildForm.is_valid():

            missingModel = MissingPersonModel()
            missingModel.name = missingchildForm.cleaned_data["name"]
            missingModel.age = missingchildForm.cleaned_data["age"]
            missingModel.gender = missingchildForm.cleaned_data["gender"]
            missingModel.skincolor = missingchildForm.cleaned_data["skincolor"]
            missingModel.height = missingchildForm.cleaned_data["height"]
            missingModel.languages = missingchildForm.cleaned_data["languages"]
            missingModel.languages = missingchildForm.cleaned_data["languages"]
            missingModel.image = missingchildForm.cleaned_data["image"]
            missingModel.isdisabled = missingchildForm.cleaned_data["isdisabled"]
            missingModel.ishavingmadness = missingchildForm.cleaned_data["ishavingmadness"]
            missingModel.nationality = missingchildForm.cleaned_data["nationality"]
            missingModel.state = missingchildForm.cleaned_data["state"]

            missingModel.education = missingchildForm.cleaned_data["education"]
            missingModel.dateofmissing = missingchildForm.cleaned_data["dateofmissing"]
            missingModel.locationofmissing = missingchildForm.cleaned_data["locationofmissing"]
            missingModel.locationofmoles = missingchildForm.cleaned_data["locationofmoles"]
            missingModel.userid=request.session['username']

            missingModel.save()

            return render(request, "missingpersons.html", {"persons": getmissingpersons(request.session['username'])})

        else:
            return render(request, 'addmissingperson.html', {"message": "Please Fill Form Data"})
    else:
        return render(request, 'addmissingperson.html', {"message": "Invalid Request"})

def login(request):

    if request.method == "GET":

        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]

            print(uname,upass)

            if uname == "admin" and upass == "admin":

                request.session['username'] = "admin"
                request.session['role'] = "admin"

                return render(request, "missingpersons.html", {"persons": getmissingpersons(request.session['username'])})

            else:

                user = UserModel.objects.filter(username=uname, password=upass).first()

                if user is not None:

                    request.session['username'] = uname
                    request.session['role'] = "user"

                    return render(request, "missingpersons.html",
                                  {"persons": getmissingpersons(request.session['username'])})

                else:
                    return render(request, 'index.html', {"message": "Invalid Credentials"})
        else:
            return render(request, 'index.html', {"message": "Please Enter Username and Password"})
    else:
        return render(request, 'index.html', {"message": "Invalid Request"})

def viewmissingperson(request):

    return render(request, "missingpersons.html", {"persons": getmissingpersons(request.session['username'])})

def viewuserprofile(request):

    persons = []
    for person in MissingPersonModel.objects.filter(name=request.GET['username']):
        person.image = str(person.image).split("/")[1]
        persons.append(person)

    return render(request, "missingpersons.html", {"persons":persons})

def deletemissingperson(request):

    personid=request.GET['personid']
    MissingPersonModel.objects.get(id=personid).delete()

    return render(request, "missingpersons.html", {"persons": getmissingpersons(request.session['username'])})

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})

#==============================================================================

def viewrecordedpersons(request):
    return render(request, "viewrecordedpersons.html", {"recordedpersons":RecordModel.objects.all()})

def findMissingPerson(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = BASE_DIR+"\\images"
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    print("images:",images, "type:",type(images))
    print("Classes:",classNames,"type:",type(classNames))
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    UNKNOWN_THRESHOLD = 0.55

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            bestMatchDistance = faceDis[matchIndex]  # Smallest distance
            probability = 1 - bestMatchDistance  # Higher means better match
            print(matches, matchIndex, f"Probability: {probability:.2f}")

            print(probability,UNKNOWN_THRESHOLD)
            if probability > UNKNOWN_THRESHOLD:  # Confident match
                name = classNames[matchIndex].upper()
            else:
                name = "UNKNOWN"

            # Draw rectangle and label
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            color = (0, 255, 0) if name != "UNKNOWN" else (0, 0, 255)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
            cv2.putText(img, f"{name} ({probability:.2f})", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            if name != "UNKNOWN":
                isRecorded = RecordModel.objects.filter(name=name.lower()).count()
                if isRecorded == 1:
                    RecordModel.objects.filter(name=name.lower()).update(recordeddate=timezone.now())
                else:
                    RecordModel(name=name.lower(), recordeddate=datetime.datetime.now()).save()

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)