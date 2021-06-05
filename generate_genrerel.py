import csv
genre_ids = dict()
with open('genre.csv', 'r', encoding='utf-8') as rf:
    rd = csv.reader(rf, delimiter=',')
    skip_header = True
    for row in rd:
        if skip_header:
            skip_header = False
            continue
        genre_ids[row[1]] = int(row[0])
    
with open('title-basics.tsv', 'r', encoding='utf-8') as rf:
    with open('genrerel.csv', 'w', newline='', encoding='utf-8') as wf:
        rd = csv.reader(rf, delimiter='\t')
        wr = csv.writer(wf)
        wr.writerow(['genreid','productionid'])
        skip_header = True
        for row in rd:
            if skip_header:
                skip_header = False
                continue
            try:
                production_id = int(row[0][2:])
                production_genres = row[8].split(',')
            except:
                continue
            for genre in production_genres:
                try:
                    genre_id = genre_ids[genre]
                    wr.writerow([genre_id, production_id])
                except:
                    pass
