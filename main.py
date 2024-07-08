def validacionFloat(pregunta):
    while True:
        try:
            respuesta = float(input(pregunta))
            break
        except ValueError:
            print("Error, ingrese un valor numérico.")
    return respuesta


def validacionInt(pregunta):
    while True:
        try:
            respuesta = int(input(pregunta))
            break
        except ValueError:
            print("Error, ingrese un valor numérico sin decimales.")
    return respuesta

def validacionSN(pregunta):
    while True:
        respuesta = input(pregunta).upper()
        if respuesta == "S" or respuesta == "N":
            break
        else:
            print("Error, ingrese S o N.")
    return respuesta

# empresa = "Laboratorios Regionales S.A. de C.V."
empresa = input("Ingrese el nombre de la empresa: ")

print(f"Empresa: {empresa}")
print("Presupuestó Maestro\n")

# Registro de datos
print("Ingreso de datos del Estado de Situación Financiera\n")

# Activos
print("Ingreso de datos de los activos")
# Circulantes
print("Ingreso de datos de los activos circulantes")
efectivoESF = validacionFloat("Ingrese el total de la cuenta de efectivo: ")
clientesESF = validacionFloat("Ingrese el total de la cuenta de clientes: ")
invMaterialesESF = validacionFloat("Ingrese el total de la cuenta de inventario de materiales: ")
invArticulosESF = validacionFloat("Ingrese el total de la cuenta de inventario de artículos: ")
totalCirculanteESF = efectivoESF + clientesESF + invMaterialesESF + invArticulosESF
print(f"El total de activos circulantes es: ${totalCirculanteESF:,.2f}\n")

# No Circulantes
print("Ingreso de datos de los activos no circulantes")
terrenoESF = validacionFloat("Ingrese el total de la cuenta de terreno: ")
plantaYEquipoESF = validacionFloat("Ingrese el total de la cuenta de planta y equipo: ")
depAcumESF = validacionFloat("Ingrese el total de la cuenta de depreciación acumulada: ")
totalNoCirculanteESF = terrenoESF + plantaYEquipoESF - depAcumESF
print(f"El total de activos no circulantes es: ${totalNoCirculanteESF:,.2f}\n")

# Activo Total
activoTotalESF = totalCirculanteESF + totalNoCirculanteESF
print(f"El total de activos es: ${activoTotalESF:,.2f}\n")

# Pasivos
print("Ingreso de datos de los pasivos")
# Corto Plazo
print("Ingreso de datos de los pasivos a corto plazo\n")
proveedoresESF = validacionFloat("Ingrese el total de la cuenta de proveedores: ")
documentosPorPagarESF = validacionFloat("Ingrese el total de la cuenta de documentos por pagar: ")
ISRPagarESF = validacionFloat("Ingrese el total de la cuenta de ISR por pagar: ")
pasivosCortoPlazoESF = proveedoresESF + documentosPorPagarESF + ISRPagarESF
print(f"El total de pasivos a corto plazo es: ${pasivosCortoPlazoESF:,.2f}\n")

# Largo Plazo
print("Ingreso de datos de los pasivos a largo plazo")
obligacionesESF = validacionFloat("Ingrese el total de la cuenta de obligaciones por pagar: ")
print(f"El total de pasivos a largo plazo es: ${obligacionesESF:,.2f}\n")

# Total Pasivo
pasivoTotalESF = proveedoresESF + documentosPorPagarESF + ISRPagarESF + obligacionesESF
print(f"El total de pasivos es: ${pasivoTotalESF:,.2f}\n")

# Capital Contable
print("Ingreso de datos del capital contable")
capitalAportadoESF = validacionFloat("Ingrese el total de Capital aportado: ")
# capitalGanadoESF = validacionFloat("Ingrese el total de Capital ganado: ")
capitalGanadoESF = 89625.00
print(f"El total de capital ganado es: ${capitalGanadoESF:,.2f}")
totalCapitalESF = capitalAportadoESF + capitalGanadoESF
print(f"El total de capital contable es: ${totalCapitalESF:,.2f}\n")

print(f"El total de Pasivo y Capital Contable es: ${pasivoTotalESF + totalCapitalESF:,.2f}\n")

numeroProductos = validacionInt("Ingrese el número de productos que se fabrican: ")
numeroMateriasPrimas = validacionInt("Ingrese el número de materias primas que se utilizan: ")

