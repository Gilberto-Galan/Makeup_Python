import Constantes as Constantes
import BuscarProductos as Buscar
import os

def MostrarMenu():
    print(Constantes.variable_menu_principal)
    ValidarMenu()

def ValidarMenu():
    preguntar_menu = True
    while preguntar_menu:
        global opcion_menu_principal
        opcion_menu_principal = input("Escriba el numero de la opción que quiere hacer: \n")
        try:
            opcion_menu_principal = int(opcion_menu_principal)
            preguntar_menu = False
        except ValueError:
            print ("Eso no es un numero")
        else:
            if opcion_menu_principal == 1:
                MostrarSubMenu1()
            elif opcion_menu_principal == 2:
                MostrarSubMenu2()
            elif opcion_menu_principal == 3:
                MostrarSubMenu3()
            elif opcion_menu_principal == 4:
                MostrarSubMenu4()
            elif opcion_menu_principal == 5:
                archivo = 'Excel_files.xlsx'
                if os.path.exists(archivo):
                    os.remove(archivo)
                    print("El archivo ha sido eliminado")
                else:
                    print("El archivo no existe")
                return MostrarMenu()
            elif opcion_menu_principal == 6:
                print("opción salir")
            else:
                print ("Opcion no valida, vuelva a intentar.")
                preguntar_menu = True

def ValidarSubMenus():
    preguntar_menu = True
    while preguntar_menu:
        opcion_submenu = input("Escriba el numero de la opción que quiere hacer: \n")
        try:
            opcion_submenu = int(opcion_submenu)
            preguntar_menu = False
        except ValueError:
            print ("Eso no es un numero")
        else:
            if opcion_submenu == 1:
                preguntar_menu = False
                Buscar.FiltrarOpcionesSubmenu1()
            elif opcion_submenu == 2:
                preguntar_menu = False
                Buscar.FiltrarOpcionesSubmenu2()
            elif opcion_submenu == 3:
                if opcion_menu_principal == 4:
                    print("grafica 3")
                MostrarMenu()               
            else:
                print ("Opcion no valida, vuelva a intentar.")
                preguntar_menu = True

#cambiar menus y submenus a constantes
def MostrarSubMenu1():
    print(Constantes.variable_submenu1)
    ValidarSubMenus()

def MostrarSubMenu2():
    print(Constantes.variable_submenu2)
    ValidarSubMenus()

def MostrarSubMenu3():
    print(Constantes.variable_submenu3)
    ValidarSubMenus()

def MostrarSubMenu4():
    print(Constantes.variable_submenu4)
    ValidarSubMenus()
