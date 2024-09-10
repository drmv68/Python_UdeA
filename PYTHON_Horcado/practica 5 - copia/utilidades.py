from datetime import datetime

def validar_nombre(nombre):
    '''
    Valida nombre válido
    '''
    booleano=''
    parametros_malos='1234567890+-.,:;-_<>@#$%&/()=?¡¡¿`!'
    for letras in nombre:
        if not letras in parametros_malos:
            letras=''
            booleano+=letras
        else:
            booleano+=letras
    
    if booleano=='':
        return True
    else:
        return False
    
def validar_documento(documento):
    '''
    Valida un número de documento. Debe contener 10 caracteres, todos numéricos.
    se valida que la variable booleano esta vacia para dar true o false.
    '''
    cont=0
    caracteres_validos='1234567890'
    documen=str(documento)
    for i in documen:
        if i in caracteres_validos:
            cont+=1
           
        else:
            cont=cont-1
    if cont==10 and len(documen)==10:
        return True
 
    else:
        return False
    

def imprimir_tabla(tabla, ancho, encabezado=None):  
    ''' 
    Imprime en pantalla un tabla con los datos pasados, ajustado a los tamaños deseados.
    separa en su respectivo orden hacia la derecha.
    '''
    def dividir_fila(ancho,sep='-'):
        '''
        ancho: Lista con el tamaño de cada columna
        sep: Caracter con el que se van a formar las líneas que 
            separan las filas
        '''
        linea = ''
        for i in range(len(ancho)):
            linea += ('+'+sep*(ancho[i]-1))
        linea = linea[:-1]+'+'
        print(linea)
        
    def imprimir_celda(texto, impresos, relleno):
        '''
        texto: Texto que se va a colocar en la celda
        impresos: cantidad de caracteres ya impresos del texto
        relleno: cantidad de caracteres que se agregan automáticamente,
            para separar los textos del borde de las celda.
        '''        
        if type(texto) == type(0.0):
            texto = '{:^7.2f}'.format(texto)
        else:
            texto = str(texto)
        texto = texto.replace('\n',' ').replace('\t',' ')
        if impresos+relleno < len(texto):
            print(texto[impresos:impresos+relleno],end='')
            impresos+=relleno
        elif impresos >= len(texto):
            print(' '*(relleno),end='')
        else:
            print(texto[impresos:], end='')
            print(' '*(relleno-(len(texto) - impresos)),end='')
            impresos = len(texto)
        return impresos
    
    def imprimir_fila(fila):
        '''
impresos: Esta variable se utiliza para almacenar la cantidad de caracteres ya impresos en cada celda.
alto: Esta variable se utiliza para almacenar la altura de la fila.
        '''
        impresos = []   
        alto = 1
        for i in range(len(fila)):
            impresos.append(0)
            if type(fila[i]) == type(0.0):
                texto = '{:7.2f}'.format(fila[i])
            else:
                texto = str(fila[i])
            alto1 = len(texto)//(ancho[i]-4)
            if len(texto)%(ancho[i]-4) != 0:
                alto1+=1
            if alto1 > alto:
                alto = alto1
        for i in range(alto):
            print('| ',end='')
            for j in range(len(fila)):
                relleno = ancho[j]-3
                if j == len(fila)-1:
                    relleno = ancho[j] -4
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' |')
                else:
                    impresos[j] = imprimir_celda(fila[j], impresos[j], relleno)
                    print(' | ',end='')   
                    """
Para cada celda, la función imprimir_celda() se utiliza para imprimir la celda, con el ancho especificado.
                    """
                    """
                    Estas líneas de código se utilizan para validar los parámetros de la función imprimir_tabla()
            """
    if not len(tabla) > 0:
        return
    if not type(tabla[0]) is list:
        return
    ncols = len(tabla[0])
    if type(ancho) == type(0):
        ancho = [ancho+3]*ncols 
    elif type(ancho) is list:
        for i in range(len(ancho)):
            ancho[i]+=3
    else:
        print('Error. El ancho debe ser un entero o una lista de enteros')
        return
    assert len(ancho) == ncols, 'La cantidad de columnas no coincide con los tamaños dados'
    ancho[-1] += 1
    if encabezado != None:
        dividir_fila(ancho,'=')
        imprimir_fila(encabezado)
        dividir_fila(ancho,'=')
    else:
        dividir_fila(ancho)
    for fila in tabla:
        imprimir_fila(fila)
        dividir_fila(ancho)

