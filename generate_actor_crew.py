import csv
with open('title-principals.tsv', 'r', encoding='utf-8') as rf:
    with open('actor.csv', 'w', newline='', encoding='utf-8') as af:
        with open('crew.csv', 'w', newline='', encoding='utf-8') as cf:
            rd = csv.reader(rf, delimiter='\t')
            aw = csv.writer(af)
            cw = csv.writer(cf)
            aw.writerow(['personid', 'productionid', 'charactername'])
            cw.writerow(['personid', 'productionid', 'jobtitle'])
            skip_header = True
            for row in rd:
                if skip_header:
                    skip_header = False
                    continue
                try:
                    person_id = int(row[2][2:])
                    production_id = int(row[0][2:])
                except:
                    continue
                try:
                    character = eval(row[5])[0]
                    job = None
                except:
                    job = row[3]

                if job is None:
                    aw.writerow([person_id, production_id, character])
                else:
                    cw.writerow([person_id, production_id, job])
                
