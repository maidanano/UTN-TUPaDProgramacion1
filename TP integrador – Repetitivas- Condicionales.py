#TP integrador – Repetitivas- Condicionales y Secuenciales
print("TP integrador – Repetitivas- Condicionales y Secuenciales")

while True:
    opcion = int(input("Ingrese el ejercicio a ejecutar y 0 para salir:"))
    match opcion:
        case 0:
            break
        case 1:
            '''
            Objetivo: Simular una compra con validaciones y cálculo de total.

            '''
            print("------------------ EJERCICIO 1 -------------------------")
            print(" “Caja del Kiosco”")
            print()
            #A continuación se pide el nombre del cliente
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            #Se procede con la validación del nombre del cliente
            while not (nombre_cliente.isalpha()) or not nombre_cliente:
                print("Debe ingresar solo letras en el nombre del cleinte")
                nombre_cliente = input("Ingrese el nombre del cliente: ")

            #Una vez validado el nombre, se pide la cantidad de productos a comprar:
            cant_productos = input("Ingrese la cantidad de productos a comprar: ")
            
            #Se valida la cantidad de productos. que sea un número positivo:
            while not cant_productos.isdigit() or int(cant_productos) <= 0:
                print("Debe ingresar una cantidad de productos debe ser positiva y entera")
                cant_productos = input("Ingrese la cantidad de productos a comprar: ")

            #Una vez validada la cantidad de prodcutos y el nombre, se procede con la solicitud de los demás datos de la venta
            
            #Se crean las variables "precios", "tienen descuento" que van a alvergar diferentes valores
            precios = []
            tienen_descuentos = [] 
            total_sin_descuento = 0
            total_con_descuento = 0 
            for i in range (int(cant_productos)):
                precio = input("Ingrese el precio del producto "  + str(i +1) + ": $")
                #Se valida el precio del prodcuto
                while not(precio.isdigit()):
                    print("El precio debe ser un entero positivo")
                    precio = input("Ingrese el precio del producto " + str(i +1) + ": $")
                precio = int(precio)
                #se guarda el vlor del precio en una vector de precios.    
                precios.append(precio)   
                #Se pide si tiene o no descuento el prodcuto y se lo define en minusculas
                tiene_descuento = input("El producto tiene descuento? (S/N): ").lower()
                #se guarda el valor si tiene o no descuento en un vector de descuentos
                tienen_descuentos.append(tiene_descuento)

                #Se valida si tiene o no descuento
                if "s" == tiene_descuento:
                    descuento = 0.9
                else:
                    descuento = 1
                #Se convierten las variables a enteros
                precio = int(precio)
                cant_productos = int(cant_productos)
                
                #Se realizan calculos de totales
                total_sin_descuento += precio
                total_con_descuento += (precio * descuento)
                promedio = float(total_con_descuento / cant_productos)

            #Se imprime el recibo de la venta
            print()    
            print("Cliente: ", nombre_cliente)
            print("Cantidad de productos:", cant_productos)
            #Se imprime la lista de productos con su precio y si tiene o no descuento
            for i in range (int(cant_productos)):
                print(f"Prodcuto  {i +1} - Precio:  {precios[i]} Descuento (S/N) : {tienen_descuentos[i]}")
            
            print()
            #Se imprimen totales
            print("Total sin descuentos: $", total_sin_descuento)
            print("Total con desctuentos: $", total_con_descuento)
            print("Ahorro: $", (total_sin_descuento - total_con_descuento))
            print(f"promedio por producto: ${promedio:.2f}")
            print()

        case 2:
            #Ejercicio 2 — “Acceso al Campus y Menú Seguro”
            print("------------------ EJERCICIO 2 -------------------------")
            print()
            
            #Se definen las credenciales fijas
            usuario_correcto = "alumno"
            clave_correcta = "python123"

            #Se pide ingresar al usuario ambas creedenciales para luego compararlas con las claves correctas
            #Se muestra el mensaje de ingreso
            print("Bienvenido!, ingrese sus credenciales")
            
            #Se pide que ingrese el nombre de usuario y si pone algo en mayúscula, se convierte en minusculas. 
            usuario = input("Ingrese el nombre de usuario: ").lower()
            #Se pide el ingreso de la contraseña
            clave = input("Ingrese la contraseña: ")

            #Defino la variable i (contador)
            i=1
            #Mientras el contador sea menor o iual a 3 que haga todo lo siguiente
            while i <=3:
                #Si i<=3, Se evalúan las credenciales si son verderas. Se evalúa la condicion "incorrrecta"
                if (usuario != usuario_correcto or clave != clave_correcta):
                    print()

                    print(f"Intento {i}/3")                
                    print(f"Usuario: {usuario}")
                    print(f"Clave: {clave}")
                    print("Error!. Credenciales Inválidas. Inténtelo de nuevo.")
                    print()
                    
                    i +=1
                    usuario = input("Ingrese el nombre de usuario: ").lower()
                    clave = input("Ingrese la contraseña: ")
                #Si las credenciales son verdaderas se muestra el mensaje de acceso y el menú de opciones   
                
                
                else:
                    print()
                    print("Acceso Concedido!")
                    print()

                    print("Menú de opciones")
                    print("1) Estado    2) Cambiar Clave    3) Mensajes     4) Salir")
                    opcion = input()
                    #Se evalúa el ingreso por consola si lo ingresado es un digito
                    
                    while True:
                        if not opcion.isdigit():
                            print(f"Opcion: {opcion}")
                            print("Error: ingrese un número válido")
                            print()
                            print("1) Estado    2) Cambiar Clave    3) Mensajes     4) Salir")
                            opcion = input()
                            continue
                        #Si lo ingresado es un dígito se convierte a un número entero 
                        opcion = int(opcion)

                        if opcion > 4 or opcion <= 0:
                            print(f"Opcion: {opcion}")
                            print("Error: opcion fuera de rango")
                            print()
                            print("1) Estado    2) Cambiar Clave    3) Mensajes     4) Salir")
                            opcion = input()
                            
                        
                        #Se muestra la opción eleida 1 y se vuelve a mostrar el menú
                        elif opcion == 1:
                            print("Estado: Alumno Inscripto")
                            print()
                            print("1) Estado    2) Cambiar Clave    3) Mensajes     4) Salir")
                            opcion = input()
                        
                        #Se muestra la opción eleida 2 y se vuelve a mostrar el menú    
                        elif opcion ==2:
                            #Se pide ingresar la nueva clave
                            clave = input("Ingrese la nueva clave: ")
                            #Se evalúa el mínimo de caracteres necesarios
                            while len(clave) < 6:
                                print("Error: mínimo 6 caracteres")
                                clave = input("Ingrese la nueva clave: ")
                            
                            #Se solicita la confirmación de la nueva clave    
                            confirmacion = input("ingrese nuevamnte la nueva clave para confirmar: ")
                            
                            #Se evalúa si la nueva clave y la confirmación son iguales
                            while clave != confirmacion:
                                print("Las claves no coinciden.")
                                #Se solicita de nuevo la clave confirmación debido a que no son iguales
                                confirmacion = input("ingrese nuevamnte la nueva clave para confirmar: ")
                            
                            #Si la clave nueva y la confirmación son igules, se modifica la clave correcta    
                            if clave == confirmacion:
                                clave = clave_correcta                          
                                print()
                                print("Clave cambiada con éxito!")

                            print()
                            print("1) Estado    2) Cambiar Clave    3) Mensajes     4) Salir")
                            opcion = input()
                        
                        #Se muestra la opción eleida 3 y se vuelve a mostrar el menú
                        elif opcion == 3:
                            mensaje = input("Ingrese un mensaje: ")
                            print(f"Mensaje Enviado!: {mensaje}")
                            print()
                            print("1) Estado    2) Cambiar Clave    3) Mensajes     4) Salir")
                            opcion = input()
                        
                        #Se muestra la opción eleida 4 y se cierra la sesión saliendo del programa
                        elif opcion == 4:
                            print()
                            print("Cesión Cerrada")
                            print()
                            break
                    break
                            
                    #Si el contador es igual a 3 (lo que equivaleal 3er intento) y la credenciales son incorrectas, se bloquea la cuenta
                if i==3 and (usuario != usuario_correcto or clave != clave_correcta):
                    print()
                    print("Intento 3/3 faliido")
                    print("Cuenta bloqueada")
                    print()
                    break

        case 3:
            #Ejercicio 3 (Alta) — "Agenda de Turnos con Nombres"
            print("------------------ EJERCICIO 3 -------------------------")
            print("Ejercicio 3 (Alta) — Agenda de Turnos con Nombres")
            print()
            
            #Se definen las variables de los dias y turnos
            lunes_t1 = ""
            lunes_t2 = ""
            lunes_t3 = ""
            lunes_t4 = ""
            martes_t1 = ""
            martes_t2 = ""
            martes_t3 = ""
            
            #Se solicita el nombre del operador para mostrar luego el menú de opciones.
            operador = input("Ingrese el nombre del operador: ")
            
            #Se verifica que lo ingresado sean solo letras. Mientras no lo sea, se vuelve a pedir.
            while not operador.isalpha():
                print()
                print("Error!. El nombre del operador debe contener solo letras")
                print()
                #Se solicita el ingrso del nombre del operador
                operador = input("Ingrese el nombre del operador: ")
            print()
            print(f"Bienvenido! {operador}")
            
            while True:

                print()
                #Menu
                print("Menu:")
                print("1). Reservar Turno")
                print("2). Cancelar Turno")
                print("3). Ver agenda del día")
                print("4). Ver Resumen general")
                print("5). Cerrar Sistema")
                
                #Se solicita el ingreso de una opción del menú
                opcion = input("seleccione una opción:")
                
                #Se evalúa si lo ingresado es un digito, de no ser hacer se repite la petición
                if not opcion.isdigit():
                    print("Debe ingresar solo números, vuelva a ingresar la opción:")
                    continue
                
                # Si la opción ingresada es un dígito, se convieerte la variable a número entero
                opcion = int(opcion)
                    
                if opcion >= 6 or opcion <=0:
                    print(f"Opcion: {opcion}")
                    print("Error: opcion fuera de rango")
                    continue
                
                
                #RESERVA DE TURNOS
                if opcion == 1:
                    print("Reservar turno:")
                    print("------ elije el día:")
                    print("1)- Lunes")
                    print("2)- Martes")
                    dia = input()
                    
                    #Se verifica que la variable dia sea un digito
                    if not dia.isdigit():
                        print("debe ingresar el numero 1 para elegir Lunes o el numero 2 para elegir Martes")
                        continue
                    
                    #Si es un digito se transforma la variable a número entero
                    dia = int(dia)
                        
                    #Se verifica que la variable dia sea 1 o 2
                    if dia != 1 and dia != 2:
                        print()
                        print("Ha ingresado un valor no válido")
                        continue
                    
                    #Se  solicita el nombre del paciente
                    print()
                    nombre = input("Ingrese el nombre del paciente: ")               

                    #Se verifica que el nombre del paciente sean solo letras                
                    if not nombre.isalpha():
                        print()
                        print("Error!. El nombre del paciente debe contener solo letras")
                        print()
                        continue

                    #Turnos para día Lunes
                    if dia == 1:                        
                        if lunes_t1 == "" or lunes_t1 == "libre":
                            lunes_t1 = nombre
                            print()
                            print(f"{nombre}, has sido agendado al primer turno del día lunes")
                        
                        elif lunes_t2 == "" or lunes_t2 == "libre":
                            lunes_t2 = nombre
                            print()
                            print(f"{nombre}, has sido agendado al segundo turno del día lunes")
                        
                        elif lunes_t3 == "" or lunes_t3 == "libre":
                            lunes_t3 = nombre
                            print()
                            print(f"{nombre}, has sido agendado al tercer turno del día lunes")
                        
                        elif lunes_t4 =="" or lunes_t4 == "libre":
                            lunes_t4 = nombre
                            print()
                            print(f"{nombre}, has sido agendado al cuarto turno del día  lunes")
                        else:
                            print("\n No hay turnos disponibles para este día")
                        
                    #Turnos para día Martes
                    else:
                        if martes_t1 == "" or martes_t1 == "libre":
                            martes_t1 = nombre
                            print(f"{nombre}, has sido agendado al primer turno del día martes")
                        
                        elif martes_t2 == "" or martes_t2 == "libre":
                            martes_t2 = nombre
                            print(f"{nombre}, has sido agendado al segundo turno del día martes")
                        
                        elif martes_t3 == "" or martes_t3 == "libre":
                            martes_t3 = nombre
                            print(f"{nombre}, has sido agendado al tercer turno del día martes")
                        
                        else:
                            print("\n No hay turnos disponibles para este día")
                #CANCELAR TURNOS                            
                elif opcion == 2:
                        print()

                        print("------ Elije el día:")
                        print("1)- Lunes       2)- Martes")
                        dia = input()

                        if not dia.isdigit():
                            print("\n Error: Debe ingresar números.") 
                            continue

                        dia = int(dia)

                        if dia != 1 and dia != 2:
                            print()
                            print("Ha ingresado un valor no válido")
                            continue                        

                        nombre = input("\n Ingrese el nombre del  paciente para cancelar el turno: ") 
                    
                        if dia == 1:
                            if nombre == lunes_t1:
                                lunes_t1 = ""
                                print("Turno cancelado con éxito.")
                            elif nombre == lunes_t2:
                                lunes_t2 = ""
                                print("Turno cancelado con éxito.")
                            elif nombre == lunes_t3:
                                lunes_t3 = ""
                                print("Turno cancelado con éxito.")
                            elif nombre == lunes_t4:
                                lunes_t4 = ""
                                print("Turno cancelado con éxito.")
                            else:
                                print("\n No hay turno registrado para ese nombre de paciente")
                                continue

                        elif dia == 2:
                            if nombre == martes_t1:
                                martes_t1 = ""
                                print("Turno cancelado con éxito.")
                            
                            elif nombre == martes_t2:
                                martes_t2 = ""
                                print("Turno cancelado con éxito.")
                            
                            elif nombre == martes_t3:
                                martes_t3 = ""
                                print("Turno cancelado con éxito.")
                            
                        else:
                            print("\n No hay ningún turno para ese paciente en ese dia.")
                            continue

                        print("\n Turno cancelado con éxito!.")
                
                # VER AGENDA   
                elif opcion == 3:
                    print()
                    print("Has seleccionado --- Ver agenda del día:")
                    print()
                    print("Elije el día para ver su agenda:")
                    print("1)- Lunes       2)- Martes")
                    dia = input()

                    if not dia.isdigit():
                        print("debe ingresar el numero 1 para elegir Lunes o el numero 2 para elegir Martes")
                        continue
                
                    dia = int(dia)  

                    if dia == 1:
                        
                        if lunes_t1 == "":
                            lunes_t1 = "libre"
                        
                        if lunes_t2 == "":
                            lunes_t2 = "libre"
                        
                        if lunes_t3 == "":
                            lunes_t3 = "libre"
                        
                        if lunes_t4 == "":
                            lunes_t4 = "libre"
                        
                        print("\n Seleccionaste la agenda del día Lunes:")
                        print(f"Turno 1: {lunes_t1}")
                        print(f"Turno 2: {lunes_t2}")
                        print(f"Turno 3: {lunes_t3}") 
                        print(f"Turno 4: {lunes_t4}")

                    elif dia == 2:
                        if martes_t1 == "":
                            martes_t1 = "libre"
                        
                        if martes_t2 == "":
                            martes_t2 = "libre"
                        
                        if martes_t3 == "":
                            martes_t3 = "libre"

                        print("\n Seleccionaste la agenda del día Martes:")
                        print(f"Turno 1: {martes_t1}")
                        print(f"Turno 2: {martes_t2}")
                        print(f"Turno 3: {martes_t3}")

                    else:
                        print("\n Error al seleccionar la agenda,")
                        continue         

                #Seleccion de resumen general
                elif opcion == 4:
                    
                    turnos_lunes_ocup = 0
                    turnos_martes_ocup = 0

                    #Conteo para turnos libres de los Lunes
                    if lunes_t1 != "" and not lunes_t1 == "libre":
                        turnos_lunes_ocup += 1
                    
                    if lunes_t2 != "" and not lunes_t2 == "libre":
                        turnos_lunes_ocup += 1
                    
                    if lunes_t3 != "" and not lunes_t3 == "libre":
                        turnos_lunes_ocup += 1
                    
                    if lunes_t4 != "" and not lunes_t4 == "libre":
                        turnos_lunes_ocup += 1

                    #Conteo para los turnos libres de los Martes
                    if martes_t1 != "" and not martes_t1 == "libre":
                        turnos_martes_ocup += 1
                    
                    if martes_t2 != "" and not martes_t2 == "libre":
                        turnos_martes_ocup += 1
                    
                    if martes_t3 != "" and not martes_t3 == "libre":
                        turnos_martes_ocup += 1

                    turnos_lunes_disp = 4 - turnos_lunes_ocup
                    turnos_martes_disp = 3 - turnos_martes_ocup    

                    print()
                    print("Has seleccionado --- Ver resumen general:")
                    print(f"La cantidad de turnos libres del día Lunes es: {turnos_lunes_disp} turnos.")
                    print(f"La cantidad de turnos ocupados del día Lunes es : {turnos_lunes_ocup} turnos")
                    print()
                    print(f"La cantidad de turnos libres del día Martes es: {turnos_martes_disp} turnos.")
                    print(f"La cantidad de turnos ocupados del día Martes es : {turnos_martes_ocup} turnos")

                    if turnos_lunes_disp == turnos_martes_disp:
                        print()
                        print("El día lunes y martes coinciden con la cantidad de turnos disponibles")
                    elif turnos_lunes_disp > turnos_martes_disp:
                        print()
                        print("El día lunes tiene mayor disponibilidad de turnos")
                    else:
                        print()
                        print("el día martes tiene mayor diponibilidad de turnos")

                #Seleccion finalizar sesión
                if opcion == 5:
                    print()
                    print("Sesion finalizada")
                    break

        case 4:
                #Ejercicio 4 — “Escape Room: La Bóveda”
                print("\n Ejercicio 4 — “Escape Room: La Bóveda \n")

                #inicializacion de variables
                energia = 100
                tiempo = 12
                cerraduras_abiertas = 0
                alarma = False
                codigo_parcial = ""
                forzar_seguidas = 0

                #Se solicita el nombre del agente
                print("\n Bienvenido Agente!\n")
                agente = input("Ingrese su nombre: ")

                #Verifico que el nombre del agente contenga solo letras
                while not agente.isalpha():
                    print("\n El nombre del agente debe contener solo letras\n")
                    agente = input("Ingrese el nombre del agente: ")

                #Comienza el juego!
                while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

                    #Bloqueo por alarma
                    if alarma and tiempo <=3:
                        print("\n Sistema bloqueado por alarma!")
                        break

                    print("\nEstado:")
                    print(f"Tenés {energia} de energía")
                    print(f"Tu tiempo es de: {tiempo}")
                    print(f"La cantidad de cerraduras abiertas es: {cerraduras_abiertas}")
                    print(f"Alarma en estado: {alarma}")
                    print(f"Código parcial: {codigo_parcial}")

                    #Menú de opciones
                    print("\n1)- Forzar cerradora")
                    print("2)- Hackear panel")
                    print("3)- Descansar")

                    #Validacion e a opción elegida
                    while True:
                        opcion = input("Elegí una de las opciones: ")
                        if opcion.isdigit():
                            opcion = int(opcion)
                            if opcion > 3 or opcion < 1:
                                print("\nOpción inválidad.")
                            else:
                                break
                                
                        else:
                            print("\nDebe ingresar solo números del 1 al 3")
                            
                    
                    #Se elige la opcion de forzar Cerradura
                    if opcion == 1:

                        print("\nHa elegido: ---Forzar cerradurda---\n")
                        energia -=20
                        tiempo -= 2
                        forzar_seguidas += 1

                        #Para la regla Anti.Spam
                        if forzar_seguidas == 3:
                            print("\nAlarma activada--- Se ha trabado la cerradura")
                            alarma = True

                        else:
                            #Para riesgo de energía bajo
                            if energia < 40:    
                                print("\nRiesgo de Alarma\n")
                                numero = input("Ingrese un numero entre 1 y 3 : ")

                                while not numero.isdigit() or int(numero) > 3 or int(numero) < 1:
                                    print("\El núero ingresado es in´valido. Intentelo de nuevo")
                                    numero = input("Ingrese un numero entre 1 y 3 : ")

                                if numero == 3:
                                    alarma = True

                            if not alarma:
                                print("\nCerradura abierta!\n")
                                cerraduras_abiertas += 1             

                    #Se elije la opcion de Hackear Panel
                    elif opcion == 2:
                        energia -= 10
                        tiempo -= 2
                        forzar_seguidas = 0
                        print("\nHas elegido: ---Hackear panel---\n")
                        
                        for i in range(4):
                            print(f"Paso {i + 1}")
                            codigo_parcial += "A"

                        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                            cerraduras_abiertas += 1
                            print("\nCerradura abierta por Hackeo!")
                    
                    #Se elijer la opción Descansar
                    elif opcion == 3:
                        print("\nHas elegido: ---Descansar---\n")

                        energia += 15
                        
                        if energia > 100:
                            energia = 100

                        tiempo -= 1
                        forzar_seguidas = 0

                        if alarma:
                            energia -= 10
                            print("\nGasto de energía ectra por alarma")           

                #RESULTADOS
                print("\n////// RESULTADOS //////\n")

                if cerraduras_abiertas == 3:
                    print("Has abierto la Bóbeda. VICTORIA! ")
                elif energia <= 0 or tiempo <= 0:
                    print("Tus recursos se acabaron antes de que puedas abrir la bóbeda. HAS SIDO DERROTADO!")
                elif alarma and tiempo <= 3:
                    print("Sistema Bloqueeado. HAS SIDO DERROTADO!")

        case  5:
            #Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
            print("\nEjercicio 5 — Escape Room: La Arena del Gladiador\n" )
            print("--- BIENVEINDO A LA ARENA---")            
            
            #Se pide el nombre al Gladiador
            gladiador = input("Nombre del Gladiador: ")
            
            #Se  verifica que el nombre solo tenga letras
            while not gladiador.isalpha():
                print("\nError: Solo se permiten letras\n")
                gladiador = input("Nombre del Gladiador: ")

            #Definicion de variables
            vida_gladiador = 100
            vida_enemigo = 100
            posiones = 3
            ataque_pesado = 15
            ataque_enemigo = 12
            turno_gladiador = True    
            
            print("\n=== INICIO DEL COMBATE ===\n")
            
            while vida_gladiador > 0 and vida_enemigo > 0:
                print("\n=== NUEVO TURNO ===\n ")
                print(f"{gladiador} (HP: {vida_gladiador})  vs  Enemigo (HP: {vida_enemigo:.2f})    |  Pociones: {posiones}\n")            
                print("Elige acción:")
                print("1. Ataque Pesado")
                print("2. Ráfaga Veloz")
                print("3. Curar")
                
                opcion = input("Opción:")
                while not opcion.isdigit():
                    print("Error: Ingrese un número válido.")
                    opcion = input("Opción:")

                opcion = int(opcion)

                if opcion < 1 or  opcion > 3:
                    print("Error. Opción fuera de rango")
                    continue
                    

                elif opcion == 1:
                    print("Inicias un Ataque Pesado!")
                    if vida_enemigo < 20:
                        vida_enemigo -= (ataque_pesado * 1.5)
                        print(f"¡Atacaste al enemigo por {ataque_pesado * 1.5} puntos de daño!")
                    else:
                        vida_enemigo -= ataque_pesado
                        print(f"¡Atacaste al enemigo por {ataque_pesado} puntos de daño!")
                
                elif opcion == 2:
                    print("Inicias un Ataque Veloz!")
                    for  i in range(3):
                        vida_enemigo -= 5
                        print(" Golpe conectado por 5 de daño")
                
                elif opcion == 3:
                    if posiones > 0:
                        vida_gladiador += 30
                        posiones -= 1
                        print("Usaste una posión!. Sumas 30 puntos a tu vida")
                    else:
                        print("¡No quedan pociones!")    
                        
                #Ataque enemigo
                print("¡El enemigo contraataca por 12 puntos!")
                vida_gladiador -= 12

                
            if vida_gladiador <= 0:
                print("\n DERROTA. Has caído en combate.\n")
            
            elif vida_enemigo <= 0:
                print(f"\n¡VICTORIA! {gladiador} ha ganado la batalla\n")    







