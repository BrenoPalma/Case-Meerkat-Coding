from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/biancascrape', methods=['GET'])
def scrape_bianca():
    # URL do site
    url = "http://bianca.com"

    # Fazer a requisição HTTP do site
    response = requests.get(url)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Usar BeautifulSoup para fazer o parsing do HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Pegando o título da página
        title = soup.title.string if soup.title else 'titulo nao encontrado'

        # Pegando o primeiro <h1>
        h1 = soup.find('h1').text if soup.find('h1') else 'H1 tag nao encontrada'

        # Procurar por outros elementos caso sejam adicionados
        other_elements = []
        for element in soup.find_all(['h2', 'p', 'div']):
            other_elements.append(element.text.strip())

        # Dados de saída
        data = {
            'titulo': title,
            'h1': h1,
            'outros_elementos': other_elements
        }
        return jsonify(data)
    else:
        return jsonify({'error': 'Falha ao acessar a pagina'})

if __name__ == "__main__":
    app.run(debug=True)