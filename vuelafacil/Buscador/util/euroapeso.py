from bs4 import BeautifulSoup
import requests

#funcion para convertir el Euro a pesos con valor oficial diario
def precioEuro():
    #Scraping de pagina web para tener el valor real del EURO en PESOS
    url = "https://www.larepublica.co/indicadores-economicos/mercado-cambiario/euro"
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")

    valor_euro = soup.find_all('span', class_="price")

    valor= list()
    precio = ""
    respuesta= ""
    numero = ""
    for i in valor_euro:
        valor.append(i.text)
        for i in valor[:1]:
            precio = i[2:] #para tomar solo el valor del euro en tiempo real
    for i in precio:        #para convertir el string en un formato valido para convertir a float
            if i != ".":
                respuesta+=i
            else:
                pass
    for i in respuesta:
            if i == ",":
                i = "."
            else:
                pass
            numero += i
    return float(numero)

 #funcion para dar el valor del viaje en pesos
   
def convertir_euros_a_pesos(cantidad_euros):
    return (cantidad_euros * precioEuro())