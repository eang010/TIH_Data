import requests
import os
import re

# Define a dictionary to map dataset names to their respective selected_item structures
dataset_configs = {
    "accommodation": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "leadInRoomRates": "leadInRoomRates",
        "leadInRoomSize": "leadInRoomSize",
        "noOfRooms": "noOfRooms",
        "amenities": "amenities",
        "address": "address.block address.streetName address.postalCode",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    "attractions": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "admissionInfo": "admissionInfo",
        "pricing": "pricing.others",
        "amenities": "amenities",
        "address": "address.block address.streetName address.postalCode",
        "businessHour": 
        {
            "day": "businessHour.day",
            "openTime": "businessHour.openTime",
            "closeTime": "businessHour.closeTime",
            "description": "businessHour.description"
        },
        "businessHourNotes": "businessHourNotes.notes",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    "bars_clubs": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "amenities": "amenities",
        "address": "address.block address.streetName address.postalCode",
        "businessHour": 
        {
            "day": "businessHour.day",
            "openTime": "businessHour.openTime",
            "closeTime": "businessHour.closeTime",
            "description": "businessHour.description"
        },
        "businessHourNotes": "businessHourNotes.notes",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    "events": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "startDate": "startDate",
        "endDate": "endDate",
        "eventOrganizer": "eventOrganizer",
        "ticketed": "ticketed",
        "pricing": "pricing",
        "address": "address.block address.streetName address.postalCode",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        },
        "eventDetailList": {
            "startTime": "eventDetailList.timePeriod.startTime",
            "endTime": "eventDetailList.timePeriod.endTime",
        }
    },
    "food_beverages": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "rating": "rating",
        "cuisine": "cuisine",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "pricing": "pricing",
        "amenities": "amenities",
        "address": "address.block address.streetName address.postalCode",
        "businessHour": {
            "day": "businessHour.day",
            "openTime": "businessHour.openTime",
            "closeTime": "businessHour.closeTime",
            "description": "businessHour.description"
        },
        "businessHourNotes": "businessHourNotes.notes",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    "precincts": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "details": "details",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "recommendedDwellTime": "recommendedDwellTime",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    "shops": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "amenities": "amenities",
        "address": "address.block address.streetName address.postalCode",
        "businessHour": {
            "day": "businessHour.day",
            "openTime": "businessHour.openTime",
            "closeTime": "businessHour.closeTime",
            "description": "businessHour.description"
        },
        "businessHourNotes": "businessHourNotes.notes",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    "tours": {
        "category": "categoryDescription",
        "type": "type",
        "name": "name",
        "description": "description",
        "tourLanguage": "tourLanguage",
        "tourDuration": "tourDuration",
        "rating": "rating",
        "nearestMrtStation": "nearestMrtStation",
        "officialWebsite": "officialWebsite",
        "startingPoint": "startingPoint",
        "endingPoint": "endingPoint",
        "startDate": "startDate",
        "endDate": "endDate",
        "minimumAge": "minimumAge",
        "pricing": "pricing",
        "childFriendly": "childFriendly",
        "wheelChairFriendly": "wheelChairFriendly",
        "businessHour": {
            "day": "businessHour.day",
            "openTime": "businessHour.openTime",
            "closeTime": "businessHour.closeTime",
            "description": "businessHour.description"
        },
        "businessHourNotes": "businessHourNotes.notes",
        "contact": {
            "primaryContact": "contact.primaryContactNo",
            "secondaryContact": "contact.secondaryContactNo",
        },
        "location": {
            "latitude": "location.latitude",
            "longitude": "location.longitude",
        }
    },
    # Add more dataset configurations as needed
}

# Define the dataset name
dataset_name = "precincts" # Change this to the dataset you want to retrieveÍ

# Define the API URL and API key
api_url = "https://api.stb.gov.sg/content/common/v2/search"
api_key = ""

# Define the dataset configuration
dataset_config = dataset_configs[dataset_name]

# Initialize a dictionary to store selected data
selected_data = {}

# Set up the API request
query_params = {
    "dataset": dataset_name,
    "limit": 50,
    "offset": 0,
}

headers = {
    "X-API-KEY": api_key
}

# Initialize a dictionary to store selected data
dataset_selected_data = {}

# Define a function to create a selected item from an API item and a dataset configuration
def create_selected_item(item, config):
    selected_item = {}
    for key, value in config.items():
        if isinstance(value, dict):
            sub_item = create_selected_item(item, value)
            selected_item[key] = sub_item
        else:
            selected_item[key] = item.get(value)
    return selected_item

# Set up the API request
query_params = {
    "dataset": dataset_name,
    "limit": 50,
    "offset": 0,
}

headers = {
    "X-API-KEY": api_key
}

# Initialize a dictionary to store selected data
dataset_selected_data = {}

# Send API requests until all data has been retrieved
while True:
    response = requests.get(api_url, params=query_params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if not data['data']:
            break
        else:
            for item in data['data']:
                selected_item = create_selected_item(item, dataset_config)
                dataset_selected_data[item['name']] = selected_item
            query_params["offset"] += query_params["limit"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Store the selected data
selected_data[dataset_name] = dataset_selected_data

# Sort the data by ratings in descending order
sorted_data = dict(sorted(selected_data[dataset_name].items(), key=lambda item: item[1].get('rating', 0), reverse=True))

# Create a directory to store the JSON files
output_directory = f"{dataset_name}_data"
os.makedirs(output_directory, exist_ok=True)

# Function to remove special characters and spaces from a string
def sanitize_filename(name):
    # Replace spaces with underscores
    name = name.replace(" ", "_")
    # Remove special characters using regular expressions
    name = re.sub(r'[^\w\s-]', '', name)
    return name

# Export each item's data to a separate JSON file in sorted order
for name, item in sorted_data.items():
    # Sanitize the name for the filename
    sanitized_name = sanitize_filename(name)
    filename = os.path.join(output_directory, f"{sanitized_name}.txt")
    with open(filename, "w") as file:
        file.write('\n'.join(f"{key}: {value}" for key, value in item.items()))
        file.write("\n\n")
