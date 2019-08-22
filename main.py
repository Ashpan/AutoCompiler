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
            if prediction[0] == str(6):
                print("correct")
                correct += 1
            else:
                print("Incorrect")
            print("Right Hatches Scored in Autonomous: " + str(prediction))
        elif image == "2.png":
            if prediction[0]  == str(3):
                print("correct")
                correct += 1
            else:
                print("Incorrect")
            print("Center Hatches Scored in Autonomous: " + str(prediction))

        elif image == "3.png":
            if prediction[0] == str(4):
                print("correct")
                correct += 1
            else:
                print("Incorrect")
            print("Left Hatches Scored in Autonomous: " + str(prediction))
        elif image == "4.png":
            if prediction[0]  == str(0):
                print("correct")
                correct += 1
            else:
                print("Incorrect")
            print("Center Hatches Missed in Autonomous: " + str(prediction))
        elif image == "5.png":
            if prediction[0]  == str(1):
                print("correct")
                correct += 1
            else:
                print("Incorrect")
            print("Left Hatches Missed in Autonomous: " + str(prediction))
        elif image == "6.png":
            if prediction[0]  == str(0):
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Right Hatches Missed in Autonomous: " + str(prediction))
        elif image == "7.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Left Cargo's Scored in Autonomous: " + str(prediction))
        elif image == "8.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Right Cargo's Scored in Autonomous: " + str(prediction))
        elif image == "9.png":
            if prediction[0]  == str(4):
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Center Cargo's Scored in Autonomous: " + str(prediction))
        elif image == "10.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Left Cargo's Missed in Autonomous: " + str(prediction))
        elif image == "11.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Center Cargo's Missed in Autonomous: " + str(prediction))
        elif image == "12.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Right Cargo's Missed in Autonomous: " + str(prediction))
        elif image == "13.png":
            if prediction[0]  == str(1):
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Hatches Scored in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "14.png":
            if prediction[0]  == str(0):
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Hatches Missed in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "15.png":
            if prediction[0]  == str(4):
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Cargo Missed in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "16.png":
            if prediction[0]  == str(3):
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Cargo Scored in Cargo Bay during Teleoperated: " + str(prediction))
        elif image == "17.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Low Hatches Scored on Rocket during Teleoperated: " + str(prediction))
        elif image == "18.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Middle Hatches Scored on Rocket during Teleoperated: " + str(prediction))
        elif image == "19.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("High Hatches Scored on Rocket during Teleoperated: " + str(prediction))
        elif image == "20.png":
            if prediction == None:
                print("correct")
                correct += 1
            else:
                print("Inncorrect")
            print("Low Cargo Scored on Rocket during Teleoperated: " + str(prediction))


        os.remove(file_name)
    accuracy = (correct/total)*100
    print("Accuracy: " + str(accuracy) + "%")



if __name__ == "__main__":
    sheet = compile_sheet("sheet.jpg")
