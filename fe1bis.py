import csv
import calendar

def main():
    file = open("train.csv")
    csv_file = csv.reader(file)
    n_crimes_by_category = {}
    diu = {}
    not_prosecuted = {}
    n_crimes_by_neigh = {}
    crimes_by_day = {}
    # Skipping the header
    csv_file.next()
    for crime in csv_file:
        if crime[1] not in n_crimes_by_category:
            n_crimes_by_category[crime[1]] = 0
        n_crimes_by_category[crime[1]] += 1
        if crime[1] == "DRIVING UNDER THE INFLUENCE":
            if crime[3] not in diu:
                diu[crime[3]] = 0
            diu[crime[3]] += 1
        if crime[5] == "NOT PROSECUTED":
            if crime[1] not in not_prosecuted:
                not_prosecuted[crime[1]] = 0
            not_prosecuted[crime[1]] += 1
        if crime[4] not in n_crimes_by_neigh:
            n_crimes_by_neigh[crime[4]] = 0
        n_crimes_by_neigh[crime[4]] += 1
        if crime[3] not in crimes_by_day:
            crimes_by_day[crime[3]] = 0
        crimes_by_day[crime[3]] += 1

    print "1)"
    l = sorted(n_crimes_by_category.iteritems(), key=lambda x:x[1], reverse=True)
    for x in range(10):
        print str(l[x][0]) + "-" + str(l[x][1])
    print "2)"
    print max(diu.iterkeys(), key=(lambda k: diu[k]))
    print "3)"
    l = sorted(n_crimes_by_neigh.iteritems(), key=lambda x:x[1], reverse=True)
    for x in range(3):
        print str(l[x][0]) + "-" + str(l[x][1])
    print "4)"
    for crime in not_prosecuted.iterkeys():
        not_prosecuted[crime] = not_prosecuted[crime] * 100.0 / n_crimes_by_category[crime]
    l = sorted(not_prosecuted.iteritems(), key=lambda x:x[1], reverse=True)
    print str(l[0][0]) + "-" + str(l[0][1])[:3] + "%"
    print "5)"
    print crimes_by_day


if __name__ == "__main__":
    main()
