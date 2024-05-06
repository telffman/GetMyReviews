import json
import csv

# Load JSON data from the file
with open('Reviews.json', 'r') as file:
    data = json.load(file)

# Open a new CSV file and write the extracted data
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Name', 'Five Star Rating', 'Review Text', 'Date'])

    # Loop through each feature in the features list
    for feature in data['features']:
        # Extract name; provide a default if not found
        name = feature['properties']['location'].get('name', 'No Name Available')
        
        # Extract rating; provide a default if not found
        rating = feature['properties'].get('five_star_rating_published', 'No Rating')

        # Extract review text; provide a default if not found or leave it empty
        review_text = feature['properties'].get('review_text_published', '')

        date = feature['properties'].get('date', 'No Date Provided')

        # Write the data to the CSV file
        writer.writerow([name, rating, review_text, date])
