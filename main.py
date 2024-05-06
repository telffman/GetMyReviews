import json
import csv

with open('Reviews.json', 'r') as file:
    data = json.load(file)


with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Five Star Rating', 'Review Text', 'Date'])

    for feature in data['features']:
        
        name = feature['properties']['location'].get('name', 'No Name Available')
        
        rating = feature['properties'].get('five_star_rating_published', 'No Rating')

        review_text = feature['properties'].get('review_text_published', '')

        date = feature['properties'].get('date', 'No Date Provided')

        writer.writerow([name, rating, review_text, date])
