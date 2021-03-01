from selenium import webdriver
from object_config import parameters as param

class Meli(object):

    link = 'https://inmuebles.mercadolibre.com.ar/' + \
           'departamentos/alquiler/1-dormitorio/1-a-2-ambientes/' + \
           'capital-federal/caballito-o-almagro-o-barrio-norte-o-' + \
           'belgrano-o-flores-o-palermo-o-parque-centenario-o-' + \
           'palermo-hollywood-o-palermo-chico-o-palermo-nuevo-o-' + \
           'palermo-soho-o-recoleta-o-villa-crespo/_DisplayType_G_NoIndex_True'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Meli.link)

    def get_cards(self):
        return self.driver.find_elements_by_xpath(param['MELI']['cards'])

x = Meli()