productos = {}
materiasPrimas = {}

# Información de Materias Primas
print("\nIngreso de datos de las materias primas")

for num in range(numeroMateriasPrimas):
    nombreMP = input("Ingrese el nombre de la materia prima: ")
    invInicialMP = validacionFloat("Ingrese cuantos gramos se tendrían en inventario al iniciar: ")
    invFinalMP = validacionFloat("Ingrese cuantos gramos se tendrían en inventario al terminar: ")
    costoMP1S = validacionFloat("Ingrese su costo en el 1er semestre: ")
    costoMP2S = validacionFloat("Ingrese su costo en el 2do semestre: ")
    materiasPrimas[f"{nombreMP}"] = {"costos": {"1Sem": costoMP1S, "2Sem": costoMP2S},
                                     "inventario": {"inicial": invInicialMP, "final": invFinalMP},
                                     'requerimientos': {'1Sem': 0, '2Sem': 0, 'total': 0},
                                     'compra': {'1Sem': 0, '2Sem': 0, 'total': 0}}
    print("")

# Información de Productos
print("Ingreso de datos de los productos")
for num in range(numeroProductos):
    nombreProducto = input("Ingrese el nombre del producto: ")
    invInicialProd = validacionFloat(
        f"Ingrese cuantas unidades del producto {nombreProducto} se tendrían en inventario al iniciar: ")
    invFinalProd = validacionFloat(
        f"Ingrese cuantas unidades del producto {nombreProducto} se tendrían en inventario al terminar: ")
    precioProducto1S = validacionFloat(f"Ingrese el precio de venta del producto {nombreProducto} en el 1er semestre: ")
    precioProducto2S = validacionFloat(f"Ingrese el precio de venta del producto {nombreProducto} en el 2do semestre: ")
    ventasPlaneadas1S = validacionFloat(f"Ingrese cuantas unidades se planean vender del producto {nombreProducto} en el 1er semestre: ")
    ventasPlaneadas2S = validacionFloat(f"Ingrese cuantas unidades se planean vender del producto {nombreProducto} en el 2do semestre: ")

    productos[f"{nombreProducto}"] = {
        "precioVenta": {"1Sem": precioProducto1S, "2Sem": precioProducto2S},
        "ventasProyectadas": {"1Sem": ventasPlaneadas1S, "2Sem": ventasPlaneadas2S},
        "inventario": {"inicial": invInicialProd, "final": invFinalProd},
        "requisitos": {},
        "requerimientos": {},
    }

    for materia in materiasPrimas:
        requisitoMP = validacionFloat(f"Ingrese la cantidad de {materia} que se requiere para elaborar el producto {nombreProducto}: ")
        productos[f"{nombreProducto}"]["requisitos"][f"{materia}"] = requisitoMP
    horasElaboracion = validacionFloat(f"Ingrese las horas que se requieren para elaborar el producto {nombreProducto}: ")
    productos[f"{nombreProducto}"]["requisitos"]["horas"] = horasElaboracion
    print("")

print("Costo Mano de Obra")
manoObra1Sem = validacionFloat("Ingrese el total de la mano de obra por hora del 1er semestre: ")
manoObra2Sem = validacionFloat("Ingrese el total de la mano de obra por hora del 2do semestre: ")

# Gastos de administración y ventas
print("\nIngreso de datos de los gastos de administración y ventas")
depreciacionAV = validacionFloat("Ingrese el total de la depreciación: ")
sueldosYSalarios = validacionFloat("Ingrese el total de los sueldos y salarios: ")
porcentajeComisiones = validacionFloat("Ingrese el porcentaje de comisiones: ")
porcentajeComisiones = porcentajeComisiones / 100
variosAV1Sem = validacionFloat("Ingrese el total de los gastos varios del 1er semestre: ")
variosAV2Sem = validacionFloat("Ingrese el total de los gastos varios del 2do semestre: ")
interesesObligaciones = validacionFloat("Ingrese el total de los intereses por pagar de obligaciones: ")

# Gastos de fabricación indirecta
print("\nIngreso de datos de los gastos de fabricación indirecta")

