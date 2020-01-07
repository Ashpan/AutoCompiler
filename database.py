from firebase import firebase
from ocr import *
from number_rec import *
from boxes import *
import csv
import os


def postCSV(dir_path,csv_file):
    files = os.listdir(dir_path)
    for i in range(len(files)):
        number_data = {'Team Number':'', 'Match Number':'',
    'Autonomous Rocket Cargo Scored':'', 'Autonomous Rocket Cargo Missed':'',
        'Autonomous Rocket Hatch Scored':'', 'Autonomous Rocket Hatch Missed':'',
        'Autonomous Cargoship Cargo Scored':'', 'Autonomous Cargoship Missed':'',
        'Teleoperated Rocket Hatches Scored':'','Teleoperated Rocket Hatches Missed':'',
        'Teleoperated Rocket Cargo Scored':'','Teleoperated Rocket Cargo Missed':'',
        'Teleoperated Cargoship Hatches Scored':'','Teleoperated Cargoship Hatches Missed':'',
        'Teleoperated Cargoship Cargo Scored':'','Teleoperated Cargoship Cargo Missed':''}

        check_data = {'Climb 1':'','Climb 2':'','Climb 3':'','Defense Bad':'','Defense Meh':'',
        'Defense Good':'','Defense Clamps':'','Defense Line':'','Defense Cargo':'',
        'Defense Ping Pong':''}

        file_name = os.path.basename(files[i])
        data_label = os.path.splitext(files_name)[0]

        if data_label == None:
            print('File Name is None')

        if data_label in number_data:
            value = number_recognition(data_label)
            number_data[data_label] = value
        elif data_label in check_data:
            if field_empty(data_label) is True:
                value = 'TRUE'
            else:
                value = 'FALSE'

            check_data[data_label] = value

        else:
            print('Data Label not in CSV')

        os.path.remove(file_name)
        RESULTS = []
        for key in number_data.keys():
            RESULTS.append(number_data[key])

        for key in check_data.keys():
            RESULTS.append(check_data[key])

        with open(csv_file,'a') as file:
            writer = csv.writer(file)
            writer.writerow(RESULTS)


def pushToDatabase(csv_file, event):
    cred = 'https://scouting-test-ffa7d.firebaseio.com'
    database = firebase.FirebaseApplication(cred, None)

    try:
        database.get('/'+ event, None)
    except ConnectionError:
        print('Check Internet Connection')
    else:
        with open(csv_file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader)
            labels = next(reader)

            writer = csv.writer(csvFile)
            for row in reader:

                team_num = str(row[0])
                print(team_num)
                match_num = str(row[1])

                numbers = database.get('/'+ event, None)
                if numbers == None or team_num not in numbers:
                    database.post('/'+ event + '/' + str(team_num),None)

                matches = database.get('/'+ event + '/' + str(team_num),None)
                if matches == None or match_num not in matches:
                    link = '/' + event + '/'+ team_num
                    database.post(link + '/' + match_num,None)

                    for i in range(len(row)):
                        if i != 0 and i != 1:
                            link = '/' + event + '/'+ str(team_num) + '/' + str(match_num)
                            print(link + '/' + labels[i])
                            database.put("", link + '/' + labels[i], row[i])

                    print('Match' + match_num + ' successfully pushed...')



if __name__ == "__main__":
    pushToDatabase("/Users/bilalqadar/Documents/GitHub/FuckCompiling/offline_stemely.csv",'stemely')
