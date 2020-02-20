from numpy.random import randint
import csv

#Create a 10 csv files with random integer numbers
for item in range(10):
    with open("{}data.csv".format(item), "w") as csvfile:
        values = randint(0, 5, 10)
        new_list =[]
        for i in values:
            new_list.append(values[i])
        filewriter = csv.writer(csvfile, delimiter=',')
        print(new_list)
        filewriter.writerow(["a", "b", "c", "d", "e"])
        filewriter.writerow(new_list)