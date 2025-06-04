# 📊 Embrapa API - Tech Challenge

API pública para consulta de dados vitivinícolas extraídos do site da Embrapa, com foco em auxiliar análises e previsões de safra via integração com dashboards e modelos de machine learning.

---

## 🔧 1. Arquitetura do Sistema

### 📌 Diagrama Simplificado
[Site Embrapa] → [API Flask (Render)] → [Aplicação Cliente]


### 🔄 Fluxo de Dados

- **Coleta:** Web scraping do site da Embrapa com `BeautifulSoup`.
- **Transformação:** Conversão dos dados para JSON.
- **Disponibilização:** Endpoints REST (ex: `/api/producao`, `/api/processamento`).
- **Consumo:** Dashboards, aplicativos ou modelos de machine learning.

---

## 🚀 2. Plano de Deploy

### ☁️ Infraestrutura

- **Plataforma:** [Render](https://render.com) (plano gratuito).
- **API Online:** [https://embrapaapi.onrender.com](https://embrapaapi.onrender.com)
- **Recursos:** 512MB RAM, CPU compartilhada.

### ⚙️ Deploy Automatizado

Push no GitHub → Render realiza o deploy automático


- **Build:** `pip install -r requirements.txt`
- **Execução:** `python app.py`

### 🔍 Monitoramento

- Acompanhamento de logs via painel da Render.
- Health check básico disponível no endpoint `/`.

---

## 📈 3. Cenário de Uso

### Dashboard de Previsão de Safra

**Funcionalidades:**

- Visualização de dados históricos (produção, exportação, etc.)
- Identificação de tendências para produtores e comerciantes
- 🔮 **Futuro:** Integração com modelos de ML para prever demanda

---

## 📚 4. Documentação dos Endpoints

### Endpoints Disponíveis

| Método | Endpoint               | Descrição                  | Exemplo de Uso                                               |
|--------|------------------------|----------------------------|--------------------------------------------------------------|
| GET    | `/api/producao`        | Dados de produção          | `curl https://embrapaapi.onrender.com/api/producao`          |
| GET    | `/api/processamento`   | Dados de processamento     | `curl https://embrapaapi.onrender.com/api/processamento`     |
| GET    | `/api/comercializacao` | Dados de comercialização   | `curl https://embrapaapi.onrender.com/api/comercializacao`   |
| GET    | `/api/importacao`      | Dados de importação        | `curl https://embrapaapi.onrender.com/api/importacao`        |
| GET    | `/api/exportacao`      | Dados de exportação        | `curl https://embrapaapi.onrender.com/api/exportacao`        |

### 🧪 Exemplo de Resposta

```json
{
  "opcao": "opt_02",
  "data": [
    ["Ano", "Vinho (L)", "Espumante (L)"],
    ["2020", "350000000", "15000000"]
  ],
  "status": "success"
}
```
🗂️ 5. Estrutura do Projeto
/embrapa-api
├── app.py            # Código principal da API
├── scraper.py        # Coleta de dados via scraping
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação e instruções

🧪 6. Como Usar
Acesso Rápido via Navegador
https://embrapaapi.onrender.com/api/producao

Integração com Código (Python)

📎 Repositório GitHub
Link do repositório: https://github.com/leonardocae/embrapaAPI/

Projeto desenvolvido como parte do Tech Challenge.
