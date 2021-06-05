import csv
with open('name-basics.tsv', 'r', encoding='utf-8') as rf:
    with open('person.csv', 'w', newline='', encoding='utf-8') as wf:
        rd = csv.reader(rf, delimiter='\t')
        wr = csv.writer(wf)
        wr.writerow(['id','name','birthyear','deathyear'])
        skip_header = True
        for row in rd:
            if skip_header:
                skip_header = False
                continue
            try:
                person_id = int(row[0][2:])
            except:
                continue
            person_name = row[1]
            try:
                birth_year = int(row[2])
            except:
                birth_year = 'null'
            try:
                death_year = int(row[3])
            except:
                death_year = 'null'
            wr.writerow([person_id, person_name, birth_year, death_year])
                
