import re
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup

LOGGER = logging.getLogger(__name__)

def criar_driver():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    service = Service('/usr/local/bin/geckodriver')
    driver = webdriver.Chrome(service=service, options=firefox_options)
    return driver

def execute_scrape(cnpj):
    try:
        driver = criar_driver()
        driver.get("http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html")
        
        radio_button_cnpj = driver.find_element(By.ID, "rTipoDocCNPJ")
        radio_button_cnpj.click()
        
        input_cnpj = driver.find_element(By.ID,'tCNPJ')
        input_cnpj.send_keys(cnpj)

        button_consultar = driver.find_element(By.NAME,'btCGC')
        button_consultar.click()

        driver.implicitly_wait(5)
        
        html = driver.page_source
        data = extract_data(html)
        return data
    except Exception as e:
        LOGGER.error(f"Erro ao realizar web scraping: {e}")
    finally:
        driver.quit()
        

def field_finder(soup, field, tag='span'):
    fields = soup.find_all(tag, text=re.compile(field))
    
    for field_tag in fields:
        label_text = field_tag.find_next_sibling('span', class_='label_text')
        if label_text:
            return label_text.get_text(strip=True)
    return None


def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    cnpj_data = {
        "cnpj": field_finder(soup, 'CNPJ'),
        "inscricao_estadual": field_finder(soup, 'Inscrição Estadual'),
        "cadastro_atualizado_em": field_finder(soup, 'Cadastro Atualizado em'),
        "nome_empresarial": field_finder(soup, 'Nome Empresarial'),
        "contribuinte": field_finder(soup, 'Contribuinte?'),
        "nome_fantasia": field_finder(soup, 'Nome Fantasia'),
        "endereco": field_finder(soup, 'Endereço Estabelecimento', tag='div'),
        "atividade_principal": field_finder(soup, 'Atividade Principal'),
        "unidade_auxiliar": field_finder(soup, 'Unidade Auxiliar:'),
        "condicao_uso": field_finder(soup, 'Condição de Uso:'),
        "data_final_contrato": field_finder(soup, 'Data Final do Contrato:'),
        "regime_apuracao": field_finder(soup, 'Regime de Apuração:'),
        "situacao_cadastral": field_finder(soup, 'Situação Cadastral Vigente:'),
        "data_situacao": field_finder(soup, 'Data desta Situação Cadastral:'),
        "data_cadastramento": field_finder(soup, 'Data de Cadastramento:'),
        "operacoes_nfe": field_finder(soup, 'Operações com NF-E:'),
    }
    
    return cnpj_data



