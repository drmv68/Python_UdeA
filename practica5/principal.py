from funciones import validacionDeDatoIngresado, autentificacionDeUsuario

yesOrNo = True

while yesOrNo:
    usuario = input('Seleccione .1- si usted es un usuario registrado .2- si desea el acceso de invitado, .3- si desea salir de la aplicaion: ')
    resultado = validacionDeDatoIngresado(usuario)

    if usuario == '3':
        break    
    else:
        yesOrNo = False


if usuario == '1':    
    yesOrNo = True
    while yesOrNo:
        documento = input('ingrese por favor numero de documento:  ')
        contraseña = input('ahora ingrese su contraseña:  ')
        autentificacionDeUsuario(documento, contraseña)
        
        if autentificacionDeUsuario:
            
            
            break