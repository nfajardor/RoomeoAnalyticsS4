import firebase_admin
import matplotlib.pyplot as plt
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Use a service account
cred = credentials.Certificate('roomeo-6acbb-3dff41e45b38.json')

firebase_admin.initialize_app(cred)

db = firestore.client()

def option2():
    print("You have selected option 2")

def option3():
    print("You have selected option 3")

def option4():
    name = []
    currentCap = []
    occupation = []
    maxOc = 0
    maxBuild = ""
    docs = db.collection('Buildings').get()
    for doc in docs:
        number = 0
        d = doc.to_dict()
        name.append(d['Name'])
        for classrooms in d['classrooms']:
            n = classrooms['currentCap']
            number = number + n
        percent = (number / d['Capacity']) * 100
        occupation.append(percent)
        if percent > maxOc:
            maxOc = percent
            maxBuild = d['Name']

    plt.bar(name, occupation)
    plt.title('Percentage of occupation by building')
    plt.xlabel('Building')
    plt.ylabel('% occupation')
    plt.show()
    print("The building with the highest occupation rate is " + maxBuild + " with " + str(maxOc) +"%")

def option5():
    docs = db.collection('Analytics').get()
    for doc in docs:
        if (doc.id == 'averageHW'):
            d = doc.to_dict()
            print("The average time between hand washing reports is " + str(d['average']) + " for " + str(d['ammount']) + " reports")
def option6():
    docs = db.collection('Analytics').get()
    for doc in docs:
        if doc.id == 'visitInfo':
            d = doc.to_dict()
            print("A total of " + str(d['ammountUsers']) + " users have used the self care feature")
def option7():
    docs = db.collection('Analytics').get()
    for doc in docs:
        if doc.id == 'QRUses':
            d = doc.to_dict()
            print("The QR scanning function has been used a total of " + str(d['uses']) + " times")
def option8():
    docs = db.collection('Analytics').get()
    for doc in docs:
        print('a')
def option9():
    print("You have selected option 9")

running = True
while running:
    print("Please select the action that you want to do:\n1. Exit\n2. What are the occupancy rates of certain rooms/buildings?\n3. On average which classrooms are the most requiested?\n4. Which building has the highest occupancy rate?\n5. What is the average time between hand washing reports by students?\n6. How many users have used the self-care feature?\n7. How many times has the QR scanning functionality been used?\n8. How many reservations has the user cancelled?\n9. How frequently is the self-care feature used by the users?")
    s = int(input())

    if s == 1:
        print("You have selected option 1")
        running = False
        print("---------------------------------------------")
    if s == 2:
        print("You have selected option 2")
        print("---------------------------------------------")
        option2()
        print("---------------------------------------------")
    if s == 3:
        print("You have selected option 3")
        print("---------------------------------------------")
        option3()
        print("---------------------------------------------")
    if s == 4:
        print("You have selected option 4")
        print("---------------------------------------------")
        option4()
        print("---------------------------------------------")
    if s == 5:
        print("You have selected option 5")
        print("---------------------------------------------")
        option5()
        print("---------------------------------------------")
    if s == 6:
        print("You have selected option 6")
        print("---------------------------------------------")
        option6()
        print("---------------------------------------------")
    if s == 7:
        print("You have selected option 7")
        print("---------------------------------------------")
        option7()
        print("---------------------------------------------")
    if s == 8:
        print("You have selected option 8")
        print("---------------------------------------------")
        option8()
        print("---------------------------------------------")
    if s == 9:
        print("You have selected option 9")
        print("---------------------------------------------")
        option9()
        print("---------------------------------------------")




