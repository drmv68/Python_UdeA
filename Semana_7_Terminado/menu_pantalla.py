"""
Aqui se imprimiran los menus de pantalla
"""
def salir_sistema():
    print("Estas apunto de salir del sitema, ¿Quieres hacerlo?")
    print("1. Si")
    print("2. No")
    
    while True:
        try:
            print("\n")
            opcion_perfi_usu = int(input("Seleciones una opcion: "))
            if 1 <= opcion_perfi_usu <= 2:
                print("\n")
                if opcion_perfi_usu == 1:
                    return opcion_perfi_usu
                else:
                    return opcion_perfi_usu
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
            
def pantalla_inicio():
    print("1. Administrar cursos")
    print("2. Administrar estudiantes")
    print("3. Administrador de notas")
    print("4. Salir del sistema")
    print("\n")
    
    while True:
        try:
            selecInterfaz = int(input("Selecciona una de las opciones: "))
            if 1 <= selecInterfaz <= 4:
                print("\n"*2)
                return selecInterfaz
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
            
def pantalla_administrar_cursos():
    print("1. Agregar curso")
    print("2. Eliminar curso")
    print("3. Volver al menu anterior")
    print("\n")
    
    while True:
            try:
                selecInterfaz = int(input("Selecciona una de las opciones: "))
                if 1 <= selecInterfaz <= 3:
                    print("\n"*2)
                    return selecInterfaz
                else:
                    print("El valor es incorrecto")
            except ValueError:
                print("Valor no valido, verifique porfavor")
                
def pantalla_administrar_estudiantes():
    print("1. Agregar estudiante")
    print("2. Eliminar estudiante")
    print("3. Volver al menu anterior")
    print("\n")
    
    while True:
            try:
                selecInterfaz = int(input("Selecciona una de las opciones: "))
                if 1 <= selecInterfaz <= 3:
                    print("\n"*2)
                    return selecInterfaz
                else:
                    print("El valor es incorrecto")
            except ValueError:
                print("Valor no valido, verifique porfavor")
                
def pantalla_administrardor_de_notas():
    print("1. Editar notas")
    print("2. Visualizar notas")
    print("3. Volver al menu anterior")
    print("\n")
    
    while True:
            try:
                selecInterfaz = int(input("Selecciona una de las opciones: "))
                if 1 <= selecInterfaz <= 3:
                    print("\n"*2)
                    return selecInterfaz
                else:
                    print("El valor es incorrecto")
            except ValueError:
                print("Valor no valido, verifique porfavor")
    
def pantalla_elegir_curso(cursos):
    i = 1
    contador = 0
    for curso in cursos:
        if contador == (len(cursos)-1):
            curso = curso.replace("\n", "")
        print(i, ". ", "".join(curso.replace(" ", "")))
        i += 1
        contador += 1
    print(i, ". Volver al menu principal")
    print("\n")
    while True:
        try:
            selec_curso = int(input("Selecione el curso a eliminar: "))
            print("\n")
            if 1 <= selec_curso <= len(cursos):
                print("\n")
                return selec_curso
            elif selec_curso == i:
                return "s"
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")

def pantalla_mostrar_notas():
    print("1. Promedio por estudiante")
    print("2. Promedio por cursos")
    print("3. Tres mayores notas por curso")
    print("4. Menor nota de estudiante")
    print("5. Ordenar promedios estudiantes")#Calcular la posición en la lista de promedios
    print("6. Ordenar estudiantes por cantidad de cursos")
    print("7. Ordenar cursos según cancelaciones")
    print("8. Volver al menu principal")
    
    print("\n")
    
    while True:
        try:
            selec_curso = int(input("Seleccione una opcion: "))
            print("\n")
            if 1 <= selec_curso <= 7:
                print("\n")
                return selec_curso
            elif selec_curso == 8:
                return "s"
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
                
def seleccionar_documento(documentos):
    i = 0
    contador = 1
    while i != len(documentos):
        print(f"{contador}. {documentos[i]} ")
        contador += 1
        i += 1
    print(f"{contador}. Volver al menu principal")
    print("\n")
    
    
    while True:
        try:
            selec_documento = int(input("Selecione el estudiante a eliminar: "))
            print("\n")
            pos_doc = (selec_documento)-1
            if selec_documento <= (len(documentos)):
                documento = documentos[pos_doc]
            if 1 <= selec_documento <= len(documentos):
                print("\n")
                return documento
            elif selec_documento == (len(documentos)+1):
                return "s"
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
        
def seleccionar_curso(cursos):
    i = 1
    contador = 0
    for curso in cursos:
        if contador == (len(cursos)-1):
            curso = curso.replace("\n", "")
        print(i, ". ", "".join(curso.replace(" ", "")))
        i += 1
        contador += 1
    print(i, ". Volver al menu principal")
    print("\n")
    while True:
        try:
            selec_curso = input("Selecione una de las opciones: ")
            print("\n")
            pos_curso = (int(selec_curso)-1)
            if int(selec_curso) <= (len(cursos)):
                curso = cursos[pos_curso]
            if 1 <= int(selec_curso) <= len(cursos):
                print("\n")
                return curso.replace(" ", "")
            elif int(selec_curso) == i:
                return "s"
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
    
def nueva_nota():
    while True:
        try:
            nota = input("Ingresa la nueva nota: ")
            if float(nota) == -1.0 or float(nota) == -2.0:
                nota == int(nota)
                return nota
            elif 0.0 < float(nota) <= 5.0:
                return nota
            else:
                print("Nota fuera de rango(0 - 5)")
        except ValueError:
            print("Valor no valido, verifique porfavor")
        
def volver():
    while True:
        try:
            print("\n")
            selec_medida = int(input("Selecione 1 para volver: "))
            if 1 == selec_medida :
                print("\n")
                return selec_medida
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
            
def elegir_estudiante(documentos):
    contador = 1 
    for documento in documentos:
        print(contador, ". ", documento)
        contador += 1
    print(contador, ". Volver al menu principal")
    while True:
        try:
            selec_curso = input("Selecione una opcion: ")
            print("\n")
            if int(selec_curso) == contador:
                return "s"
            elif 1 <= int(selec_curso) <= len(documentos):
                print("\n")
                return documentos[(int(selec_curso)-1)]
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")
            
def elegir_metodo():
    print("1. Seleccionar estudiante")
    print("2. Buscar estudiante manualmente")
    print("3. Volver al menu anterior")
    print("\n")
    
    while True:
        try:
            selec_curso = int(input("Seleccione una opcion: "))
            print("\n")
            if 1 <= selec_curso <= 3:
                print("\n")
                return selec_curso
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")