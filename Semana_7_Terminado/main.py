import utilidades as ut
import menu_pantalla as mp
import sys

def main():
    print("\n"*20)
    print("------------------------------------------------------------------------")
    print("BIENVENIDO A LAS ESTADISTICAS DE LOS ESTUDIANTES DE MEDICINA DE LA UDEA")
    print("------------------------------------------------------------------------")
    print("\n")
    archivo = input("Ingrese un nombre de archivo si desea analizar uno diferente al cargado, si no, pulse enter: ")
    print("\n")
    if archivo == "":
        archivo = "database_p7.txt"
    print(f"El programa se ejecutara con el archivo * {archivo} *")
    print("\n")
    inicio = True
    while inicio == True:  
        opcion_menu_pantalla_inicio = mp.pantalla_inicio() # menu inicio
        if opcion_menu_pantalla_inicio == 1:#menu de adminirstrar cursos  Listo
            opcion_cursos = mp.pantalla_administrar_cursos()#cursos
            if opcion_cursos == 1:#Agregar cursos
                nuevo_curso = input("Ingrese el nombre del curso que desea agregar: ")
                documentos = ut.obtener_documentos(archivo)
                notas = ut.capturar_cursos(documentos)
                ut.agregar_curso(nuevo_curso, notas, archivo)
            elif opcion_cursos == 2:#Eliminar cursos
                cursos = ut.obtener_cursos(archivo)
                opcion_eliminar_curso = mp.pantalla_elegir_curso(cursos)
                if opcion_eliminar_curso == "s":
                    continue
                curso_eliminar = cursos[opcion_eliminar_curso - 1].replace("\n", "").replace(" ", "")
                ut.eliminar_curso(curso_eliminar,archivo)
            elif opcion_cursos == 3:#Volver a menu anterior
                continue
        elif opcion_menu_pantalla_inicio== 2:#menu de administrar estudiantes  Listo
            opcion_estudiantes = mp.pantalla_administrar_estudiantes()#estudiantes
            if opcion_estudiantes == 1:# agregar estudiante
                cursos = ut.obtener_cursos(archivo)
                documentos = ut.obtener_documentos(archivo)
                documento = ut.agregar_estudiante(archivo, documentos)
                if documento == "s":
                    print("\n"*2)
                    print("Este estudiante ya esta registrado")
                    print("\n"*2)
                    continue
                ut.capturar_notas_estudiante(documento, cursos, archivo)
                continue
            elif opcion_estudiantes == 2:# eliminar estudiante
                documentos = ut.obtener_documentos(archivo)
                aux_menu = 0
                while aux_menu == 0:
                    documento = mp.seleccionar_documento(documentos)
                    if documento == "s":
                        aux_menu = 1
                    else:
                        ut.eliminar_estudiante(documento, archivo)
                        aux_menu = 1
            elif opcion_estudiantes == 3: # volver a menu anterior
                continue
        
        elif opcion_menu_pantalla_inicio == 3:# menu de administrador de notas
            opcion_notas = mp.pantalla_administrardor_de_notas()#notas
            if opcion_notas == 1:#editar notas  Listo
                opcion_aux = mp.elegir_metodo()
                documentos = ut.obtener_documentos(archivo)
                cursos_aux = ut.obtener_cursos(archivo)
                cursos = []
                for i in cursos_aux:
                    cursos.append(i.strip())
                if opcion_aux == 1:
                    aux_menu = 0
                    while aux_menu == 0:
                        documento_selec = mp.seleccionar_documento(documentos)
                        if documento_selec == "s":
                            aux_menu = 1
                            continue
                        curso = mp.seleccionar_curso(cursos)
                        new_nota = mp.nueva_nota()
                        aux_menu = 1
                elif opcion_aux == 2:
                    curso = input("Ingrese el nombre del curso tal y cual como esta registrado: ")
                    print("\n")
                    while not(curso in cursos):
                        print("Curso no encontrado")
                        print("\n")
                        curso = input("Ingrese el nombre del curso tal y cual como esta registrado: ")
                        print("\n")
                    documento_selec = input("Ingrese el documento del estudiante (sin puntos, ni comas): ")
                    print("\n")
                    while not(documento_selec in documentos):
                        print("Documento no encontrado")
                        print("\n")
                        documento_selec = input("Ingrese el documento del estudiante (sin puntos, ni comas): ")
                        print("\n")
                    new_nota = mp.nueva_nota()
                elif opcion_aux == 3:
                    continue
                ut.editar_notas(documento_selec, curso, archivo, new_nota)
                aux_menu = 1
                
            elif opcion_notas == 2:#visualizar notas
                aux_ver_notas = 0
                while aux_ver_notas == 0:
                    opcion_ver_notas = mp.pantalla_mostrar_notas()
                    if opcion_ver_notas == "s":
                        aux_ver_notas = 1
                        continue
                    if opcion_ver_notas == 1:
                        ut.promedio_estudiante(archivo)
                        opcion_volver = mp.volver()
                        if opcion_volver == 1:
                            continue
                    elif opcion_ver_notas == 2:
                        ut.promedio_cursos(archivo)
                        opcion_volver = mp.volver()
                        if opcion_volver == 1:
                            continue
                    elif opcion_ver_notas == 3:
                        cursos = ut.obtener_cursos(archivo)
                        curso = mp.seleccionar_curso(cursos)
                        if curso == "s":
                            continue
                        ut.tres_notas(archivo, curso)
                        opcion_volver = mp.volver()
                    elif opcion_ver_notas == 4:
                        documentos = ut.obtener_documentos(archivo)
                        documento = mp.elegir_estudiante(documentos)
                        if documento == "s":
                            continue
                        ut.curso_menor_nota(archivo, documento)
                        opcion_volver = mp.volver()
                    elif opcion_ver_notas == 5:
                        documento, posicion = ut.promedio_estudiante_ordenado(archivo)
                        print(f"El estudiante {documento[0]} se encuentra en posicion {posicion} segun el promedio " + ("\n"*2))
                    elif opcion_ver_notas == 6:
                        ut.ordenar_estudiantes(archivo)
                        opcion_volver = mp.volver()
                        if opcion_volver == 1:
                            continue
                    elif opcion_ver_notas == 7:
                        ut.ordenar_cursos(archivo)
                
            elif opcion_notas == 3:#volver al menu
                continue
        
        elif opcion_menu_pantalla_inicio == 4: #salir del sistema
            print("\n")
            salir_sistema = mp.salir_sistema()
            if salir_sistema == 1:
                print("Saliste del sistema con exito")
                sys.exit(0)
            elif salir_sistema == 2:
                inicio = True
    
main()


