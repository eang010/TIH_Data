import requests
import json

api_url = "https://api.stb.gov.sg/content/common/v2/search"
api_key = ""

query_params = {
    "dataset": "attractions",
    "limit": 50,
    "offset": 0,
}

headers = {
    "X-API-KEY": api_key
}

# Initialize a list to store selected attraction data
selected_attraction_data = []

while True:
    # Make the API request with the specified query parameters and headers
    response = requests.get(api_url, params=query_params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not data['data']:
            break  # No more data to fetch
        else:
            for item in data['data']:
                # Select the fields you want to include in the JSON
                selected_item = {
                    "category": item['categoryDescription'],
                    "type": item['type'],
                    "name": item['name'],
                    "description": item['description'],
                    "rating": item['rating'],
                    "nearestMrtStation": item['nearestMrtStation'],
                    "officialWebsite": item['officialWebsite'],
                    "admissionInfo": item['admissionInfo'],
                    "pricing": item.get('pricing', {}).get('others'),
                    "amenities": item['amenities'],
                    "address": " ".join(part for part in [item['address']['block'], item['address']['streetName'], item['address']['postalCode']] if part),
                    "businessHour": [
                        {
                            "day": business_hour['day'],
                            "openTime": business_hour['openTime'],
                            "closeTime": business_hour['closeTime'],
                            "description": business_hour['description']
                        }
                        for business_hour in item.get("businessHour", [])
                    ],
                    "businessHourNotes": item.get('businessHourNotes', {}).get('notes')
                }
                selected_attraction_data.append(selected_item)

            query_params["offset"] += query_params["limit"]  # Update the offset to fetch the next page
    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Sort selected_attraction_data by rating in descending order
selected_attraction_data = sorted(selected_attraction_data, key=lambda x: x['rating'], reverse=True)

# Export the selected attraction data as a plain text file
with open('selected_attractions_sorted_by_rating_cat.txt', 'w', encoding='utf-8') as text_file:
    for item in selected_attraction_data:
        text_file.write('\n'.join(f"{key}: {value}" for key, value in item.items()))
        text_file.write("\n\n")
