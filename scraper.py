import requests
from bs4 import BeautifulSoup

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

def get_data(opcao):
    try:
        params = {'opcao': opcao}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
         
        data = []
        tables = soup.find_all('table', class_='tb_dados')
        
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                if cols:  # Ignora linhas vazias
                    data.append(cols)
        
        return {
            "opcao": opcao,
            "data": data,
            "status": "success"
        }
    except Exception as e:
        return {
            "opcao": opcao,
            "error": str(e),
            "status": "error"
        }