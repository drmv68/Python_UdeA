#Optimizacion 1
"""
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
                
        
        promedios.sort(key=lambda x: x[1], reverse=True)
        contador = 1
        interacciones1 = 0
        for estudiante, promedio in promedios:
            print(f"|{str(contador):4s} | {estudiante:15s} | {promedio:10.2f}|")
            print("_"*36)
            contador += 1
            interacciones1 +=1
    return interacciones1



def promedio_estudiante_ordenado_aux(archivo):
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
        
        # ordenamiento de burbuja
        n = len(promedios)
        interacciones1 = 0
        for i in range(n):
            for j in range(0, n-i-1):
                if promedios[j][1] < promedios[j+1][1] :
                    promedios[j], promedios[j+1] = promedios[j+1], promedios[j]
                interacciones1 += 1
    return interacciones1
        
archivo = "database_p7.txt"

inter1 = promedio_estudiante_ordenado(archivo)
inter2 = promedio_estudiante_ordenado_aux(archivo)

print("interaciones 1", inter1)
print("interaciones 2", inter2)
"""

#Optimizacion 2
"""
def ordenar_estudiantes(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        estudiantes_cursos = []
        contador = 0
        for i in range(2, len(lineas)):
            notas = lineas[i].split()
            canti = sum(1 for nota in notas if nota not in ("-1", "-2"))
            estudiantes_cursos.append((lineas[i-1].strip(), canti))
            contador += 1
        
        estudiantes_cursos.sort(key=lambda x: x[1], reverse=True)
        contador += len(estudiantes_cursos)
        
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
            contador += 1

    return contador


def ordenar_estudiantes_aux(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        estudiantes_cursos = []
        contador = 0
        for i in range(cantidad):
            if i == 1:
                estudiantes = lineas[i].split()
            elif i > 1:
                notas = lineas[i].split()
                canti = 0
                for nota in notas:
                    if not(nota == "-1" or nota == "-2"):
                        canti += 1
                    contador += 1
                estudiantes_cursos.append((estudiantes[i-2], canti))
        
        # ordenamiento por seleccion
        for i in range(len(estudiantes_cursos)):
            min_idx = i
            for j in range(i+1, len(estudiantes_cursos)):
                if estudiantes_cursos[min_idx][1] < estudiantes_cursos[j][1]:
                    min_idx = j
                estudiantes_cursos[i], estudiantes_cursos[min_idx] = estudiantes_cursos[min_idx], estudiantes_cursos[i]
                contador += 1
    return contador

#archivo = "database_p7.txt"
archivo = "p6_big_data.txt"

original = ordenar_estudiantes_aux(archivo)
optimizado = ordenar_estudiantes(archivo)

print("original", original)
print("optimizado", optimizado)
"""

#Optimizacion 3
"""
def obtener_nota(tupla):
    return tupla[1]

def tres_notas_aux(archivo, curso):  
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
        contador_iteraciones = 0
        for i in range(cantidad):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
                indice_curso = cursos.index(curso)
                contador_iteraciones += 1
            elif i == 1:
                estudiantes = lineas[i].split()
                contador_iteraciones += 1
            else:
                notas = lineas[i].split()
                nota = notas[indice_curso]
                if not(nota == "-1" or nota == "-2"):
                    notas_curso.append((estudiantes[i-2], float(nota)))
                    contador_iteraciones += 1
        notas_curso.sort(key=obtener_nota, reverse=True) #Otra forma de usar el sort sin necesidad de usar lambda
        contador = 1
        for i, (estudiante, nota) in enumerate(notas_curso[:3]):
            print(f"|{str(contador):4s} | {estudiante:15s} | {nota:10.2f}|")
            print("_"*36)
            contador += 1
        print("\n"*2)
        return contador_iteraciones
   
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
        contador_iteraciones = 0
        for i in range(1, len(notas_curso)):
            key = notas_curso[i]
            j = i - 1
            while j >= 0 and key[1] > notas_curso[j][1]:
                notas_curso[j + 1] = notas_curso[j]
                j -= 1
                contador_iteraciones += 1
            notas_curso[j + 1] = key
        contador = 1
        for i, (estudiante, nota) in enumerate(notas_curso[:3]):
            print(f"|{str(contador):4s} | {estudiante:15s} | {nota:10.2f}|")
            print("_"*36)
            contador += 1
    print("\n"*2)
    return contador_iteraciones
    
#archivo = "p6_big_data.txt"   
#curso = "Curso_1" 

archivo = "database_p7.txt"
curso = "Curso1"
original = tres_notas(archivo, curso)
optimizado = tres_notas_aux(archivo, curso)

print("Original", original)
print("Optimizado", optimizado)
"""

