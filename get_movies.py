import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("API_KEY")

def get_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "pt-BR"
    }
    
    r = requests.get(url, params=params)
    r.raise_for_status()

    print("Status:", r.status_code)
    #print("URL:", r.url)
    #print(r.json())
    data = r.json()
    poster_path = data.get("poster_path")
    print(poster_path)
    return poster_path