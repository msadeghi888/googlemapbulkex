import requests
import pandas as pd
import os
import time

# Insert your API key here
API_KEY = 'YOUR_API_KEY'
QUERY = 'جایگاه سوخت'

# Search parameters
params = {
    'engine': 'google_maps',
    'q': QUERY,
    'api_key': API_KEY,
    'hl': 'fa',
    'location': 'YOUR_LOCATION',
    'type': 'search',
    'device': 'desktop'
}

# Send request
url = 'https://serpapi.com/search.json'
print("Fetching data...")
response = requests.get(url, params=params)

# Check results
if response.status_code == 200:
    data = response.json()
    places = data.get('local_results', [])
    
    # Sometimes results are in maps_results
    if not places and 'maps_results' in data:
        places = data.get('maps_results', [])
    
    if places:
        results = []
        print(f"Found {len(places)} locations. Processing...")
        
        for place in places:
            place_id = place.get('place_id')
            map_link = None
            if place_id:
                map_link = f"https://www.google.com/maps/place/?q=place_id:{place_id}"
            
            results.append({
                'Name': place.get('title', ''),
                'Address': place.get('address', ''),
                'Phone': place.get('phone', ''),
                'Rating': place.get('rating', ''),
                'Reviews': place.get('reviews', ''),
                'Type': place.get('type', ''),
                'Google Maps Link': map_link
            })
        
        if results:
            filename = 'fil.csv'
            df = pd.DataFrame(results)
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            
            # Check if file was created successfully
            if os.path.exists(filename):
                filesize = os.path.getsize(filename)
                print(f"✅ CSV file created with {len(results)} locations ({filesize} bytes)")
            else:
                print("❌ Error creating file")
        else:
            print("⚠️ Could not extract location data")
    else:
        print("⚠️ No results found")
        print("Available keys:", list(data.keys()))
else:
    print(f"❌ Error: {response.status_code}")
    try:
        error_msg = response.json().get('error', 'Unknown error')
        print(f"Error message: {error_msg}")
    except:
        print("Cannot read error details")
