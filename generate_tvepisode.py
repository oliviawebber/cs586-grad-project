import csv
ids = set()
with open('production.csv', 'r', encoding='utf-8') as rf:
    rcsv = csv.reader(rf)
    skip_header = True
    for row in rcsv:
        if skip_header:
            skip_header = False
            continue
        production_id = int(row[0])
        ids.add(production_id)
        
with open('title-episode.tsv', 'r', encoding='utf-8') as rf:
    with open('tvepisodes.csv', 'w', newline='', encoding='utf-8') as wf:
        rd = csv.reader(rf, delimiter='\t')
        wr = csv.writer(wf)
        wr.writerow(['seriesid','productionid','season','episode'])
        skip_header = True
        for row in rd:
            if skip_header:
                skip_header = False
                continue
            try:
                production_id = int(row[0][2:])
                series_id = int(row[1][2:])
            except:
                continue
            try:
                season_number = int(row[2])
            except:
                season_number = 'null'
            try:
                episode_number = int(row[3])
            except:
                episode_number = 'null'
            if production_id in ids and series_id in ids:
                wr.writerow([series_id, production_id, season_number, episode_number])
                
