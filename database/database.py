from firebase import firebase
import sys
import os
import csv
import cv2

sys.path.insert(0, '/sheet/')
sys.path.insert(0, '/recognition/')
sys.path.insert(0, '/database/')
from recognition import number_rec

def postCSV(dir_path,csv_file):
    files = os.listdir(path=dir_path)

    raw_data = {'team_num1':'','team_num2':'','team_num3':'','team_num4':'',
    'match1':'','match2':'','match3':'',
    'auto_cargoship_cargo_missed1':'','auto_cargoship_cargo_missed2':'',
    'auto_cargoship_cargo_scored1':'','auto_cargoship_cargo_scored2':'',
    'auto_cargoship_hatch_missed1':'','auto_cargoship_hatch_missed2':'',
    'auto_cargoship_hatch_scored1':'','auto_cargoship_hatch_scored2':'',
    'auto_rocket_cargo_missed1':'', 'auto_rocket_cargo_missed2':'',
    'auto_rocket_cargo_scored1':'', 'auto_rocket_cargo_scored2':'',
    'auto_rocket_hatch_missed1':'', 'auto_rocket_hatch_missed2':'',
    'auto_rocket_hatch_scored1':'', 'auto_rocket_hatch_scored2':'',
    'teleop_rocket_cargo_missed1':'','teleop_rocket_cargo_missed2':'',
    'teleop_rocket_cargo_scored1':'','teleop_rocket_cargo_scored2':'',
    'teleop_rocket_hatch_missed1':'','teleop_rocket_hatch_missed2':'',
    'teleop_rocket_hatch_scored1':'','teleop_rocket_hatch_scored2':'',
    'teleop_cargoship_cargo_missed1':'','teleop_cargoship_cargo_missed2':'',
    'teleop_cargoship_cargo_scored1':'','teleop_cargoship_cargo_scored2':'',
    'teleop_cargoship_hatch_missed1':'','teleop_cargoship_hatch_missed2':'',
    'teleop_cargoship_hatch_scored1':'','teleop_cargoship_hatch_scored2':''}

    check_data = {'climb_1':'','climb_2':'','climb_3':'','defense_bad':'','defense_meh':'',
    'defense_good':'','defense_line':'','defense_cargo':'',
    'defense_pingpong':''}

    for i in range(len(files)):

        file_name = os.path.basename(files[i])
        data_label = os.path.splitext(file_name)[0]
        #print(data_label)

        if data_label == None:
            print('File Name is None')

        if data_label in raw_data:
            label = './processing/completed/'+data_label+'.jpg'
            value = number_rec.number_recognition(label)
            raw_data[data_label] = value

        elif data_label in check_data:
            image_array = cv2.imread('./processing/completed/'+data_label+'.jpg', cv2.IMREAD_GRAYSCALE)
            if number_rec.field_empty(image_array,15000) is True:
                value = 'TRUE'
            else:
                value = 'FALSE'

            check_data[data_label] = value

        else:
            print('Saving comment...')

    number_data = {'team_number':int(raw_data['team_num1']+ raw_data['team_num2'] + raw_data['team_num3']+ raw_data['team_num4']),
    'match_number':int(raw_data['match1'] + raw_data['match2'] + raw_data['match3']),
    'auto_cargoship_cargo_missed':int(raw_data['auto_cargoship_cargo_missed1'] + raw_data['auto_cargoship_cargo_missed2']),
    'auto_cargoship_cargo_scored':int(raw_data['auto_cargoship_cargo_scored1']+ raw_data['auto_cargoship_cargo_scored2']),
    'auto_cargoship_hatch_missed':int(raw_data['auto_cargoship_hatch_missed1']+ raw_data['auto_cargoship_hatch_missed2']),
    'auto_cargoship_hatch_scored':int(raw_data['auto_cargoship_hatch_scored1']+ raw_data['auto_cargoship_hatch_scored2']),
    'auto_rocket_cargo_missed':int(raw_data['auto_rocket_cargo_missed1']+ raw_data['auto_rocket_cargo_missed2']),
    'auto_rocket_cargo_scored':int(raw_data['auto_rocket_cargo_scored1']+ raw_data['auto_rocket_cargo_scored2']),
    'auto_rocket_hatch_missed':int(raw_data['auto_rocket_hatch_missed1']+raw_data['auto_rocket_hatch_missed2']),
    'auto_rocket_hatch_scored':int(raw_data['auto_rocket_hatch_scored1']+raw_data['auto_rocket_hatch_scored2']),
    'teleop_rocket_cargo_missed':int(raw_data['teleop_rocket_cargo_missed1']+raw_data['teleop_rocket_cargo_missed2']),
    'teleop_rocket_cargo_scored':int(raw_data['teleop_rocket_cargo_scored1']+raw_data['teleop_rocket_cargo_scored2']),
    'teleop_rocket_hatch_missed':int(raw_data['teleop_rocket_hatch_missed1']+raw_data['teleop_rocket_hatch_missed2']),
    'teleop_rocket_hatch_scored':int(raw_data['teleop_rocket_hatch_scored1']+raw_data['teleop_rocket_hatch_scored2']),
    'teleop_cargoship_cargo_missed':int(raw_data['teleop_cargoship_cargo_missed1']+raw_data['teleop_cargoship_cargo_missed2']),
    'teleop_cargoship_cargo_scored':int(raw_data['teleop_cargoship_cargo_scored1']+raw_data['teleop_cargoship_cargo_scored2']),
    'teleop_cargoship_hatch_missed':int(raw_data['teleop_cargoship_hatch_missed1']+raw_data['teleop_cargoship_hatch_missed2']),
    'teleop_cargoship_hatch_scored1':int(raw_data['teleop_cargoship_hatch_scored1']+raw_data['teleop_cargoship_hatch_scored2'])}

    #print(number_data)
    #print(raw_data)
    #print(check_data)
    os.rename("./processing/completed/comments.jpg","./processing/comments/comment_"+str(number_data["team_number"]) + "_"+ str(number_data["match_number"]) +".jpg")

    RESULTS = []
    for key in number_data.keys():
        RESULTS.append(number_data[key])

    for key in check_data.keys():
        RESULTS.append(check_data[key])

    #print(RESULTS)

    with open(csv_file,'a') as file:
        writer = csv.writer(file)
        writer.writerow(RESULTS)

    print("Saving offline backup of data...")

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
            labels = next(reader)

            for row in reader:
                team_num = str(row[0])
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
                            #print(link + '/' + labels[i])
                            database.put("", link + '/' + labels[i], row[i])

                    print('Match' + match_num + ' successfully pushed...')
