import requests

#? Esta funcion sirve para buscar por marca
def buscar_productos_por_marca(marca):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?brand={marca}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
#? Esta funcion sirve para buscar por categoria
def buscar_productos_por_categoria(categoria):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_type={categoria}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#? Esta funcion sirve para buscar por etiqueta
def buscar_productos_por_etiqueta(etiqueta):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?product_tags={etiqueta}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
#? Esta funcion sirve para buscar por precio    
def buscar_productos_por_rango_de_precio(minimo, maximo):
    url = f"https://makeup-api.herokuapp.com/api/v1/products.json?price_greater_than={minimo}&price_less_than={maximo}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None