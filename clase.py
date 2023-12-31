from BD.conexion import DAO

class Empresa():
    def __init__(self,rut,nombre_completo,sexo,cargo):
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.sexo = sexo
        self.cargo = cargo
    
    def returnArray(self):
        return [self.rut,self.nombre_completo,self.sexo,self.cargo]
class Trabajador(Empresa):
    def __init__(self, rut, nombre_completo, sexo, cargo, direccion, telefono, fecha_ingreso,area,departamento):
        super().__init__(rut, nombre_completo, sexo, cargo)
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso
        self.area = area
        self.depertamento = departamento

    def returnArray2(self):
        return super().returnArray() + [self.direccion, self.telefono, self.fecha_ingreso,self.area,self.depertamento]


class Musica():
    trabajador= []
    def listarTrabajador(self):
        print("\nTrabajadores:\n")
        for trabajador in self.trabajador:
                datos = "Rut: {0} | Nombre Completo: {1} | Sexo: {2} | Cargo: {3}"
                print(datos.format(trabajador.rut, trabajador.nombre_completo, trabajador.sexo, trabajador.cargo))
                print(" ")
    def rutExiste(self,rut):
        existerut = False
        c=0
        for con in self.trabajador:
            if con.rut == rut:
                existerut = True
                break
            c += 1
        if existerut:
            indice = c
        else:
            indice = -1
        return indice #retorna -1 si no está, sino, retorna indice en donde está esa id en el arreglo

    def addCd(self,trabajador):
        self.trabajador.append(trabajador)
        
    @staticmethod
    def pedirDatosCD(rut):
        rut= input("Ingrese el rut: ")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            sexo = input("Ingrese sexo: ")
            
            direccion = input("Ingrese Direccion: ")
            telefono = input("Ingrese telefono: ")
            print("====Datos laborales==== ")
            cargo = input("Ingrese cargo: ")
            fecha_ingreso = input("Ingrese fecha ingreso:")
            print("---Para ingresar el area digite el Numero.---")
            area = dao.listararea()
            for i in range(len(area)):
                print(area[i])
                continue
            area = input("Ingrese numero: ")
            print("== Ingrese ID departamento del trabajador según lo siguiente: ")
            departamento = dao.listarDepartamento()
            for i in range(len(departamento)):
                print(departamento[i])
                continue
            departamento = input("Ingrese ID del departamento: ")
            NumeroCorrecto = True
        trabajador = Trabajador(rut,nombre_completo,sexo,cargo,direccion,telefono,fecha_ingreso,area,departamento)
        return trabajador

    def agregarTrabajador(self):  #Agrega Cds
        rut=0
        for con in self.trabajador: #revisa arreglo creado más arriba
            if con.rut > rut:
                rut = con.rut
        trabajador=Musica.pedirDatosCD(rut+1) #esto asegura que el id es mayor al último registrado  #
        return trabajador
    
    def actualizarTrajador(self):
        self.listarTrabajador()
        
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            rutEditar = input("Ingrese el rut del Trabajdor a editar: ")
            if idEditar.isnumeric():
                if (int(rutEditar) > 0):
                    NumeroCorrecto = True
                    idEditar = int(rutEditar)
                else:
                    print("El rut no esta registrado")
            else:
                print("debe ingresar un número.")
        
        existeRut=self.rutExiste(rutEditar)

        if existeRut > -1:
            print("ingrese datos a modificar")
            trabajador=Musica.pedirDatosCD(rutEditar)
            self.trabajador[existeRut]=trabajador #modifica el contacto en el objeto
        else:
            trabajador = None

        return trabajador
    
    def eliminarCds(self):
        self.listarTrabajador()

        NumeroCorrecto = False
        while(not NumeroCorrecto):
            idEliminar = input("Ingrese el id del contacto a eliminar: ")
            if idEliminar.isnumeric():
                if (int(idEliminar) > 0):
                    NumeroCorrecto = True
                    idEliminar = int(idEliminar)
                else:
                    print("El Id debe ser mayor a 0.")
            else:
                print("debe ingresar un número.")
        existerut=self.rutExiste(idEliminar)

        if existerut == -1:
            idEliminar = 0
        else:
            del self.trabajador[existerut] #elimina el contacto de la lista en el obj
        
        return idEliminar
class Contacto():
    def __init__(self,rut_contacto,nombre_completo,relacion,telefono,id_rut):
        self.rut_contacto = rut_contacto
        self.nombre_completo = nombre_completo
        self.relacion = relacion
        self.telefono = telefono
        self.id_rut = id_rut

    def arrayContacto(self):
        return [self.rut_contacto,self.nombre_completo,self.relacion,self.telefono,self.id_rut]
    
class Emergencia():
    contacto =[]

    def pedirDatosContacto(self):
        rut_contacto = input("Ingrese el rut: ")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            relacion = input("Ingrese relacion: ")
            telefono = input("Ingrese telefono: ")
            id_rut = input("Ingrese el rut del trabajador")
            NumeroCorrecto = True
        contacto = Contacto(rut_contacto,nombre_completo,relacion,telefono,id_rut)
        return contacto
    def agregarContacto(self):  #Agrega Cds
        rut_contacto=0
        for con in self.contacto: #revisa arreglo creado más arriba
            if con.rut_contacto > rut_contacto:
                rut_contacto = con.rut_contacto
        contacto =Emergencia.pedirDatosContacto(rut_contacto+1) #esto asegura que el id es mayor al últiregistrado  
        return contacto

class Carga():
    def __init__(self,rut_carga,nombre_completo,parentesco,rut):
        self.rut_carga = rut_carga
        self.nombre_completo = nombre_completo
        self.parentesco = parentesco
        self.rut = rut

    def returnCarga(self):
        return [self.rut_carga,self.nombre_completo,self.parentesco,self.rut]

class Familiar():
    carga = []
    def pedirDatosCarga(rut_carga):
        print("=== Datos carga familiar del trabajador ===")
        rut_carga= input("Ingrese el rut carga familiar: ")
        NumeroCorrecto = False
        while(not NumeroCorrecto):
            nombre_completo = input("Ingrese nombre completo : ")
            parentesco = input("Ingrese parentesco: ")
            rut = input("Ingrese rut del trabajador: ")
            NumeroCorrecto = True
        carga = Carga(rut_carga,nombre_completo,parentesco,rut)
        return carga

    def agregarCarga(self):  #Agrega Cds
        rut_carga=0
        for con in self.carga: #revisa arreglo creado más arriba
            if con.rut_carga > rut_carga:
                rut_carga = con.rut_carga
        carga = Familiar.pedirDatosCarga(rut_carga+1) #esto asegura que el id es mayor al último registrado  #
        return carga
dao = DAO()