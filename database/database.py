from firebase import firebase
import sys
import os
import csv
import cv2

name = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))
sys.path.insert(0,name + "/recognition/")
#from recognition import number_rec


def postCSV(data, csv_file):
    print("Saving offline backup of data...")

    number_data,check_data = data
    RESULTS = []

    for key in number_data.keys():
        RESULTS.append(number_data[key])

    for key in check_data.keys():
        RESULTS.append(check_data[key])

    with open(csv_file,'a') as file:
        writer = csv.writer(file)
        writer.writerow(RESULTS)

def pushToDatabase(event,id,csv_file,cred):
    database = firebase.FirebaseApplication(cred, None)

    try:
        database.get('/'+ event, None)
    except ConnectionError:
        print('Check Internet Connection')
    else:
        print("Pushing to Database...")
        with open(csv_file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            labels = next(reader)

            for row in reader:
                id = str(row[0])
                match_num = str(row[1])
                numbers = database.get('/'+ event, None)

                if numbers == None or id not in numbers:
                    database.post('/'+ event + '/' + str(id),None)

                    for i in range(len(row)):
                        if i != 0 and i != 1:
                            link = '/' + event + '/'+ str(id)
                            database.put("", link + '/' + labels[i], row[i])

                    print('Survey ' + id + ' successfully pushed...')

if __name__ == "__main__":
    name = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))
    postCSV(name + "/processing/completed","csv_file",(175,135,5))
