import csv
import pandas as pd
count = 0
ratings = dict()
with open('title-ratings.tsv', 'r', encoding='utf-8') as rf:
    rcsv = csv.reader(rf, delimiter='\t')
    skip_header = True
    for row in rcsv:
        if skip_header:
            skip_header = False
            continue
        production_id = int(row[0][2:])
        if production_id == 180:
            print('here')
        ratings[production_id] = row[1]
        
with open('title-basics.tsv', 'r', encoding='utf-8') as bf:
    with open('production.csv', 'w', newline='', encoding='utf-8') as wf:
        bcsv = csv.reader(bf, delimiter='\t')
        wr = csv.writer(wf)
        wr.writerow(['id', 'title', 'type', 'rating', 'startyear', 'endyear', 'runtime'])
        skip_header = True
        for row in bcsv:
            if skip_header:
                skip_header = False
                continue
            count += 1
            production_id = int(row[0][2:])
            production_type = row[1]
            production_title = row[2]
            try:
                production_startyear = int(row[5])
            except:
                production_startyear = 'null'
            try:
                production_endyear = int(row[6])
            except:
                production_endyear = 'null'
            try:
                production_runtime = int(row[7])
            except:
                production_runtime = 'null'
            try:
                production_rating = float(ratings[production_id])
            except:
                production_rating = 'null'
            wr.writerow([production_id, production_title, production_type, production_rating, production_startyear, production_endyear, production_runtime])
                

