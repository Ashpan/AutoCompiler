from number_rec import *
import os

def test_data(directory):
    images = os.listdir(directory)
    size = len(images)
    individual_acc = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    correct = 0
    incorrect = 0
    for i in range(len(images)):
        guess = number_recognition(os.path.join(directory,images[i]))

        if guess[0] == images[i][0]:
            correct += 1
            individual_acc[int(images[i][0])] += 1
        else:
            incorrect += 1
        print("Guess for " + images[i] + ": " + str(guess[0]))

    accuracy = (correct/size)*100
    for key in individual_acc.keys():
        ind_acc = (individual_acc[key]/(size/10))*100
        print(str(key) + " Accuracy: " + str(ind_acc))

    print("Overall Accuracy: " + str(accuracy))
    print("Test Set Size: " + str(size))
    
if __name__ == "__main__":
    number = test_data("/Users/bilalqadar/Documents/GitHub/FuckCompiling/test_data/pencil_set")
    print(number)
