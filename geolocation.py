import requests
import folium
import os

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        response.raise_for_status()
        data = response.json()
        ip = data.get("ip", "Not found")
        location = data.get("loc", "0,0").split(",")
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        return ip, float(location[0]), float(location[1]), city, region, country
    except requests.exceptions.RequestException as e:
        print(f"Error fetching location data: {e}")
        return None, 0, 0, "Unknown", "Unknown", "Unknown"

def display_map(lat, lon, city, region, country):
    map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker(
        [lat, lon],
        popup=f"Location:\nLatitude: {lat}, Longitude: {lon}\nCity: {city},\nRegion: {region},\nCountry: {country}"
    ).add_to(map)
    map.save("map.html")
    print("Map saved as map.html. Open it in your browser:")
    print("file://" + os.getcwd() + "/map.html")

def main():
    ip, lat, lon, city, region, country = get_location()
    if ip:
        print(f"Your IP address is: {ip}")
        print(f"Your location is: {lat}, {lon}")
        print(f"Your city is: {city}")
        print(f"Your region is: {region}")
        print(f"Your country is: {country}")
        display_map(lat, lon, city, region, country)
    else:
        print("Could not fetch geolocation.")

if __name__ == "__main__":
    main()