depreciacionFI = validacionFloat("Ingrese el total de la depreciación: ")
segurosFI = validacionFloat("Ingrese el total de los seguros: ")
mantenimiento1Sem = validacionFloat("Ingrese el total de los gastos de mantenimiento del 1er semestre: ")
mantenimiento2Sem = validacionFloat("Ingrese el total de los gastos de mantenimiento del 2do semestre: ")
energeticos1Sem = validacionFloat("Ingrese el total de los gastos de energéticos del 1er semestre: ")
energeticos2Sem = validacionFloat("Ingrese el total de los gastos de energéticos del 2do semestre: ")
variosFI = validacionFloat("Ingrese el total de los gastos varios: ")

# Datos Adicionales
print("\nIngreso de datos adicionales")
tasaISR = validacionFloat("Ingrese la tasa de ISR: ")
tasaISR = tasaISR / 100
tasaUtilidad = validacionFloat("Ingrese la tasa de utilidad: ")
tasaUtilidad = tasaUtilidad / 100
porcentajeCobroClientesESF = validacionFloat("Ingrese el porcentaje de cobro de la cuenta de clientes del ESF: ")
porcentajeCobroClientesESF = porcentajeCobroClientesESF / 100
porcentajeCobroClientesActual = validacionFloat("Ingrese el porcentaje de cobro de la cuenta de clientes del año: ")
porcentajeCobroClientesActual = porcentajeCobroClientesActual / 100
porcentajePagoESF = validacionFloat("Ingrese el porcentaje de pago de la cuenta de proveedores del ESF: ")
porcentajePagoESF = porcentajePagoESF / 100
porcentajePagoActual = validacionFloat("Ingrese el porcentaje de pago de la cuenta de proveedores del año: ")
porcentajePagoActual = porcentajePagoActual / 100
pagoISRESF = validacionSN("¿Se pagara ISR del ESF? (S/N): ")
pagoISRActual = validacionSN("¿Se pagara ISR del año? (S/N): ")

# Presupuesto de Ventas
print("\n1.- Presupuesto de Ventas")
totalVentas = 0
for producto in productos.items():
    ventas1Sem = producto[1]["ventasProyectadas"]["1Sem"] * producto[1]["precioVenta"]["1Sem"]
    ventas2Sem = producto[1]["ventasProyectadas"]["2Sem"] * producto[1]["precioVenta"]["2Sem"]
    totalVentas += ventas1Sem + ventas2Sem
print(f"El total de ventas es de: ${totalVentas:,.2f}")

# Determinación del saldo de Clientes y Flujo de Entradas
print("\n2.- Determinación del saldo de Clientes y Flujo de Entradas")
# Saldo de Clientes
totalClientes = clientesESF + totalVentas

# Entradas de efectivo:
totalEntradas = (clientesESF * porcentajeCobroClientesESF) + (totalVentas * porcentajeCobroClientesActual)

# Resultado de la Cuenta de Clientes
saldoClientes = totalClientes - totalEntradas
print(f"El saldo de clientes es de: ${saldoClientes:,.2f}")

# Presupuesto de producción
print("\n3.- Presupuesto de producción")
# Unidades a producir
for producto in productos:
    unidadesProducir1Sem = productos[f"{producto}"]["ventasProyectadas"]["1Sem"] + \
                           productos[f"{producto}"]["inventario"]["inicial"]
    unidadesProducir1Sem -= productos[f"{producto}"]["inventario"]["inicial"]
    unidadesProducir2Sem = productos[f"{producto}"]["ventasProyectadas"]["2Sem"] + \
                           productos[f"{producto}"]["inventario"]["final"]
    unidadesProducir2Sem -= productos[f"{producto}"]["inventario"]["inicial"]
    unidadesProducir = unidadesProducir1Sem + unidadesProducir2Sem
    productos[f"{producto}"]["unidadesProducir"] = {"1Sem": unidadesProducir1Sem, "2Sem": unidadesProducir2Sem,
                                                    "total": unidadesProducir}
    # print(f"Unidades a producir del producto {producto} en el 1er semestre: {unidadesProducir1Sem} unidades.")
    # print(f"Unidades a producir del producto {producto} en el 2do semestre: {unidadesProducir2Sem} unidades.")
    print(f"Unidades a producir del producto {producto} en el año: {unidadesProducir} unidades.")
    # print("")

