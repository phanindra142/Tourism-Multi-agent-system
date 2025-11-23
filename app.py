from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_coordinates(place):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 1}
    headers = {"User-Agent": "TourismMultiAgentWeb/1.0"}
    response = requests.get(url, params=params, headers=headers)
    results = response.json()
    if results:
        lat = float(results[0]['lat'])
        lon = float(results[0]['lon'])
        return lat, lon
    return None, None

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": "true", "forecast_days": 1, "hourly": "precipitation_probability"}
    response = requests.get(url, params=params)
    data = response.json()
    try:
        temperature = data['current_weather']['temperature']
        rain_prob = data['hourly']['precipitation_probability'][0]
        return temperature, rain_prob
    except Exception:
        return None, None

def get_places(lat, lon):
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json][timeout:30];
    (
      node["tourism"="attraction"](around:8000,{lat},{lon});
      node["leisure"="park"](around:8000,{lat},{lon});
      node["amenity"="museum"](around:8000,{lat},{lon});
      node["amenity"="zoo"](around:8000,{lat},{lon});
      node["historical"="yes"](around:8000,{lat},{lon});
    );
    out 20;
    """
    response = requests.post(overpass_url, data=overpass_query)
    data = response.json()
    attractions = []
    for elem in data.get('elements', []):
        name = elem.get('tags', {}).get('name')
        if name and name not in attractions:
            attractions.append(name)
        if len(attractions) >= 5:
            break
    return attractions

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    place = request.form.get('place')
    weather = request.form.get('weather') == 'true'
    places = request.form.get('places') == 'true'
    lat, lon = get_coordinates(place)

    if lat is None or lon is None:
        return jsonify({"error": "Sorry, I don’t know if this place exists."})

    result = {}
    if weather:
        temperature, rain_prob = get_weather(lat, lon)
        if temperature is not None and rain_prob is not None:
            result['weather'] = f"In {place} it’s currently {temperature}°C with a chance of {rain_prob}% to rain."
        else:
            result['weather'] = f"Weather information for {place} is currently unavailable."
    if places:
        attractions = get_places(lat, lon)
        if attractions:
            result['places'] = f"In {place} these are the places you can go:\n" + "\n".join(attractions)
        else:
            result['places'] = "No attractions found in this place."
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
