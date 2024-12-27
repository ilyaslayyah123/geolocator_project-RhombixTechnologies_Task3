# Geolocatior Project

## Overview
This project is a Python script that fetches your geolocation (IP address, city, region, country, latitude, and longitude) and displays it on an interactive map. The map is saved as an HTML file that can be opened in a web browser.

## Features
- Fetches public IP address and geolocation data using the `ipinfo.io` API.
- Displays the location on an interactive map using the `folium` library.
- Saves the map as an HTML file for easy viewing.
- Provides detailed location information in the console.

## Installation

### Prerequisites
- Python 3.7 or higher installed on your system.
- `pip` (Python package manager).

### Required Libraries
Install the required libraries using the following command:
```bash
pip install requests folium
```

## Usage
1. Clone this repository or download the script file.
2. Run the script in a Python environment:
   ```bash
   python geolocation.py
   ```
3. The script will display your IP address and location details in the console. It will also generate a file named `map.html`.
4. Open the `map.html` file in your web browser to view your location on the map.

## Example Output
### Console Output
```
Your IP address is: 123.45.67.89
Your location is: 37.7749, -122.4194
Your city is: San Francisco
Your region is: California
Your country is: United States
Map saved as map.html. Open it in your browser:
file:///path/to/your/directory/map.html
```

### Map
The map displays a marker at your location with a popup showing:
- Latitude and Longitude
- City
- Region
- Country

## Project Structure
```
.
├── geolocation.py    # Main script file
├── map.html          # Generated map file (after running the script)
```

## Error Handling
- If there is no internet connection or the API request fails, the script will display an error message and use default placeholder values.

## Future Enhancements
- Add support for user-input IP addresses to fetch geolocation for any IP.
- Improve the UI of the map with additional markers or layers.
- Implement a GUI using `tkinter` or `PyQt`.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
Developed by [Muhammad ilyas]www.linkedin.com/in/muhammad-ilyas-a59bb0289.

Feel free to contribute or provide feedback!

