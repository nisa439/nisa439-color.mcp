import requests
import json

def get_color(color: str) -> str:
    """
    Get the color name from the color code.

    """
    #use 'https://colormagic.app/api/palette/search?q={searchQuery}'to get the color name
          
    
    url="https://colormagic.app/api/palette/search?q={}"
    response = requests.get(url.format(color))
    if response.status_code == 200:
        data = response.json()
        if data and 'results' in data and len(data['results']) > 0:
            color_name = data['results'][0]['name']
            return color_name
        else:
            return "Color not found"
    else:
        return "Error: Unable to fetch color name"
    