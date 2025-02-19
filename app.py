from flask import Flask, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://rickandmortyapi.com/api/character/"

# Helper function to filter characters based on criteria
def filter_character(character, criteria):
    """
    Filters a character based on the given criteria.
    """
    if criteria == "human" and character['species'] == "Human":
        return True
    if criteria == "alive" and character['status'] == "Alive":
        return True
    if criteria == "earth":
        # Check if 'origin' or 'location' contains the word 'Earth'
        if 'Earth' in character.get('origin', {}).get('name', '') or 'Earth' in character['location']['name']:
            return True
    return False

# Function to fetch characters based on criteria
def fetch_characters(criteria=None):
    """
    Fetches and filters characters based on the given criteria (human, alive, earth).
    """
    filtered_characters = []
    page = 1

    while True:
        try:
            response = requests.get(f"{BASE_URL}?page={page}")
            response.raise_for_status()  # Will raise an exception for 4xx/5xx responses
        except requests.exceptions.RequestException as e:
            return {"error": f"Unable to fetch data from API: {str(e)}"}, 500

        data = response.json()
        for character in data['results']:
            if filter_character(character, criteria):
                filtered_characters.append({
                    "Name": character['name'],
                    "Location": character['location']['name'],
                    "Image": character['image']
                })

        if not data['info']['next']:  # No more pages left
            break

        page += 1

    return filtered_characters

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """
    Health check endpoint to verify the service is running.
    """
    return jsonify({"status": "ok"}), 200

@app.route('/characters/human', methods=['GET'])
def get_human_characters():
    """
    Fetch and return all human characters.
    """
    characters = fetch_characters(criteria="human")
    return jsonify(characters), 200

@app.route('/characters/alive', methods=['GET'])
def get_alive_characters():
    """
    Fetch and return all alive characters.
    """
    characters = fetch_characters(criteria="alive")
    return jsonify(characters), 200

@app.route('/characters/earth', methods=['GET'])
def get_earth_characters():
    """
    Fetch and return all characters associated with Earth (origin or location).
    """
    characters = fetch_characters(criteria="earth")
    return jsonify(characters), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

