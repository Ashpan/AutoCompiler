from firebase import firebase
import sys
import os
import csv
import cv2

name = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))
sys.path.insert(0,name + "/recognition/")
#from recognition import number_rec


def postCSV(dir_path,csv_file,box_parameters):
    print("Saving offline backup of data...")
    w,h,line_weight = box_parameters
    files = os.listdir(path=dir_path)

    raw_data = {}
    check_data = {}

    for i in range(len(files)):

        file_name = os.path.basename(files[i])
        data_label = os.path.splitext(file_name)[0]
        image = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
        box_num = int(data_label[1])
        data_type = data_label[2]
        for i in range(box_num):
            #Do some stuff here


    # RESULTS = []
    # for key in number_data.keys():
    #     RESULTS.append(number_data[key])
    #
    # for key in check_data.keys():
    #     RESULTS.append(check_data[key])
    #
    # #print(RESULTS)
    #
    # with open(csv_file,'a') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(RESULTS)

def pushToDatabase(csv_file, event):
    cred = 'https://scouting-test-ffa7d.firebaseio.com'
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

if __name__ == "__main__":
    name = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))
    postCSV(name + "/processing/completed","csv_file",(175,135,5))
