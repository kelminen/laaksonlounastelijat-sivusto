from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def lounaslistat():
    # Määrittele lounaslistojen URL-osoitteet
    urls = {
        "Viisi Penniä": "https://viisipennia.fi/lounas/",
        "Toinen Ravintola": "https://toinenravintola.fi/lounas/"  # Vaihda oikeaan URL:iin
    }

    lounaslistat = {}
    for nimi, url in urls.items():
        try:
            # Hae sivun sisältö
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')

            # Etsi lounaslistan sisältö (muokkaa valitsinta tarpeen mukaan)
            lounas = soup.find('div', class_='lounaslista')  # Vaihda oikeaan elementtiin
            lounaslistat[nimi] = lounas if lounas else "Lounaslistaa ei löytynyt."
        except requests.exceptions.RequestException as e:
            lounaslistat[nimi] = f"Virhe haettaessa lounaslistaa: {e}"

    # Luo HTML-sivu, jossa lounaslistat näytetään vierekkäin
    html = """
    <html>
    <head>
        <style>
            .container {
                display: flex;
                gap: 20px;
            }
            .lounas {
                border: 1px solid #ccc;
                padding: 10px;
                width: 45%;
            }
        </style>
    </head>
    <body>
        <div class="container">
            {% for nimi, lounas in lounaslistat.items() %}
            <div class="lounas">
                <h2>{{ nimi }}</h2>
                <div>{{ lounas|safe }}</div>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, lounaslistat=lounaslistat)

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hae_lounaslista():
    url = "https://www.scandichotels.fi/hotellit/suomi/helsinki/scandic-meilahti/ravintola-ja-baari/ravintola"
    try:
        # Hae verkkosivun sisältö
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Etsi PDF-linkki
        pdf_element = soup.find('p', class_='PdfIconLink')
        if pdf_element:
            pdf_link = pdf_element.find('a')['href']
            pdf_text = pdf_element.get_text(strip=True)
        else:
            pdf_link = None
            pdf_text = "Lounaslistaa ei löytynyt."

    except requests.exceptions.RequestException as e:
        pdf_link = None
        pdf_text = f"Virhe haettaessa sisältöä: {e}"

    # Luo HTML-sivu, jossa PDF-linkki ja esikatselu näytetään
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scandic Meilahti - Lounaslista</title>
        <style>
            iframe {
                width: 100%;
                height: 600px;
                border: 1px solid #ccc;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Scandic Meilahti - Lounaslista</h1>
        {% if pdf_link %}
            <p><a href="{{ pdf_link }}" target="_blank">{{ pdf_text }}</a></p>
            <iframe src="{{ pdf_link }}" title="Lounaslista PDF"></iframe>
        {% else %}
            <p>{{ pdf_text }}</p>
        {% endif %}
    </body>
    </html>
    """
    return render_template_string(html, pdf_link=pdf_link, pdf_text=pdf_text)

if __name__ == '__main__':
    app.run(debug=True)