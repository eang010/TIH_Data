# TIH_Data
Extracting data from TIH API

# Description of scripts
Attractions_Sort_By_Rating.py : Export all attractions data as a text file. Sorted by ratings.

TIH_Para_2.py : Export all data in the dataset and convert into paragraphs using OpenAI. Sorted by ratings.

TIH_Para_2_testing : Export only a few records (based on the limit and offset parameter) from the dataset and convert into paragraphs using OpenAI. Sorted by ratings.
TIH API has a limit of 50.

Export as Word : Contains each category filtered fields, export as word doc in JSON format

1_txt_file_per_cat : Export each category as a text file, sorted by ratings

# Setup

##1 Run pip install -r requirements.txt or pip3 install -r requirements.txt

##2 Input API key for TIH API and OpenAI

##3 Input dataset in query_params based on the list below.

"data": [
    "accommodation",
    "attractions",
    "bars_clubs",
    "cruises",
    "events",
    "food_beverages",
    "mice_events",
    "precincts",
    "shops",
    "tours",
    "venues",
    "walking_trails"
  ]