def archivos(archivo):
    """
    recibe el archivo 'registros_.txt'
    y retorna la información extraida en un diccionario, con otro diccionario anidado y en este una lista con la información
    """
    
    diccionario_usuarios={}
    diccionario_estaciones ={}
    municipios ={}
    diccionario_registro={}
    texto=open(archivo,'r')
    for linea in texto:
        if linea != '\n':
            if linea[0]=='<':
               
                usuario=(slipt(linea[1:-2],';'))
                diccionario_usuarios[usuario[0]]=usuario
            elif linea[0]==':':
                municipios=(slipt(linea[1:-1],','))
           
            elif linea[4]=='-':
                registros=(slipt(linea[0:-1], ';'))
                diccionario_registro[registros[2]]=registros
                
            elif linea[0]=='P':
                parametros=(slipt(linea[0:-1],';'))
            elif linea[1] or linea[2] or linea[3]==',':
                estaciones=(slipt(linea[0:-1],','))
                diccionario_estaciones[estaciones[0]]=estaciones
    texto.close()
                
    datos = {'Usuarios': diccionario_usuarios, 'Municipios': municipios, 'Estaciones': diccionario_estaciones, 'Registros': diccionario_registro}
    return datos      
      
def slipt(texto, separador):
    """
    funcion que recibe una cadena de caracteres y un carater que los separa(',','.','-',':',entre otros)
    retorna una lista con los elementos eliminados
    """
    cadena=[]
    cara=''
    for i in texto:
        if i==separador:
            cadena.append(cara)
            cara=''
        else:
            cara+=i
    cadena.append(cara)
    return cadena


def reemplazar_lista(lista, buscar, reemplazar_con):
    """
    Función que reemplaza una palabra de la lista por otra
    """
    lista_reemplazada = [reemplazar_con if elemento == buscar else elemento for elemento in lista]
    return lista_reemplazada

def elimina_lista(lista,posicion):
    """
    elimina una posicion de la lista.
    la función recibe una una lista, y la posicion que se desea eliminar;
    y retorna una lista con la posición eliminada
    """
    for i in range (posicion,len(lista)-1):
        lista[i]=lista[i+1]
        
    lista.pop(len(lista)-1)
        
    return lista
        
        
def validador_contraseña(contraseña):
    """
    valida la contraseña, utilizando la longitud permitida
    """
    longi=len(contraseña)
    if longi>=4:
        return True
    else:
        return False
    
def registrado():
    """
ejecuta todas las opciones del mennú,de registrados, invocando las funciones del admin y operador
    """
    ban=False
    contador=3
    documento=input('ingrese el documento: ')
    validador=validar_documento(documento)
    while validador==False:
        documento=input('ingrese un documento correcto: ')
        validador=validar_documento(documento)
        
        
    datos=archivos('registros_.txt')
    usuarios=datos['Usuarios']
    while ban==False:
        if documento in usuarios:
            ban=True
            contraseña=input('ingrese la contraseña: ')
            validador=validador_contraseña(contraseña)
            while validador==False:
                contraseña=input('digite una contraseña valida: ')
                validador=validador_contraseña(contraseña)
            while contador>0:
                
                if contraseña in usuarios[documento]:
                    
                    usuario=(usuarios[documento])
                    nombre=usuario[1]
                    rol=usuario[3]
                    print('bienvenido al sistema',nombre)
                    if rol=='Administrador':
                        
                        administrador()
                    elif rol=='Operador':
                        operador()
                    break
                else:
                    contraseña=input('contraseña no encontrada,ingrese una correcta: ')
                    validador_contraseña(contraseña)
                    validador=validador_contraseña(contraseña)
                    contador=contador-1
                    print('intentos permitidos',contador) 
            
                    while validador==False:
                        
                        contraseña=input('digite una contraseña valida: ')
                        validador=validador_contraseña(contraseña)
            
        else:
            documento=input('ingrese un documento registrado: ')
            ban==False
        
