from firebase import firebase
from ocr import *
from number_rec import *
from boxes import *
import csv


def postCSV(file_name):
    #Fix WiFi Error
    pass

def pushToData(csv_file, event):
    cred = 'https://scouting-test-ffa7d.firebaseio.com'
    database = firebase.FirebaseApplication(cred, None)
    try:
        database.get('/'+ event, None)
    except ConnectionError:
        print('Not Connected to Internet...')
    else:
        with open(csv_file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader)
            next(reader)

            writer = csv.writer(csvFile)
            for row in reader:

                labels = ['team_num', 'match_num', 'ar_cargo_scored', 'ar_cargo_missed',
                'ar_hatch_scored', 'ar_hatch_missed', 'ac_cargo_scored', 'ac_cargo_missed',
                'tr_hatch_scored', 'tr_hatch_missed', 'tr_cargo_scored', 'tr_cargo_missed',
                'tc_hatch_scored', 'tc_hatch_missed', 'tc_cargo_scored', 'tc_cargo_missed',
                'climb1', 'climb2', 'climb3', 'defense_bad', 'defense_meh', 'defense_good',
                'defense_clamps', 'defense_line', 'defense_cargo', 'defense_ping_pong']

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
    pushToData("/Users/bilalqadar/Documents/GitHub/FuckCompiling/offline_stemely.csv",'stemely')
