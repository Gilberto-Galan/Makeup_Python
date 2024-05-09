import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import ConsultaWeb as Consulta
import Menu as Menu

#? Manejo de Excel y la exportacion a xls 
def Hacer_Lista_de_Productos(productos):
    x = 0
    global lista_productos
    lista_productos = []
    lista_marcas = []
    lista_precios = []
    while len(lista_productos) < len(productos):
        nombre = productos [x] ["name"]
        marca = productos [x] ["brand"]
        precios = productos [x] ["price"]
        lista_productos.append(nombre)
        lista_marcas.append(marca)
        lista_precios.append(precios)
        x = x + 1
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    data = []
    data.append(lista_productos)
    for row in data:
        sheet.append(row)
    workbook.save("Excel_files.xlsx")
    print ("productos encontrados")
    numero_fila=0
    for x in lista_productos:
        print("Nombre del producto: ",lista_productos[numero_fila],"---- Precio del Producto: ",lista_precios[numero_fila])
        numero_fila = numero_fila+1
    return Menu.MostrarMenu()

#? BUSQUEDAD DENTRO DEL REQUESTS

def FiltrarOpcionesSubmenu1():
    if Menu.opcion_menu_principal == 1:
        etiqueta = "Non-GMO"
        productos= Consulta.buscar_productos_por_etiqueta(etiqueta)
        Hacer_Lista_de_Productos(productos)
        
    elif Menu.opcion_menu_principal == 2:
        marca = "fenty"
        productos = Consulta.buscar_productos_por_marca(marca)
        Hacer_Lista_de_Productos(productos)
    
def FiltrarOpcionesSubmenu2():
    if Menu.opcion_menu_principal == 1:
        etiqueta = "cruelty free"
        productos= Consulta.buscar_productos_por_etiqueta(etiqueta)
        Hacer_Lista_de_Productos(productos)

    elif Menu.opcion_menu_principal == 2:
        marca = "anna sui"
        productos = Consulta.buscar_productos_por_marca(marca)
        Hacer_Lista_de_Productos(productos)

if __name__ == "__main__":
    Menu.MostrarMenu()