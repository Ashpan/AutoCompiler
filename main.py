import sys
import os
sys.path.insert(0, '/sheet/')
sys.path.insert(0, '/recognition/')
sys.path.insert(0, '/database/')
from images import *
from recognition import number_rec
from database import database

for file in os.listdir(path='./processing/staged'):
    runBox(file)
    directory = path='./processing/completed/'
    database.postCSV(directory,'./database/test.csv')
    database.pushToDatabase('./database/test.csv','test_event')
