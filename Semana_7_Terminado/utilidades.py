def obtener_cursos(archivo):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz"
    cursos = []
    with open(archivo, "r") as archivo:
        for linea in archivo:
            if linea[0] in alfabeto:
                linea = linea.strip("\n")
                cursos_aux = linea.split(",")
                cursos.append(cursos_aux)
            else:
                break
    return cursos[0]

def obtener_documentos(archivo):
    numeros = []
    with open(archivo, "r") as archivo:
        for linea in archivo:
            numero_actual = ""
            for caracter in linea:
                if caracter.isdigit():
                    numero_actual += caracter
                elif numero_actual and 7 <= len(numero_actual) <= 10:
                    numeros.append(numero_actual)
                    numero_actual = ""
                else:
                    numero_actual = ""

    return numeros
        
def obtener_notas(archivo):
    notas = []
    with open(archivo, "r") as f:
        lineas = f.readlines()
        for linea in lineas[3:]:
            valores = [float(valor) for valor in linea.split()]
            notas.append(valores)
        return notas
    
    
def agregar_curso(curso,notas,archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        
        salida = ""
        for i in range(len(lineas)):
            if i == 0:
                aux = lineas[i].replace('\n','')
                salida += f"{aux}, {curso}" + '\n'
            elif i == 1:
                salida += lineas[i]
            else:
                salida += lineas[i].replace("\n","").strip() + " " + str(notas[i-2]) + "\n"
    print("\n")
    print("Curso y respectivas notas guardadas con exito!")
    print("\n")
    with open(archivo, "w") as f:
        f.write(salida.strip())
        
def capturar_cursos(documentos):
    aux = []
    for documento in documentos:
        i = 0
        while i == 0:
            print(f"Ingrese la nota del estudiante {documento} :", end = "")
            try:
                nota = input(" ")
                if float(nota) == -1.0 or float(nota) == -2.0:
                    nota == int(nota)
                    aux.append(nota)
                    i = 1
                elif 0.0 < float(nota) <= 5.0:
                    aux.append(nota)
                    i = 1
                else:
                    print("Nota fuera de rango(0 - 5)")
            except ValueError:
                print("Valor no valido, verifique porfavor")
    return aux
    
def eliminar_curso(curso,archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        salida = ""
        for i in range(len(lineas)):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
                for j in range(len(cursos)):
                    if cursos[j] == curso:
                        cursos.pop(j)
                        break
                
                salida += ", ".join(cursos) + "\n"
            elif i == 1:
                salida += lineas[i]
            else:
                notas = lineas[i].replace("\n", "").split(" ")
                notas.pop(j)
                salida += " ".join(notas) + "\n"
    print("El curso y sus notas respectivas se han eliminado correctamente!")
    print("\n")
    with open(archivo, "w") as f:
        f.write(salida.strip())
        
def agregar_estudiante(archivo, documentos):
    aux = 0
    while aux == 0:
        try:
            documento = input("Ingresa el documento del estudiante que se va a ingresar: ")
            if documento.isdigit() and 7 < len(documento) <= 10:
                aux = 1
            else:
                print("Número inválido")
        except ValueError:
            print("Valor no válido, verifique por favor")
    if documento in documentos:
        return "s"
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    lineas[1] = lineas[1].strip() + f' {documento}\n' #modifica segunda linea

    with open(archivo, 'w') as f:
        f.writelines(lineas)
        return documento
    
    
   
def capturar_notas_estudiante(documento, cursos, archivo):#añadir notas estudiante
    aux = []
    v = len(cursos)
    contador = 0
    while contador != v:
        curso = cursos[contador].strip()
        print(f"Ingrese la nota numero {curso} del estudiante {documento} :", end = "")
        try:
            nota = input(" ")
            if float(nota) == -1.0 or float(nota) == -2.0:
                nota == int(nota)
                new_nota = f"{nota} "
                aux.append(new_nota)
                contador += 1
            elif 0.0 < float(nota) <= 5.0:
                nota = float(nota)
                new_nota = f"{nota} "
                aux.append(new_nota)
                contador += 1
            else:
                print("Nota fuera de rango(0 - 5)")
        except ValueError:
            print("Valor no valido, verifique porfavor")
            
    with open(archivo, 'a') as f:
        f.writelines("\n")
        f.writelines(aux)
        print("\n"*2)
        print("Estudiante y sus notas correspondientes agregadas con exito!")
        print("\n"*2)

def eliminar_estudiante(documento, archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        salida = []
        cantidad = len(lineas)
        for i in range(cantidad):
            if i == 0:
                salida.append(lineas[i].strip())
            elif i == 1:
                estudiantes = lineas[i].split()
                for j in range(len(estudiantes)):
                    if estudiantes[j] == documento:
                        break
                estudiantes.pop(j)
                salida.append(" ".join(estudiantes))
            else:
                if i != (j+2):
                    salida.append(lineas[i].strip())
    print("\n")
    print("Estudiante eliminado con exito!")
    print("\n")
    with open(archivo, "w") as f:
        f.write("\n".join(salida))
                    
def editar_notas(documento, curso, archivo, nota): #nueva nota, documentodel estudiante a modificar
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        salida = ""
        for i in range(cantidad):
            if i == 0:
                salida += lineas[i]
                cursos = lineas[i].replace("\n", "").split(", ")
                for j in range(len(cursos)): #j columnas del curso
                    if cursos[j] == curso:
                        break
            elif i == 1:
                salida += lineas[i]
                estudiantes = lineas[i].split()
                for k in range(len(estudiantes)):# k + 2 linea donde se ubica el estudiante
                    if estudiantes[k] == documento:
                        break
            else:
                if i == (k+2):
                    notas = lineas[i].split()
                    notas[j] = nota
                    salida += " ".join(notas) + "\n"
                else:
                    salida += lineas[i]
    print("\n")
    print("Nota editada con exito!")
    print("\n")
    with open(archivo, "w") as f:
        f.write(salida.strip())
        
def promedio_estudiante(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        doc= "Documento"
        prom = "Promedio"
        posicion = "N°"
        print("_"*36)
        print(f"|{posicion:4s} | {doc:15s} | {prom:>10s}|")
        print("-"*36)
        contador = 1
        for i in range(cantidad):
            if i == 1:
                estudiantes = lineas[i].split()
            elif i > 1:
                notas = lineas[i].split()
                suma = 0
                canti = 0
                for nota in notas:
                    if not(nota == "-1" or nota == "-2"):
                        suma += float(nota)
                        canti += 1
                promedio = (suma/canti)
                print(f"|{str(contador):4s} | {estudiantes[i-2]:15s} | {promedio:10.2f}|")
                print("_"*36)
                contador += 1
    print("\n"*2)
   
#Optimizado             
def promedio_cursos(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        cur= "Curso"
        prom = "Promedio"
        posicion = "N°"
        print("_"*36)
        print(f"|{posicion:4s} | {cur:15s} | {prom:>10s}|")
        print("-"*36)
        for i in range(cantidad):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
                val = len(cursos)
                sumas = [0 for x in range(val)]
                canti = [0 for x in range(val)]
                
            elif i > 1:
                notas = lineas[i].split()
                for j in range(len(notas)):
                    if not(notas[j] == "-1" or notas[j] == "-2"):
                        sumas[j] += float(notas[j])
                        canti[j] += 1
        contador = 1
        for i in range(val):
            promedio = (sumas[i]/canti[i])
            print(f"| {str(contador):4s} | {cursos[i]:15s} | {promedio:10.2f}|")
            print("_"*36)
            contador +=1
    print("\n"*2)
   

#Optimizado
def tres_notas(archivo, curso):  
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        estu = "Estudiantes"
        prom = "Promedio"
        posicion = "N°"
        aux = curso.center(34)
        print("_"*36)         
        print(f"|{aux}|")
        print("_"*36)
        print(f"|{posicion:4s} | {estu:15s} | {prom:>10s}|")
        print("-"*36)
        notas_curso = []
        for i in range(cantidad):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
                indice_curso = cursos.index(curso)
            elif i == 1:
                estudiantes = lineas[i].split()
            else:
                notas = lineas[i].split()
                nota = notas[indice_curso]
                if not(nota == "-1" or nota == "-2"):
                    notas_curso.append((estudiantes[i-2], float(nota)))
        for i in range(1, len(notas_curso)):
            key = notas_curso[i]
            j = i - 1
            while j >= 0 and key[1] > notas_curso[j][1]:
                notas_curso[j + 1] = notas_curso[j]
                j -= 1
            notas_curso[j + 1] = key
        contador = 1
        for i, (estudiante, nota) in enumerate(notas_curso[:3]):
            print(f"|{str(contador):4s} | {estudiante:15s} | {nota:10.2f}|")
            print("_"*36)
            contador += 1
    print("\n"*2)

#Optimizado
def promedio_estudiante_ordenado(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        doc= "Documento"
        prom = "Promedio"
        posicion = "N°"
        print("_"*36)
        print(f"|{posicion:4s} | {doc:15s} | {prom:>10s}|")
        print("-"*36)
        promedios = []
        for i in range(cantidad):
            if i == 1:
                estudiantes = lineas[i].split()
            elif i > 1:
                notas = lineas[i].split()
                suma = 0
                canti = 0
                for nota in notas:
                    if not(nota == "-1" or nota == "-2"):
                        suma += float(nota)
                        canti += 1
                promedio = (suma/canti)
                promedios.append((estudiantes[i-2], promedio))
        
        # Ordenamiento de burbuja
        n = len(promedios)
        for i in range(n):
            for j in range(0, n-i-1):
                if promedios[j][1] < promedios[j+1][1] :
                    promedios[j], promedios[j+1] = promedios[j+1], promedios[j]
        
        contador = 1
        for estudiante, promedio in promedios:
            print(f"|{str(contador):4s} | {estudiante:15s} | {promedio:10.2f}|")
            print("_"*36)
            contador += 1
    print("\n"*2)
    print("Acontinuacion seleccione la posicion en el que esta el estudiante en la tabla o presione la tecla enter para salir")
    while True:
        try:
            selec_estu = input("Selecione una opcion: ")
            print("\n")
            if selec_estu == "":
                return "s", None
            elif 1 <= int(selec_estu) <= len(promedios):
                print("\n")
                return promedios[int(selec_estu)-1], selec_estu
            else:
                print("El valor es incorrecto")
        except ValueError:
            print("Valor no valido, verifique porfavor")

def curso_menor_nota(archivo, documento):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        menor_nota = float('inf')  # Inicializamos la menor nota como infinito
        curso_menor = None  # Inicializamos el curso de la menor nota como None
        for i in range(cantidad):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
            elif i == 1:
                estudiantes = lineas[i].split()
            else:
                notas = lineas[i].split()
                if estudiantes[i-2] == documento:  # Si encontramos al estudiante
                    for j in range(len(notas)):
                        nota = notas[j]
                        if nota != "-1" and nota != "-2" and float(nota) < menor_nota:
                            menor_nota = float(nota)
                            curso_menor = cursos[j]
        print(f"El curso con nota mas baja del estudiante {documento} es {curso_menor}")
        
        
#Optimizado
def ordenar_estudiantes(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        estudiantes_cursos = []
        for i in range(cantidad):
            if i == 1:
                estudiantes = lineas[i].split()
            elif i > 1:
                notas = lineas[i].split()
                canti = 0
                for nota in notas:
                    if not(nota == "-1" or nota == "-2"):
                        canti += 1
                estudiantes_cursos.append((estudiantes[i-2], canti))
        
        # Ordenamiento por selección
        for i in range(len(estudiantes_cursos)):
            min_idx = i
            for j in range(i+1, len(estudiantes_cursos)):
                if estudiantes_cursos[min_idx][1] < estudiantes_cursos[j][1]:
                    min_idx = j
            estudiantes_cursos[i], estudiantes_cursos[min_idx] = estudiantes_cursos[min_idx], estudiantes_cursos[i]
        
        # Imprimir estudiantes ordenados
        aux = "Estudiantes ordenados por cantidad de cursos"
        estu = "Estudiantes"
        cur = "Cantidad de cursos"
        print("_"*47)
        print(f"|{aux:46s}|")
        print("-"*47)
        print(f"|{estu:23s} | {cur:20s}|")
        print("_"*47)
        for estudiante, cursos in estudiantes_cursos:
            print(f"|{str(estudiante):23s} | {str(cursos):20s}|")
            print("_"*47)

#Optimizado
def ordenar_cursos(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        cursos_cancelaciones = []
        for i in range(cantidad):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(" ")
                cancelaciones = [0] * len(cursos)
            elif i > 1:
                notas = lineas[i].split()
                for j in range(len(notas)):
                    if notas[j] == "-1":
                        cancelaciones[j] += 1
        for i in range(len(cursos)):
            cursos_cancelaciones.append((cursos[i].replace(",", ""), cancelaciones[i]))
        
        # Ordenamiento por selección
        for i in range(len(cursos_cancelaciones)):
            max_idx = i
            for j in range(i+1, len(cursos_cancelaciones)):
                if cursos_cancelaciones[max_idx][1] < cursos_cancelaciones[j][1]:
                    max_idx = j
            cursos_cancelaciones[i], cursos_cancelaciones[max_idx] = cursos_cancelaciones[max_idx], cursos_cancelaciones[i]
        
        # Imprimir cursos ordenados
        aux = "Cursos ordenados por cantidad de cancelaciones"
        cur = "Curso"
        can = "Cantidad de cancelaciones"
        print("_"*60)
        print(f"|{aux:59s}|")
        print("-"*60)
        print(f"|{cur:28s} | {can:28s}|")
        print("_"*60)
        for curso, cancelaciones in cursos_cancelaciones:
            print(f"|{curso:28s} | {str(cancelaciones):28s}|")
            print("_"*60)