def administrador():
    """
    función que ejecuta las acciones de admin,
    mostrando un menu
    """
    caracter_validos='1','2','3','4'
    
    print('usted es admin')
    print('1.menú principal')
    print('2.gestionar estaciones')
    print('3.gestionar usuario')
    print('4.depuración de datos')
    opcion=input('ingrese una opcion: ')
    while not opcion in caracter_validos:
        opcion=input('ingrese una opcion valida: ')
    if opcion=='1':
        menu()
    elif opcion=='2':
        gestionar_estaciones()
        
    elif opcion=='3':
        gestionar_usuario()
    elif opcion=='4':
        print('depuración de datos')
        
def operador():
    """
    ejecuta las opciones de un operador
    muestra un menu con las opciones de operador
    """
    ban=False
    caracteres='1','2'
    datos=archivos('registros_.txt')
    estaciones=datos['Estaciones']
    municipios=datos['Municipios']
    print('usted es operador')

    print('1.seleccionar municipio')
    print('2.salir del sistema')
    opcion=input('ingrese una opción correcta: ')
    while not opcion in caracteres:
        opcion=input('ingrese una opción correcta: ')
    
    if opcion=='1':
        while ban==False:
            numeros=[]
            print('seleccionar municipio: ')
            print('Medellín,Bello,Itagüí,Caldas,La Estrella,Barbosa')
            municipio=input('ingrese el municipio: ')
            while True:
                if municipio in municipios:
                    break
                else:
                    municipio=input('ingrese un municipio correcto: ')
    
            lista_estacion=estaciones.values()           
            for lista in lista_estacion:

                if lista[2]==municipio:
                    
                    print('estacion', lista[0], lista[1],',', lista[2])
                    numeros+= lista[0]    
                
            print('1.escoger estación ')  
            print('2.cambiar de municipio')
            opcion1=input('escoja una opción: ')
            while not opcion1 in '12':
                opcion1=input('escoja una opción valida: ')
        
            if opcion1=='2':
                ban=False
                    
            elif opcion1=='1':
            
                opcion=input('escoja una estación por su número: ')
                while True:
                    if opcion in numeros:
                        break
                    else:
                        opcion=input('ingrese un número de estación correcto: ')
                        
                ban=True
                mostrar_registros(opcion)
    
    elif opcion=='2':
        
        menu()
      
def mostrar_registros(numero_estacion):
    encabezado=['fecha','estación','medidas']
    a=[]
    datos=archivos('registros_.txt')
    registros=datos['Registros']
   
    lista_registros=registros.values()
    for regis in lista_registros:
        
        if regis[1]==numero_estacion:
            a.append(regis)
    print('PARAMETROS DE MEDIDA: ')        
    print(' PM10[0.0:100.0,ug/m3];PM25[0.0:200.0,ug/m3];Temperatura[-20.0:50.0,°C];Humedad[0.0:100.0,%]')
            
    imprimir_tabla(a, 25,encabezado)
    crear_medida(numero_estacion)
    
