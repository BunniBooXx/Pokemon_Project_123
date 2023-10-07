import requests

def pokemon_api(id): 
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    result = requests.get(url)

    if result.ok:
        data = result.json()
        my_response= {
            "name": data['name'], 
            "ability" : data['abilities'][0], 
            "stats": data['stats'][0],
            "stats2": data['stats'][1],
            "stats3":data['stats'][2], 
            "sprite": data['sprites']['front_shiny']
        }
        return my_response
    else:
        return None