#funciones de validacion#
from registros import registros


def validacionDeDatoIngresado(usuario):
    if not usuario.isdigit():
        print('Ingrese un dato válido (número).')
        return False
    
    usuario = int(usuario)
    if usuario == 3:
        print('seleccionaste la opcion 3, salida del programa. ')
        return True
    elif usuario != 1 and usuario != 2:
        print('Ingrese un número válido (1 ,  2  o  3).')
        return False
    
    return True

def autentificacionDeUsuario(usuario, contraseña):
    if usuario in registros:
        if registros[usuario] == contraseña:
            return True
    return False