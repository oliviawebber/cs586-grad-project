import csv
genre_list = set()
with open('title-basics.tsv', 'r', encoding='utf-8') as f:
    rd = csv.reader(f, delimiter='\t')
    skip_header = True
    for row in rd:
        if skip_header:
            skip_header = False
            continue
        genres = row[-1].split(',')
        genre_list.update(genres)

genre_list.remove('\\N')
genre_id = 0
with open('genre.csv', 'w', newline='', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerow(['id','genre'])
    for genre in genre_list:
        genre_id += 1
        wr.writerow([genre_id, genre])

        
        
    
