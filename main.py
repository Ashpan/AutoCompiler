###WRITTEN BY: BILAL QADAR & ASHPAN RASKAR###
import sys
import os
sys.path.insert(0, '/sheet/')
sys.path.insert(0, '/recognition/')
sys.path.insert(0, '/database/')
from images import *
from recognition import number_rec
from database import database

CSV_location = '.database/file.csv'
database_cred = 'my firebase credentials'
id = 0
for file in os.listdir(path='./processing/staged'):
    get_rect(file,(1300,130))
    data = get_data("./processing/completed/",((2100,20),250,200,10))
    database.postCSV(data,CSV_location)
    database.pushToDatabase('test_event',str(id),CSV_location,creds)
    id += 1
