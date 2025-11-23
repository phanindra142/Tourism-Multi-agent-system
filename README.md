Project Overview
This project is a web-based multi-agent system that helps users plan their tourism trips. The system allows users to:

Enter a place they want to visit.

View the current weather for that place.

Get up to 5 suggested tourist attractions near that location.

The backend orchestrates the query using three core open-source APIs:

Nominatim (Geocoding): Finds the latitude and longitude of the typed place.

Open-Meteo (Weather): Gets current temperature and rain probability.

Overpass (Tourism): Finds nearby attractions from OpenStreetMap data.

The project demonstrates modular, agent-driven architecture and modern web design.

Features
User-friendly Web Interface: Submit location, choose which info to view.

Weather Agent: Shows current temperature and probability of rain.

Places/Attraction Agent: Suggests 5 points of interest around the location.

Loader Spinner: Indicates data is being fetched.

Modern CSS: Attractive, responsive card layout and button effects.

Error Handling: Graceful messages for unknown locations or missing attractions.

Tech Stack
Frontend: HTML5, CSS3, JavaScript (Vanilla)

Backend: Python 3.x, Flask, Requests

APIs Used:

Nominatim (Geocoding): https://nominatim.openstreetmap.org/

Open-Meteo (Weather): https://open-meteo.com/

Overpass (Points of Interest): https://overpass-api.de/

Folder Structure
text
tourism-multi-agent/
│
├── app.py                # Flask backend server
├── templates/
│   └── index.html        # Main frontend HTML file
Setup & Installation
Clone or Download the Repository

Install Python packages

bash
pip install flask requests
Run the Server

bash
python app.py
By default, the site runs on http://127.0.0.1:5000.

Access the Website

Open a browser and visit http://127.0.0.1:5000

How It Works
Enter a place (city, town, landmark).

Select options: (Show weather and/or attractions).

Submit the form:

The backend gets coordinates for your place using the Nominatim Geocoding API.

If found, Weather Agent gets current weather using Open-Meteo.

Places Agent queries Overpass API for nearby attractions.

Results are displayed nicely on the page.

If a place is unknown or misspelled:

You see a helpful error message.

Loader spinner: Appears during data fetch.

Example Usage
Enter: Bangalore
See:

Weather (e.g., "In Bangalore it’s currently 24°C with a chance of 35% to rain.")

Attractions list (e.g., Lalbagh, Bangalore Palace...)