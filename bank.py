import csv

class Bank():
    def __init__(self):
        with open("records.csv", "w+") as records:
            reader = csv.reader(records)


# Plan: Create a bank object that records the csv as an array to be interacted with by the other programs. 
# Only necessary functions are read and write, and reading should be done on initialization. 