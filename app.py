from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def viisi_pennia_sisalto():
    url = "https://viisipennia.fi/lounas/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")
    elements = doc.find_all("div", class_="elementor-widget-container")

    # Luo HTML-sivu
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lounaslista</title>
        <style>
            body {
                font-family: 'Roboto', Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            h1 {
                text-align: center;
                font-size: 3.5rem;
                margin: 20px 0 60px;
                background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
                background-size: 200% 200%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: glitter 6s linear infinite;
            }
            .iframe-container {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
                width: 100%;
                padding: 10px;
            }
            iframe {
                width: 100%;
                max-width: 400px;
                height: 700px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .viisipennia-button, .pdf-button {
                background-color: rgb(161, 3, 106);
                color: beige;
                border: none;
                height: 36px;
                width: 300px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 1rem;
                font-weight: bold;
                text-align: center;
                margin-top: 20px;
            }
            .viisipennia-button:hover, .pdf-button:hover {
                background-color: rgb(140, 2, 92);
                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.15);
            }
        </style>
    </head>
    <body>
        <h1>Laakson lounastelijat</h1>
        <div class="iframe-container">
            <iframe src="https://www.lounaat.info/lounas/ravintola-nordis/helsinki" title="Nordis"></iframe>
            <iframe src="http://kahvilawelldone.fi" title="Welldone"></iframe>
            <iframe src="https://iltrio.fi/lounas/" title="iltrio"></iframe>
            <iframe src="https://unicafe.fi/restaurants/meilahti/" title="Unicafe"></iframe>
            <iframe src="https://phadthai.fi" title="Phad Thai"></iframe>
        </div>

        <h2>Viisi Penniä Lounaslista</h2>
        <div>
            {% for element in elements %}
                {{ element|safe }}
            {% endfor %}
        </div>

        <!-- Viisi Penniä -painike -->
        <a href="https://viisipennia.fi/lounas/" target="_blank">
            <button class="viisipennia-button">VIISI PENNIÄ LOUNASLISTA</button>
        </a>

        <!-- PDF-painike -->
        <a href="https://www.scandichotels.com/RestaurantService/RestaurantMenuService/GetMenufile?hotelId=663&amp;restId=rest0&amp;fileId=91920" target="_blank">
            <button class="pdf-button">SCANDIC LOUNASLISTA</button>
        </a>
    </body>
    </html>
    """
    return render_template_string(html, elements=elements)

if __name__ == '__main__':
    app.run(debug=True)