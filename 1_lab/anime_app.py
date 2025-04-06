from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.jikan.moe/v4/anime/54595/episodes")
    data = response.json()

    result = ""
    for episode in data["data"]:
        result += f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} має оцінку {episode.get('score', 'Немає')}<p>"

    return result

@app.route('/about')
def about():
    return "<h1>Про сайт</h1><p>Цей сайт показує аніме-епізоди з MyAnimeList.</p>"

if __name__ == '__main__':
    app.run(debug=True)