#Optimizacion 4
"""
def ordenar_cursos(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        cursos_cancelaciones = []
        contador_iteraciones = 0
        for i in range(cantidad):
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(" ")
                cancelaciones = [0] * len(cursos)
                contador_iteraciones += 1
            elif i > 1:
                notas = lineas[i].split()
                for j in range(len(notas)):
                    contador_iteraciones += 1  # Incrementar el contador para cada nota
                    if notas[j] == "-1":
                        cancelaciones[j] += 1
        for i in range(len(cursos)):
            cursos_cancelaciones.append((cursos[i].replace(",", ""), cancelaciones[i]))
        
        # Ordenamiento por selección
        for i in range(len(cursos_cancelaciones)):
            max_idx = i
            for j in range(i+1, len(cursos_cancelaciones)):
                contador_iteraciones += 1  # Incrementar el contador para cada comparación
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
        return contador_iteraciones
    
    
def ordenar_cursos_aux(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        cursos_cancelaciones = []
        interacciones = 0
        for i in range(cantidad):
            interacciones += 1
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(" ")
                cancelaciones = [0] * len(cursos)
            elif i > 1:
                notas = lineas[i].split()
                for j in range(len(notas)):
                    interacciones += 1
                    if notas[j] == "-1":
                        cancelaciones[j] += 1
        for i in range(len(cursos)):
            interacciones += 1
            cursos_cancelaciones.append((cursos[i].replace(",", ""), cancelaciones[i]))
        
        # Ordenamiento usando sort()
        cursos_cancelaciones.sort(key=lambda x: x[1], reverse=True)
        
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
        return interacciones



#archivo = "p6_big_data.txt"   
archivo = "database_p7.txt"

original = ordenar_cursos(archivo)
optimizado = ordenar_cursos_aux(archivo)

print("Original: ", original)
print("Optimizado: ", optimizado)
"""

#Optimizacion 5
"""
def promedio_cursos_aux(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        cantidad = len(lineas)
        cur= "Curso"
        prom = "Promedio"
        posicion = "N°"
        print("_"*36)
        print(f"|{posicion:4s} | {cur:15s} | {prom:>10s}|")
        print("-"*36)
        interacciones = 0
        for i in range(cantidad):
            interacciones += 1
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
                val = len(cursos)
                sumas_canti = [(0, 0) for x in range(val)]
            elif i > 1:
                notas = lineas[i].split()
                for j in range(len(notas)):
                    interacciones += 1
                    if not(notas[j] == "-1" or notas[j] == "-2"):
                        suma, canti = sumas_canti[j]
                        sumas_canti[j] = (suma + float(notas[j]), canti + 1)
        contador = 1
        for i in range(val):
            suma, canti = sumas_canti[i]
            promedio = (suma/canti)
            print(f"| {str(contador):4s} | {cursos[i]:15s} | {promedio:10.2f}|")
            print("_"*36)
            contador +=1
    print("\n"*2)
    return interacciones


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
        interacciones = 0
        for i in range(cantidad):
            interacciones += 1
            if i == 0:
                cursos = lineas[i].replace("\n", "").split(", ")
                val = len(cursos)
                sumas = [0 for x in range(val)]
                canti = [0 for x in range(val)]
            elif i > 1:
                notas = lineas[i].split()
                for j in range(len(notas)):
                    interacciones += 1
                    if not(notas[j] == "-1" or notas[j] == "-2"):
                        sumas[j] += float(notas[j])
                        canti[j] += 1
        contador = 1
        for i in range(val):
            interacciones += 1
            promedio = (sumas[i]/canti[i])
            print(f"| {str(contador):4s} | {cursos[i]:15s} | {promedio:10.2f}|")
            print("_"*36)
            contador +=1
        print("\n"*2)
        return interacciones
    
archivo = "p6_big_data.txt"   
#archivo = "database_p7.txt"

original = promedio_cursos(archivo)
optimizado = promedio_cursos_aux(archivo)

print("Original: ", original)
print("Optimizado: ", optimizado)
"""
    
    