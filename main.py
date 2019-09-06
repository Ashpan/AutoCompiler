from number_rec import *
from boxes import *
import os

def compile_sheet(sheet_name):
    folder = "/Users/bilalqadar/Documents/GitHub/FuckCompiling/Cropped"
    box_extraction(sheet_name,"./Cropped/")
    files = os.listdir(folder)
    correct = 0
    total = len(files)
    for image in files:
        file_name = os.path.join(folder,image)
        prediction = number_recognition(file_name)

        if image == "1.png":
            print("Right Hatches Scored in Autonomous: " + str(prediction))
        elif image == "2.png":
            print("Center Hatches Scored in Autonomous: " + str(prediction))
        elif image == "3.png":
            print("Left Hatches Scored in Autonomous: " + str(prediction))
        elif image == "4.png":
            print("Center Hatches Missed in Autonomous: " + str(prediction))
        elif image == "5.png":
            print("Left Hatches Missed in Autonomous: " + str(prediction))
        elif image == "6.png":
            print("Right Hatches Missed in Autonomous: " + str(prediction))
        elif image == "7.png":
            print("Left Cargo's Scored in Autonomous: " + str(prediction))
        elif image == "8.png":
            print("Right Cargo's Scored in Autonomous: " + str(prediction))
        elif image == "9.png":
            print("Center Cargo's Scored in Autonomous: " + str(prediction))
        elif image == "10.png":
            print("Left Cargo's Missed in Autonomous: " + str(prediction))
        elif image == "11.png":
            print("Center Cargo's Missed in Autonomous: " + str(prediction))
        elif image == "12.png":
            print("Right Cargo's Missed in Autonomous: " + str(prediction))
        elif image == "13.png":
            print("Hatches Scored in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "14.png":
            print("Hatches Missed in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "15.png":
            print("Cargo Missed in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "16.png":
            print("Cargo Scored in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "17.png":
            print("Low Hatches Scored on Rocket during Teleoperated: " + str(prediction))
        elif image == "18.png":
            print("Middle Hatches Scored on Rocket during Teleoperated: " + str(prediction))
        elif image == "19.png":
            print("High Hatches Scored on Rocket during Teleoperated: " + str(prediction))
        elif image == "20.png":
            print("Low Cargo Scored on Rocket during Teleoperated: " + str(prediction))
        os.remove(file_name)




if __name__ == "__main__":
    sheet = compile_sheet("sheet.jpg")