def crear_medida(numero_estacion):
    diccio_nuevo={}
    datos=archivos('registros_.txt')
    registros=datos['Registros']
    caracteres='1','2'
    print('1.volver al menú: ')
    print('2.añadir medida: ')
    opcion=input('ingrese una opción: ')
    while not opcion in caracteres:
        opcion=input('ingrese una opcion valida: ')
    if opcion=='1':
        operador()
    elif opcion=='2':
        print('PM10= (desde 0.0 hasta 100.0 ug/m3)')
        PM10=float(input('ingrese la PM10: '))
        while True:
            if PM10>0.0 and PM10<100.0  or 'ND':
                break
            else:
                PM10=float(input('ingrese un valor en el rango establecido: '))
        print('PM25=(desde 0.0 hasta 200.0 ug/m3)')
        PM25=float(input('ingrese la PM25: '))
        while True:
            if PM25>0.0 and PM25<200.0:
               
                
                break
            else:
                PM25=float(input('ingrese un valor en el rango establecido: '))
        print('temperatura= (desde los -20.0 hasta los 50.0 °C)')
        temperatura=float(input('ingrese la temperatura: '))
        while True:
            if temperatura>-20.0 and temperatura<50.0 or 'ND':
                break
            else:
                temperatura=float(input('ingrese un valor en el rango establecido: '))
        print('humedad= (0.0 hasta 100.0%)')
        humedad=float(input('ingrese la humedad: '))
        while True:
            if humedad>0.0 and humedad<100.0 or 'ND':
                break
            else:
                humedad=float(input('ingrese un valor en el rango establecido: '))
        ti=datetime.now()  
        tiempo=datetime.strftime(ti, '%Y-%m-%d %H:%M:%S')
        PM10=str(PM10)
        PM25=str(PM25)
        temperatura=str(temperatura)
        humedad=str(humedad)
      
        medida='{'+ PM10 + ',' + PM25 + ',' + temperatura + ',' + humedad+ '}'
       
        diccio_nuevo={medida:[tiempo,numero_estacion,medida]}
        print(diccio_nuevo)
       
        datos['Registros'].update(diccio_nuevo) 
        cargar_datos(datos)
        operador()
        
def visitante():
    """
    función que ejecuta las opciones de un visitante,
    muestra un menú con las opciones de un visitante
    """
    caracteres='1','2'
    print('usted es visitante')
    print('1.ver estadisticas')
    print('2.ir al menú principal')
    opcion=input('ingrese una opción: ')
    while not opcion in caracteres:
        opcion=input('ingrese una opción correcta: ')
    if opcion=='1':
        estadisticas()
    
    elif opcion=='2':
        menu()
        
def estadisticas():
    
    """
   imprime las estadisticas a los visitantes
    """
    
    datos=archivos('registros_.txt')
    registros=datos['Registros']
    estaciones=datos['Estaciones']
    escoger=estaciones.values()
    for i in escoger:
        estacion = i[0]
        lugar=i[1]
        municipio=i[2]
        print(estacion, lugar, municipio)
          
    
    numero=input('ingrese el número de la estación: ')
    encabezado=['fecha','estación','medidas']
    a=[]
    lista_registros=registros.values()
    for regis in lista_registros:
        
        if regis[1]==numero:
            a.append(regis)
            
    print('PARAMETROS DE MEDIDA: ')        
    print(' PM10[0.0:100.0,ug/m3];PM25[0.0:200.0,ug/m3];Temperatura[-20.0:50.0,°C];Humedad[0.0:100.0,%]')
                
    imprimir_tabla(a, 25,encabezado)
    visitante()
      
def menu():
    """
    invoca un menu como el del main, se invoca para volver de nuevo al menu en las opciones de administrador, operador y visitante
    
    """
    print('MENÚ')


    print('1.usuario visitante')
    print('2.usuario registrado')
    print('3.salir del sistema')
    opcion=(input('seleccione una opción: '))
    caracter_validos='1','2','3'
    
    
    while not opcion in caracter_validos:
        opcion=(input('ingrese un caracter correcto: '))
    if opcion=='1':  
        visitante()
    elif opcion=='2': 
        print('usted es registrado')
        registrado()    
    elif opcion=='3':                         
        print('')
        
