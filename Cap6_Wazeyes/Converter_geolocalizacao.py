from geopy.geocoders import Nominatim
from Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes")
dicionario = ler_arquivo("entrada.json")
print(dicionario)
lista = dicionario["endereco"]
endereco = lista[1] + " " + lista[0] + " " + lista[3]
print(endereco)
location = geolocator.geocode(endereco)
print(location)
saida = {"coordenadas": (location.latitude, location.longitude)}
gravar_arquivo(saida, "saida.json")
