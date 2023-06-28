from BD.conexion import DAO
from clase import Empresa, Musica, Emergencia, Familiar

def actualizarTrabajador():
    arrayCd = dao.listarTrabajador()
    for con in arrayCd:
        musica.addCd(Empresa(con[0], con[1], con[2], con[3]))

def listar_trabajador():
    if len(musica.trabajador) > 0:
        musica.listarTrabajador()
    else:
        print("No se encontraron trabajadores...")

def listar_por_sexo():
    sexo = input("Ingrese el sexo para filtrar (Masculino/Femenino): ")
    trabajadores = dao.listarsexo(sexo)
    if len(trabajadores) > 0:
        for trabajador in trabajadores:
            print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3}".format(
                trabajador[0], trabajador[1], trabajador[2], trabajador[3]
            ))
    else:
        print("No se encontraron trabajadores con el sexo especificado.")

def listar_por_cargo():
    cargo = input("Ingrese el cargo para filtrar: ")
    trabajadores = dao.listarCargo(cargo)
    if len(trabajadores) > 0:
        for trabajador in trabajadores:
            print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3}".format(
                trabajador[0], trabajador[1], trabajador[2], trabajador[3]
            ))
    else:
        print("No se encontraron trabajadores con el cargo especificado.")

def listar_por_area():
    print("Para Filtrar por area ingrese el digito del area")
    print(dao.listararea())
    area = input("Ingrese el área para filtrar: ")
    trabajador = dao.listarArea(area)
    if len(trabajador) > 0:
        for trabajador in trabajador:
            print("Rut: {0} | Nombre: {1} | Sexo: {2} | Cargo: {3}".format(
                trabajador[0], trabajador[1], trabajador[2], trabajador[3]
            ))
    else:
        print("No se encontraron trabajadores en el área especificada.")

def registrar_trabajador():
    empleado = musica.agregarTrabajador()
    contacto_a = emergencia.agregarContacto()
    carga = familiar.agregarCarga()
    try:
        dao.registrarTrabajador(empleado.returnArray2())
        dao.registrarContacto(contacto_a.arrayContacto())
        dao.registrarCarga(carga.returnCarga())
    except:
        print("Opción no válida...")

# Programa principal
musica = Musica()
emergencia = Emergencia()
familiar = Familiar()
dao = DAO()
actualizarTrabajador()  # Ponemos los datos de la BD en el objeto agenda

def menuJefe():
    continuar = True
    while continuar:
        opcionCorrecta = False
        while not opcionCorrecta:
            print("==================== MENÚ JEFE ====================")
            print("1.- Listar Trabajadores")
            print("2.- Listar por Sexo")
            print("3.- Listar por Cargo")
            print("4.- Listar por Área")
            print("5.- Registrar Trabajador")
            print("6.- Salir")
            print("===================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 6:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                continuar = False
                print("¡Gracias por usar la aplicación!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    if opcion == 1:
        listar_trabajador()
    elif opcion == 2:
        listar_por_sexo()
    elif opcion == 3:
        listar_por_cargo()
    elif opcion == 4:
        listar_por_area()
    elif opcion == 5:
        registrar_trabajador()

menuJefe()