# Presupuesto de requerimientos de materias primas
print("\n4.- Presupuesto de requerimientos de materias primas")
for producto in productos:
    for materia in materiasPrimas:
        requerimientoMP1Sem = productos[f"{producto}"]["unidadesProducir"]["1Sem"] * \
                              productos[f"{producto}"]["requisitos"][f"{materia}"]
        requerimientoMP2Sem = productos[f"{producto}"]["unidadesProducir"]["2Sem"] * \
                              productos[f"{producto}"]["requisitos"][f"{materia}"]
        requerimientoMP = requerimientoMP1Sem + requerimientoMP2Sem
        materiasPrimas[f"{materia}"]["requerimientos"]["1Sem"] += requerimientoMP1Sem
        materiasPrimas[f"{materia}"]["requerimientos"]["2Sem"] += requerimientoMP2Sem
        materiasPrimas[f"{materia}"]["requerimientos"]["total"] += requerimientoMP
        # print(f"Requerimiento de {materia} del producto {producto} en el 1er semestre: {requerimientoMP1Sem} gramos.")
        # print(f"Requerimiento de {materia} del producto {producto} en el 2do semestre: {requerimientoMP2Sem} gramos.")
        # print(f"Requerimiento de {materia} del producto {producto} en el año: {requerimientoMP:,} gramos.")
        # print("")

print("Requerimientos totales de materias primas")
for materia in materiasPrimas:
    # print(f"Requerimiento de {materia} en el 1er semestre: {materiasPrimas[f'{materia}']['requerimientos']['1Sem']:,} gramos.")
    # print(f"Requerimiento de {materia} en el 2do semestre: {materiasPrimas[f'{materia}']['requerimientos']['2Sem']:,} gramos.")
    print(f"Requerimiento de {materia} en el año: {materiasPrimas[f'{materia}']['requerimientos']['total']:,} gramos.")

# Presupuesto de compra de materias primas
print("\n5.- Presupuesto de compra de materias primas")
compraTotal = 0
for materia in materiasPrimas:
    requerimientoMP1Sem = materiasPrimas[f"{materia}"]["requerimientos"]["1Sem"] + \
                          materiasPrimas[f"{materia}"]["inventario"]["inicial"]
    requerimientoMP1Sem -= materiasPrimas[f"{materia}"]["inventario"]["inicial"]
    compraMP1Sem = requerimientoMP1Sem * materiasPrimas[f"{materia}"]["costos"]["1Sem"]
    requerimientoMP2Sem = materiasPrimas[f"{materia}"]["requerimientos"]["2Sem"] + \
                          materiasPrimas[f"{materia}"]["inventario"]["final"]
    requerimientoMP2Sem -= materiasPrimas[f"{materia}"]["inventario"]["inicial"]
    compraMP2Sem = requerimientoMP2Sem * materiasPrimas[f"{materia}"]["costos"]["2Sem"]
    compraMP = compraMP1Sem + compraMP2Sem
    compraTotal += compraMP
    materiasPrimas[f"{materia}"]["compra"]["1Sem"] = compraMP1Sem
    materiasPrimas[f"{materia}"]["compra"]["2Sem"] = compraMP2Sem
    materiasPrimas[f"{materia}"]["compra"]["total"] = compraMP
    # print(f"Compra de {materia} en el 1er semestre: ${compraMP1Sem:,.2f}")
    # print(f"Compra de {materia} en el 2do semestre: ${compraMP2Sem:,.2f}")
    print(f"Compra de {materia} en el año: ${compraMP:,.2f}")
    # print("")
print(f"Compra total de materias primas: ${compraTotal:,.2f}\n")

# Determinación del saldo de Proveedores y Flujo de Salidas
print("6.- Determinación del saldo de Proveedores y Flujo de Salidas")
# Saldo de Proveedores
totalProveedores = proveedoresESF + compraTotal
print(f"El saldo de proveedores es de: ${totalProveedores:,.2f}")

# Salidas de efectivo:
totalSalidas = (proveedoresESF * porcentajePagoESF) + (compraTotal * porcentajePagoActual)
print(f"El total de salidas es de: ${totalSalidas:,.2f}")

# Resultado de la Cuenta de Proveedores
saldoProveedores = totalProveedores - totalSalidas
print(f"El saldo de la cuenta de proveedores es de: ${saldoProveedores:,.2f}")