def gestionar_estaciones():
    """
    función que da paso a las acciones que puede hacer el administrador en referencia a las estaciones
    """
    print('gestionar estaciones')
    caracter_validos='1','2','3','4'
    print('1.crear estación')
    print('2.editar estación')
    print('3.eliminar estación')
    print('4.volver al menú')
    opcion=input('ingrese una opción: ')
    datos=archivos('registros_.txt')
    while not opcion in caracter_validos:
        opcion=input('ingrese una opción correcta: ')
    if opcion =='1':
        print('crear estación')
        municipios='Medellín','Itagüí','Caldas','La Estrella','Barbosa','Bello'
        print(municipios)
        municipio=input('seleccione un municipio: ')
        while not municipio in municipios:
            municipio=input('error, copie el municipio correctamente: ')
        nombre_estacion=input('ingrese el nombre de la estación: ')
        validador= validar_nombre(nombre_estacion)
        while validador==False:
            nombre_estacion=input('ingrese un nombre de estación correcto: ')
        crear_estacion(nombre_estacion, municipio)
                   
    elif opcion=='2':
        print('editar estación')
        editar_estacion()
            
    
    elif opcion=='3':
      
        eliminar_estacion()
    elif opcion=='4':
        menu()
 
    
def eliminar_estacion():
    """
    elimina le estacion del sistema
    """
    
    
    lista_estaciones=[]
    lista_registros=[]
    datos=archivos('registros_.txt')
    registros=datos['Registros']
    estaciones=datos['Estaciones']
    numero=input('ingrese el número de la estación: ')
    registros=registros.values()
    
    for linea in registros:
        if linea[1]==numero:
            print('la estación tiene información, no se puede borrar')
            print('repetida',linea)
            gestionar_estaciones()
    
    datos['Estaciones'].pop(numero)
    cargar_datos(datos)
  
def editar_estacion() :
    """
    edita las estaciones  elegidas por el usuario
    """
    municipios='Medellín','Itagüí','Caldas','La Estrella','Barbosa','Bello'
    datos=archivos('registros_.txt')
    estaciones=datos['Estaciones']
    numero=input('ingrese el número de la estación a cambiar: ')
    while True:
        if numero in '1234567890'and numero in estaciones:
            break
        
        else:
            numero=input('ingrese un número valido: ')
    estacion_cambiar=estaciones[numero]
    print(estacion_cambiar)
    nombre_antiguo=estacion_cambiar[1]
    municipio_antiguo=estacion_cambiar[2]
    
    print('que desea cambiar?')
    print('1.nombre')
    print('2.municipio')
    opcion=input('ingrese una opcion: ')
    while not opcion in '12':
        opcion=input('escriba una nueva opción: ')
    if opcion=='1':
        nombre=input('ingrese el nombre: ')
        validador=validar_nombre(nombre)
        while validador==False:
            nombre=input('ingrese un nombre correcto: ')
            validador=validar_nombre(nombre)
    
        lista_reemplazada=reemplazar_lista(estacion_cambiar, nombre_antiguo, nombre)
        datos['Estaciones'].update({numero:lista_reemplazada})  
        menu_edicion(datos)
        
    elif opcion=='2':
        print(municipios)
        municipio=input('ingrese el municipio nuevo: ')
        validador=validar_nombre(municipio)
        while True:
            if municipio in municipios and validador==True:
                break
            else:
                print(municipios)
                municipio=input('ingrese un municipio correcto: ')
        
        lista_reemplazada=reemplazar_lista(estacion_cambiar, municipio_antiguo, municipio)
        datos['Estaciones'].update({numero:lista_reemplazada})  
        menu_edicion(datos)
        
def crear_estacion(nombre,municipio):
    
    """
crea la estacion nueva; tiene como parametros el nombre de la estación y su municipio

    """
    print(nombre,',',municipio)
    datos=archivos('registros_.txt')
    estaciones=datos['Estaciones']
    clave_ultima=int(list(estaciones.keys())[-1])
    clave_final=str(clave_ultima+1)
    estacion_nueva={clave_final:[clave_final,nombre,municipio]}
    datos['Estaciones'].update(estacion_nueva) 
    cargar_datos(datos)
    administrador()
        
