#coding: utf-8
import csv
from operator import itemgetter

def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

def predict_crimes(crimes, district, k):
    ''' Tries to predict the category of the crimes (of a certain district)
    based on the proximity of other crimes.
    crimes = csv file
    district = string (must be a valid district)
    k = k for knn '''
    with open(crimes) as train_file:
        coincidences = 0
        line = 0
        train_set = csv.DictReader(train_file)
        train_set = filter(lambda x: x["PdDistrict"] == district, train_set)
        for crime_test in train_set:
            dist = []
            for crime_train in train_set:
                dist.append((crime_train["Category"], distance((float(crime_test["X"]), float(crime_test["Y"])),
                    (float(crime_train["X"]), float(crime_train["Y"])))))
            dist.sort(key = lambda x:x[1])
            dist = dist[:k]
            counter = {}
            for crime in dist:
                counter.setdefault(crime[0], 0)
                counter[crime[0]] += 1
            if max(counter.items(), key=itemgetter(1))[0] == train_set[line]["Category"]:
                coincidences += 1
            print str(coincidences) + "/" + str(line)
            line += 1
        print str(coincidences) + "/" + str(len(train_set))

if __name__ == "__main__":
    predict_crimes("train.csv", "NORTHERN", 5)