# Presupuesto de Mano de Obra Directa
print("\n7.- Presupuesto de Mano de Obra Directa")
totalHoras = 0
for producto in productos:
    horas1Sem = productos[f"{producto}"]["unidadesProducir"]["1Sem"] * productos[f"{producto}"]["requisitos"]["horas"]
    horas2Sem = productos[f"{producto}"]["unidadesProducir"]["2Sem"] * productos[f"{producto}"]["requisitos"]["horas"]
    totalHoras += horas1Sem + horas2Sem
    costoManoObra1Sem = horas1Sem * manoObra1Sem
    costoManoObra2Sem = horas2Sem * manoObra2Sem
    costoManoObra = costoManoObra1Sem + costoManoObra2Sem
    productos[f"{producto}"]["costoManoObra"] = {"1Sem": costoManoObra1Sem, "2Sem": costoManoObra2Sem,
                                                 "total": costoManoObra}
    # print(f"Costo de mano de obra del producto {producto} en el 1er semestre: ${costoManoObra1Sem:,.2f}")
    # print(f"Costo de mano de obra del producto {producto} en el 2do semestre: ${costoManoObra2Sem:,.2f}")
    print(f"Costo de mano de obra del producto {producto} en el año: ${costoManoObra:,.2f}")
    # print("")

# Presupuesto de Gastos Indirectos de Fabricación
print("\n8.- Presupuesto de Gastos Indirectos de Fabricación")
# Por semestre
depreciacionFI1Sem = depreciacionFI / 2
depreciacionFI2Sem = depreciacionFI / 2
segurosFI1Sem = segurosFI / 2
segurosFI2Sem = segurosFI / 2
variosFI1Sem = variosFI / 2
variosFI2Sem = variosFI / 2
totalGIF1Sem = depreciacionFI1Sem + segurosFI1Sem + + mantenimiento1Sem + energeticos1Sem + variosFI1Sem
totalGIF2Sem = depreciacionFI2Sem + segurosFI2Sem + mantenimiento2Sem + energeticos2Sem + variosFI2Sem
totalGIF = totalGIF1Sem + totalGIF2Sem
costoHoraGIF = totalGIF / totalHoras
print(f"Costo por hora de gastos indirectos de fabricación por hora: ${costoHoraGIF:,.2f}")

# Presupuesto de Gastos de Operación
print("\n9.- Presupuesto de Gastos de Operación")
totalGOP = depreciacionAV + sueldosYSalarios + (
            totalVentas * porcentajeComisiones) + variosAV1Sem + variosAV2Sem + interesesObligaciones
print(f"Total de gastos de operación: ${totalGOP:,.2f}")

# Determinación de Costo Unitario de Producto Terminado
print("\n10.- Determinación de Costo Unitario de Producto Terminado")
for producto in productos:
    costoMPT = 0
    for materia in materiasPrimas:
        costoMPT += productos[f"{producto}"]["requisitos"][f"{materia}"] * materiasPrimas[f"{materia}"]["costos"][
            "2Sem"]
    costoUnitarioPT = costoMPT + productos[f"{producto}"]["requisitos"]["horas"] * (costoHoraGIF + manoObra2Sem)
    productos[f"{producto}"]["costoUnitarioPT"] = costoUnitarioPT
    print(f"Costo unitario de producto terminado del producto {producto}: ${costoUnitarioPT:,.2f}")

# Valuación de inventarios finales
print("\n11.- Valuación de inventarios finales")
# Inventario de materias primas
print("Inventario de materias primas")
inventarioMPTotal = 0
for materia in materiasPrimas:
    inventarioMPT = materiasPrimas[f"{materia}"]["inventario"]["final"] * materiasPrimas[f"{materia}"]["costos"]["2Sem"]
    inventarioMPTotal += inventarioMPT
    print(f"Inventario de {materia}: ${inventarioMPT:,.2f}")
print(f"Inventario total de materias primas: ${inventarioMPTotal:,.2f}")

# Inventario de productos terminados
print("\nInventario de productos terminados")
inventarioPTTotal = 0
for producto in productos:
    inventarioPT = productos[f"{producto}"]["inventario"]["final"] * productos[f"{producto}"]["costoUnitarioPT"]
    inventarioPTTotal += inventarioPT
    print(f"Inventario de {producto}: ${inventarioPT:,.2f}")
print(f"Inventario total de productos terminados: ${inventarioPTTotal:,.2f}")

print("\nThe End.")