def gestionar_usuario():
    """
    funcion que da paso a las acciones que puede hacer el administrador en referencia al usuario
    
    """
    datos=archivos('registros_.txt')
    usuarios=datos['Usuarios']
    caracter_validos='123'
    print('1.crear usuario')
    print('2.editar usuario')
    print('3.eliminar usuario')
    opcion=input('ingrese una opción: ')
    while not opcion in caracter_validos:
        opcion=input('ingrese una opción correcta: ')
    if opcion =='1':
        print('crear usuario')
        while True:
            documento=input('ingrese el documento: ')
            validador1=validar_documento(documento)
            if validador1==True:
                if not documento in usuarios:
             
                    break
            else:
                print('documento invalido, ingrese uno nuevo')
        while True:
            nombre=input('ingrese el nombre nuevo: ')
            validador2=validar_nombre(nombre)
            if validador2==True:
                break
            else:
                print('ingrese un nombre adecuado')
            
        while True:
            contraseña=input('ingrese una contraseña: ')
            validador3=validador_contraseña(contraseña)
            if validador3==True:
                
                cont=input('verifique su contraseña: ')
                while not contraseña==cont:
                    cont=input('ingrese la misma contraseña: ')
                    
                break
            else:
                print('ingrese una contraseña valida: ')
     
        print('escoja un rol')
        print('1.administrador')
        print('2.Operador')
        rol=input('ingrese un rol: ')
        while not rol in '12':
            rol=input('escoja una opción correcta: ')
        if rol=='1':
            rol='Administrador'
        elif rol=='2':
            rol='Operador'
        
        crear_usuario(documento, nombre, contraseña, rol)
        
    elif opcion=='2':
        print('editar usuario')
        editar_usuario()
        
    elif opcion=='3':
        print('eliminar usuario')
        documento_admin=input('ingrese otra vez su documento de administrador: ')
        while True:
            
            if documento_admin in usuarios:
                break
            else:
                documento_admin=input('ingrese otra vez su documento: ')
               
        
        documento_eliminar=input('ingrese el documento del usuario a eliminar: ')
        while True:
            if documento_eliminar in usuarios:
                break
            
            
            else:
                documento_eliminar=input('ingress un documento correcto: ')
        
        while True:
            if documento_admin==documento_eliminar:
                documento_eliminar=input('no se puede eliminar el documento en sección: ')
            else:
                break
        datos['Usuarios'].pop(documento_eliminar)
        menu_edicion(datos)
        
def menu_edicion(archivo):
    """
menú invocado al haber finalizado la edición de algo
    """  

    print('ejecucción finalizada')
    print('1.volver al menú') 
    print('2.salir del sistema')
    opcion=input('ingrese una opción: ')
    while not opcion in '12':
        opcion=input('ingrese una opción valida: ')
    if opcion=='1':
        cargar_datos(archivo)
        administrador()
    else:
        cargar_datos(archivo)
    
