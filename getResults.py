import csv
import operator
new_dict = {}
high = {}
with open('result.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if (row['item1'] == '900965-02'):
            new_dict.update({row['item2']:row['score']})
        #print(row['item1'], row['last_name'])
        if(row['score'] > '0.01'):
            print(row['score'])
            high.update({row['item2']:row['score']})
            
sorted_x = sorted(new_dict.items(), key=operator.itemgetter(1))
