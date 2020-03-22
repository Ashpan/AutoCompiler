###WRITTEN BY: BILAL QADAR & ASHPAN RASKAR###
import sys
import os
sys.path.insert(0, '/sheet/')
sys.path.insert(0, '/recognition/')
sys.path.insert(0, '/database/')
from images import *
from recognition import number_rec
from database import database

for file in os.listdir(os.path.join('processing', 'staged')):
	labels = runBox(file)
	print(labels)
	directory = path='./processing/completed/'
    ###CHANGE TEST.CSV TO WHATEVER CSV IS BEING USED###
	# database.postCSV(directory,'./database/test.csv')
    ###CHANGE TEST.CSV TO WHATEVER CSV IS BEING USED AND TEST_EVENT TO THE DATABASE EVENT KEY###
	# database.pushToDatabase('./database/test.csv','test_event')