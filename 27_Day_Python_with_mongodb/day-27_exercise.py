# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:27:36 2024

@author: marku
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://markussommerfeld:Solidus87@30daysofpython.smuxjbo.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
#%%
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = "mongodb+srv://markussommerfeld:Solidus87@30daysofpython.smuxjbo.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython"
client = pymongo.MongoClient(MONGODB_URI)
# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
#%%
from bson.objectid import ObjectId # id object
student_0 = db.students.find_one() # gets first entry
print(student_0)

student_1 = db.students.find_one({'_id':ObjectId('66a077db88e0c88109450672')}) #gets speciifc entry by id
print(student_1)

student_2 = db.students.find_one({'city':'London'}) # search 1 specific entry by key
print(student_2)

student_3 = db.students.find() # search all specific entry by key
for student in student_3:
    print(student)

# search all by entry and return where :1
student_4 = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in student_4:
    print(student)

# search with query like student_2
query = {"country":"Finland"}
students = db.students.find(query)

for student in students:
    print(student)
    
# query with modifier
query = {"country":"Finland", "city":"Helsinki"}
students = db.students.find(query)
for student in students:
    print(student)
    
    
# find students with age > 30
query = {"age":{"$gt":30}} # $gt = greater than
students = db.students.find(query)
for student in students:
    print(student)
    
# only find first 3 entries
students = db.students.find().limit(3)
for student in students:
    print(student)

#find and change order of find
students = db.students.find().sort('name')
for student in students:
    print(student)
    
students = db.students.find().sort('name',-1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
    print(student)
    
#%%

# update database with query
# use update_one()
# once connected the db will automatically update on the web too!
# use upate_many() to change many
query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find({'age':38}):
    print(student)
    
#%%
#  delete_one() deletes one document
# It only removes the first occurrence. 
# When we want to delete many documents we use delete_many() method, it takes a query object. 
# If we pass an empty query object to delete_many({}) it will delete all the documents in the collection.


query = {'name':'John'}
db.students.delete_one(query)
    
for student in db.students.find():
    print(student)
    
#%%
# Using the drop() method we can delete a collection from a database.

db.students.drop()