#coding=utf-8
import csv

def finger_excercise_1():
    '''
    Solution to Finger Excercise 1 of FIUBA's Data Organization class.
    This should show:
        1- The 10 most frequent crimes
        2- The day of the week in which the most DIU's happened
        3- The 3 police districts with the most crimes
        4- The crime with the highest percentaje of "Not prosecuted"
        5- Number of crimes per day of the week
    '''
    # In theory O(n) == O(5n). In real life: O(n) != O(4n)
    with open("train.csv") as file:
        reader = csv.DictReader(file)
        n_crimes_by_category = {}
        diu = {}
        not_prosecuted = {}
        n_crimes_by_neigh = {}
        crimes_by_day = {}
        for crime in reader:
            n_crimes_by_category.setdefault(crime["Category"], 0)
            n_crimes_by_category[crime["Category"]] += 1
            if crime["Category"] == "DRIVING UNDER THE INFLUENCE":
                diu.setdefault(crime["DayOfWeek"], 0)
                diu[crime["DayOfWeek"]] += 1
            if crime["Resolution"] == "NOT PROSECUTED":
                not_prosecuted.setdefault(crime["Category"], 0)
                not_prosecuted[crime["Category"]] += 1
            n_crimes_by_neigh.setdefault(crime["PdDistrict"], 0)
            n_crimes_by_neigh[crime["PdDistrict"]] += 1
            crimes_by_day.setdefault(crime["DayOfWeek"], 0)
            crimes_by_day[crime["DayOfWeek"]] += 1

    # Don't hate me for this :'(
    print "1)"
    l = sorted(n_crimes_by_category.iteritems(), key=lambda x:x[1], reverse=True)
    for x in range(10):
        print str(l[x][0]) + " - " + str(l[x][1])
    print "2)"
    print max(diu.iterkeys(), key=(lambda k: diu[k]))
    print "3)"
    l = sorted(n_crimes_by_neigh.iteritems(), key=lambda x:x[1], reverse=True)
    for x in range(3):
        print str(l[x][0]) + " - " + str(l[x][1])
    print "4)"
    for crime in not_prosecuted.iterkeys():
        not_prosecuted[crime] = not_prosecuted[crime] * 100.0 / n_crimes_by_category[crime]
    l = sorted(not_prosecuted.iteritems(), key=lambda x:x[1], reverse=True)
    print str(l[0][0]) + " - " + str(l[0][1])[:4] + "%"
    print "5)"
    for x in crimes_by_day:
        print x + ": " + str(crimes_by_day[x])


if __name__ == "__main__":
    finger_excercise_1()