def editar_usuario():
    """
    
hace las ediciones del usuario,ya sea su rol,nombre o clave
    """
    archivo=archivos('registros_.txt')
    usuarios=archivo['Usuarios']
    usuario=input('ingrese el documento del usuario a cambiar: ')

    while True:
        if usuario in usuarios:
            
            break
        else:
            usuario=input('ingrese un documento correcto: ')
    usuario_cambiar=usuarios[usuario]
    nombre_antiguo=usuario_cambiar[1]
    contraseña_antigua=usuario_cambiar[2]
    rol_antiguo=usuario_cambiar[3]
    print('el usuario es ',usuario_cambiar[1],'su clave es ',usuario_cambiar[2],'y su rol es',usuario_cambiar[3])
    print('que desea cambiar? ')
    print('1.nombre')
    print('2.clave')
    print('3.rol')
    opcion=input('ingrese la opción: ')
    while not opcion in '123':
        opcion=input('ingrese una opción correcta: ')
    if opcion=='1':
        nombre=input('ingrese el nuevo nombre: ')
        validador=validar_nombre(nombre)
        while True:
            if validador==True:
                break
            else:
                nombre=input('ingrese un nombre valido: ')
                validador=validar_nombre(nombre)
        lista_reemplazada=reemplazar_lista(usuario_cambiar, nombre_antiguo, nombre)
        archivo['Usuarios'].update({usuario:lista_reemplazada})  
        menu_edicion(archivo)
    
    elif opcion=='2':  
        clave=input('ingrese la nueva clave: ')
        validador=validador_contraseña(clave)
        while True:
            if validador==True:
                break
            else:
                clave=input('ingrese una clave correcta: ')
                
        clavex=input('verificación de clave, ingresela de nuevo: ')
        while not clavex==clave:
            clavex=input('ingrese la clave ya utilizada: ')
            
        
        lista_reemplazada=reemplazar_lista(usuario_cambiar,contraseña_antigua , clave)
        archivo['Usuarios'].update({usuario:lista_reemplazada})  
        menu_edicion(archivo)
    elif opcion=='3':
        print('1.administrador')
        print('2.operador')
        rol=input('ingrese una opción: ')
        while not rol in '12':
            rol=input('ingrese una opcion correcta: ')
        if rol=='1':
            rol='Administrador'
        elif rol=='2':
            rol='Operador'
        
        lista_reemplazada=reemplazar_lista(usuario_cambiar, rol_antiguo, rol)
        archivo['Usuarios'].update({usuario:lista_reemplazada})  
        menu_edicion(archivo)

def crear_usuario(documento,nombre,contraseña,rol):
    """
    crea el nuevo usuario 

    """
    print(documento,nombre,contraseña,rol)
    datos=archivos('registros_.txt')
    usuarios=datos['Usuarios']
    lista_nuevo=[]
    diccio_nuevo={}
    lista_nuevo=[documento,nombre,contraseña,rol]
    diccio_nuevo[documento]=lista_nuevo
    usuarios.update(diccio_nuevo)
    cargar_datos(datos)
    
    print('1.menú Administrador')
    print('2.salir del sistema')
    opcion=input('ingrese una opción: ')
    while not opcion in '12':
        opcion=input('ingrese una opción correcta')
    if opcion=='1':
        administrador()
    elif opcion=='2':
        print('')
        
        
def cargar_datos(datos):
    """
    carga todos los datos modificados al archivo txt
    """
    usu_nuevos=''
    esta_nuevos=''
    regis_nuevos=''
    muni_nuevos=''
  
    usuarios=datos['Usuarios']
    estaciones=datos['Estaciones']
    registros=datos['Registros']
  
    valores_usu= usuarios.values()
    for posi in valores_usu:
        docu=posi[0]
        nomb=posi[1]
        clave=posi[2]
        traba=posi[3]
        usu='<'+docu+';'+nomb+';'+clave+';'+traba+'>'+'\n'
        
        usu_nuevos=usu_nuevos+usu
    
    muni_nuevos= ':Medellín,Bello,Itagüí,Caldas,La Estrella,Barbosa'+'\n'
   
  
    valores_estaciones=estaciones.values()
    for posi in valores_estaciones:
        valor=posi[0]
        lugar=posi[1]
        municipio=posi[2]
        esta=valor+','+lugar+','+municipio+'\n'
        
        esta_nuevos=esta_nuevos+esta
  
    
    parametros='PM10[0.0:100.0,ug/m3];PM25[0.0:200.0,ug/m3];Temperatura[-20.0:50.0,°C];Humedad[0.0:100.0,%]'+'\n'
   
    valores_regis=registros.values()
    for posi in valores_regis:
       fecha=posi[0]
       estacion=posi[1]
       medidas=posi[2]
       regis=fecha+';'+estacion+';'+medidas+'\n'
        
       regis_nuevos=regis_nuevos+regis
  
    
    datos_nuevos=usu_nuevos+'\n'+muni_nuevos+'\n'+esta_nuevos+'\n'+parametros+'\n'+'\n'+regis_nuevos
    texto0=open('registros_.txt','w')
    texto0.write(datos_nuevos)
    