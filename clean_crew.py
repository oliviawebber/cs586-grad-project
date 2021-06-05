import csv
keys = set()
with open('crew.csv', 'r', encoding='utf-8') as rf:
    with open('crew-clean.csv', 'w', newline='', encoding='utf-8') as wf:
        rd = csv.reader(rf)
        cw = csv.writer(wf)
        cw.writerow(['personid', 'productionid', 'job'])
        skip_header = True
        for row in rd:
            if skip_header:
                skip_header = False
                continue
            person_id = int(row[0])
            production_id = int(row[1])
            job = row[2]

            if (production_id, person_id) in keys:
                continue
            else:
                keys.add((production_id,person_id))

            cw.writerow([person_id, production_id, job])
            

keys = None
persons = set()
productions = set()
with open('person.csv', 'r', encoding='utf-8') as rf:
    rd = csv.reader(rf)
    skip_header = True
    for row in rd:
        if skip_header:
            skip_header = False
            continue
        person_id = row[0]
        persons.add(int(person_id))

with open('production.csv', 'r', encoding='utf-8') as rf:
    rd = csv.reader(rf)
    skip_header = True
    for row in rd:
        if skip_header:
            skip_header = False
            continue
        production_id = row[0]
        productions.add(int(production_id))

with open('crew-clean.csv', 'r', encoding='utf-8') as rf:
    with open('crew-very-clean.csv', 'w', newline='', encoding='utf-8') as wf:
        rd = csv.reader(rf)
        cw = csv.writer(wf)
        cw.writerow(['personid', 'productionid', 'job'])
        skip_header = True
        for row in rd:
            if skip_header:
                skip_header = False
                continue
            person_id = int(row[0])
            production_id = int(row[1])
            job = row[2]

            if not person_id in persons or not production_id in productions:
                continue

            cw.writerow([person_id, production_id, job])
