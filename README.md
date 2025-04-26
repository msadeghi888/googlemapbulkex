# Location Scraper

A Python tool that uses SerpAPI to search for locations and exports the results to a CSV file.

## Overview

This script searches for locations using Google Maps data through the SerpAPI service. It extracts key information about each place including name, address, phone number, rating, number of reviews, and creates direct Google Maps links for each location.

## Requirements

- Python 3.x
- Required packages:
  - requests
  - pandas
  - (os and time are standard libraries)

You can install the required packages using pip:

```bash
pip install requests pandas
```

## Setup

1. Sign up for an API key at [SerpAPI](https://serpapi.com/)
2. Replace the `YOUR_API_KEY` placeholder with your actual API key in the script
3. Set your desired location by replacing `YOUR_LOCATION` with your target location

## Usage

1. Configure your search parameters in the script as needed:
   - `QUERY`: Your search term (default is in Persian)
   - `location`: Target location
   - Other parameters like language (`hl`) can be adjusted as well

2. Run the script:
   ```bash
   python main.py
   ```

3. The script will output a CSV file named `fil.csv` containing all the found locations

## CSV Output Format

The CSV file includes the following columns:
- Name
- Address
- Phone
- Rating
- Reviews
- Type
- Google Maps Link

## Error Handling

The script includes basic error handling for:
- API connection failures
- Missing result data
- File creation issues

## Notes

- The script uses UTF-8-SIG encoding to ensure proper character display in the CSV file
- SerpAPI has usage limits based on your subscription plan
- Some fields may be empty depending on the data availability from Google Maps


## Acknowledgements

- [SerpAPI](https://serpapi.com/) for providing the search API
- [Pandas](https://pandas.pydata.org/) for data handling capabilities
