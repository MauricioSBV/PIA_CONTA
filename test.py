from tabulate import tabulate

empresa = "Laboratorios Regionales S.A. de C.V."

print(f"Empresa: {empresa}")
print("Presupuestó Maestro\n")

# Registro de datos
print("Ingreso de datos del Estado de Situación Financiera\n")

# Activos
print("Ingreso de datos de los activos")
# Circulantes
print("Ingreso de datos de los activos circulantes")
efectivoESF = 50000.00
clientesESF = 50000.00
invMaterialesESF = 80005.00
invArticulosESF = 150000.00
totalCirculanteESF = efectivoESF + clientesESF + invMaterialesESF + invArticulosESF
print(f"El total de activos circulantes es: ${totalCirculanteESF:,.2f}\n")

# No Circulantes
print("Ingreso de datos de los activos no circulantes")
terrenoESF = 550000.00
plantaYEquipoESF = 1000000.00
depAcumESF = 50000.00
totalNoCirculanteESF = terrenoESF + plantaYEquipoESF - depAcumESF
print(f"El total de activos no circulantes es: ${totalNoCirculanteESF:,.2f}\n")

# Activo Total
activoTotalESF = totalCirculanteESF + totalNoCirculanteESF
print(f"El total de activos es: ${activoTotalESF:,.2f}\n")

# Pasivos
print("Ingreso de datos de los pasivos")
# Corto Plazo
print("Ingreso de datos de los pasivos a corto plazo\n")
proveedoresESF = 50000.00
documentosPorPagarESF = 100000.00
ISRPagarESF = 50000.00
pasivosCortoPlazoESF = proveedoresESF + documentosPorPagarESF + ISRPagarESF
print(f"El total de pasivos a corto plazo es: ${pasivosCortoPlazoESF:,.2f}\n")

# Largo Plazo
print("Ingreso de datos de los pasivos a largo plazo")
obligacionesESF = 150000.00
print(f"El total de pasivos a largo plazo es: ${obligacionesESF:,.2f}\n")

# Total Pasivo
pasivoTotalESF = proveedoresESF + documentosPorPagarESF + ISRPagarESF + obligacionesESF
print(f"El total de pasivos es: ${pasivoTotalESF:,.2f}\n")

# Capital Contable
print("Ingreso de datos del capital contable")
capitalAportadoESF = 1390380
# capitalGanadoESF = float(input("Ingrese el total de Capital ganado: "))
capitalGanadoESF = 89625.00
print(f"El total de capital ganado es: ${capitalGanadoESF:,.2f}")
totalCapitalESF = capitalAportadoESF + capitalGanadoESF
print(f"El total de capital contable es: ${totalCapitalESF:,.2f}\n")

print(f"El total de Pasivo y Capital Contable es: ${pasivoTotalESF + totalCapitalESF:,.2f}\n")

# numeroProductos = float(input("Ingrese el número de productos que fabrican: "))
numeroProductos = 3
# numeroMateriasPrimas = float(input("Ingrese el número de materias primas que necesitan: "))
numeroMateriasPrimas = 3

productos = {}
materiasPrimas = {}

# Información de Materias Primas
print("Ingreso de datos de las materias primas\n")

nombresMateriaPrima = ["Materia A", "Materia B", "Materia C"]
invInicialMateriaPrima = [10000, 15000, 5000]
invFinalMateriaPrima = [8000, 4000, 3000]
costoMateriaPrima1S = [2, 2.7, 4]
costoMateriaPrima2S = [2.1, 3, 4.4]

for num in range(numeroMateriasPrimas):
    nombreMP = nombresMateriaPrima[num]
    invInicialMP = invInicialMateriaPrima[num]
    invFinalMP = invFinalMateriaPrima[num]
    costoMP1S = costoMateriaPrima1S[num]
    costoMP2S = costoMateriaPrima2S[num]
    materiasPrimas[f"{nombreMP}"] = {"costos": {"1Sem": costoMP1S, "2Sem": costoMP2S},
                                     "inventario": {"inicial": invInicialMP, "final": invFinalMP},
                                     'requerimientos': {'1Sem': 0, '2Sem': 0, 'total': 0},
                                     'compra': {'1Sem': 0, '2Sem': 0, 'total': 0}}
    # print("")

# Información de Productos
print("Ingreso de datos de los productos\n")

nombresProductos = ["Producto D", "Producto Di", "Producto Z"]
invInicialProducto = [10000, 5000, 5000]
invFinalProducto = [7000, 3000, 2000]
precioProducto1Sem = [200, 100, 150]
precioProducto2Sem = [220, 120, 150]
ventasPlaneadas1Sem = [10000, 6000, 5000]
ventasPlaneadas2Sem = [5000, 4000, 5000]
horasElaboracion = [3, 1, 2]
requistiosMateriaPrima = [[15, 6, 9], [13, 7, 4], [10, 6, 5]]

for num in range(numeroProductos):
    nombreProducto = nombresProductos[num]
    invInicialProd = invInicialProducto[num]
    invFinalProd = invFinalProducto[num]
    precioProducto1S = precioProducto1Sem[num]
    precioProducto2S = precioProducto2Sem[num]
    ventasPlaneadas1S = ventasPlaneadas1Sem[num]
    ventasPlaneadas2S = ventasPlaneadas2Sem[num]

    productos[f"{nombreProducto}"] = {
        "precioVenta": {"1Sem": precioProducto1S, "2Sem": precioProducto2S},
        "ventasProyectadas": {"1Sem": ventasPlaneadas1S, "2Sem": ventasPlaneadas2S},
        "inventario": {"inicial": invInicialProd, "final": invFinalProd},
        'requisitos': {"horas": horasElaboracion[num]}
    }

    contador = 0
    for materia in materiasPrimas:
        productos[f"{nombreProducto}"]["requisitos"][f"{materia}"] = requistiosMateriaPrima[num][contador]
        contador += 1
    # print("")

print("Costo Mano de Obra")
manoObra1Sem = 10.00
manoObra2Sem = 11.00
# Gastos de administración y ventas
print("\nIngreso de datos de los gastos de administración y ventas")
depreciacionAV = 10000.00
sueldosYSalarios = 200000.00
porcentajeComisiones = 5
porcentajeComisiones = porcentajeComisiones / 100
variosAV1Sem = 6000.00
variosAV2Sem = 7000.00
interesesObligaciones = 30000.00

# Gastos de fabricación indirecta
print("\nIngreso de datos de los gastos de fabricación indirecta")

depreciacionFI = 100000.00
segurosFI = 5000.00
mantenimiento1Sem = 30000.00
mantenimiento2Sem = 35000.00
energeticos1Sem = 20000.00
energeticos2Sem = 32000.00
variosFI = 10000

# Datos Adicionales
print("\nIngreso de datos adicionales")
tasaISR = 35
tasaISR = tasaISR / 100
tasaUtilidad = 10
tasaUtilidad = tasaUtilidad / 100
porcentajeCobroClientesESF = 100
porcentajeCobroClientesESF = porcentajeCobroClientesESF / 100
porcentajeCobroClientesActual = 90
porcentajeCobroClientesActual = porcentajeCobroClientesActual / 100
porcentajePagoESF = 100
porcentajePagoESF = porcentajePagoESF / 100
porcentajePagoActual = 60
porcentajePagoActual = porcentajePagoActual / 100
pagoISRESF = "S"
pagoISRActual = "S"

print("I. Presupuesto de Operaciones.")

# Presupuesto de Ventas
# print("\n1.- Presupuesto de Ventas")
paso1 = [["1.- Presupuesto de Ventas", "", "", ""], ["", "1er Semestre", "2do Semestre", "Total"]]
ventas1SemTotal = 0
ventas2SemTotal = 0
totalVentas = 0
for producto in productos.items():
    ventas1Sem = producto[1]["ventasProyectadas"]["1Sem"] * producto[1]["precioVenta"]["1Sem"]
    ventas2Sem = producto[1]["ventasProyectadas"]["2Sem"] * producto[1]["precioVenta"]["2Sem"]
    ventas1SemTotal += ventas1Sem
    ventas2SemTotal += ventas2Sem
    totalVentas += ventas1Sem + ventas2Sem
    paso1.append([producto[0], "", "", ""])
    paso1.append(
        ["Unidades a Vender", f"${producto[1]['ventasProyectadas']['1Sem']:,.2f}",
         f"${producto[1]['ventasProyectadas']['2Sem']:,.2f}", ""])
    paso1.append(
        ["Precio de Venta", f"${producto[1]['precioVenta']['1Sem']:,.2f}",
         f"${producto[1]['precioVenta']['2Sem']:,.2f}", ""])
    paso1.append(
        ["Importe de Venta", f"${ventas1Sem:,.2f}", f"${ventas2Sem:,.2f}", f"${(ventas1Sem + ventas2Sem):,.2f}"])
    paso1.append(["", "", "", ""])
paso1.append(
    ["Total Ventas por Semestre", f"{ventas1SemTotal:,.2f}", f"{ventas2SemTotal:,.2f}", f"{totalVentas:,.2f}"])
print(tabulate(paso1, headers="firstrow", tablefmt="rounded_grid"))
# print(f"El total de ventas es de: ${totalVentas:,.2f}")

# Determinación del saldo de Clientes y Flujo de Entradas
# print("\n2.- Determinación del saldo de Clientes y Flujo de Entradas")
paso2 = [["2.- Determinación del saldo de Clientes y Flujo de Entradas", "", ""], ["Descripción", "Importe", "Total"],
         ["Saldo de Clientes al Inicio del Periodo", "", f"${clientesESF:,.2f}"],
         ["Total de Ventas", "", f"${totalVentas:,.2f}"]]
# Saldo de Clientes
totalClientes = clientesESF + totalVentas
paso2.append(["Saldo de Clientes al Final del Periodo", "", f"${totalClientes:,.2f}"])

# Entradas de efectivo:
# Cobro de Clientes
paso2.append(["", "", ""])
paso2.append(["Entradas de Efectivo", "", ""])
paso2.append(["Cobranza año anterior", f"${(clientesESF * porcentajeCobroClientesESF):,.2f}", ""])
paso2.append(["Cobranza año actual", f"${(totalVentas * porcentajeCobroClientesActual):,.2f}", ""])
totalEntradas = (clientesESF * porcentajeCobroClientesESF) + (totalVentas * porcentajeCobroClientesActual)
paso2.append(["Total de Entradas", "", f"${totalEntradas:,.2f}"])

# Resultado de la Cuenta de Clientes
saldoClientes = totalClientes - totalEntradas
paso2.append(["", "", ""])
paso2.append(["Resultado de la Cuenta de Clientes", "", f"${saldoClientes:,.2f}"])
print(tabulate(paso2, headers="firstrow", tablefmt="rounded_grid"))
# print(f"El saldo de clientes es de: ${saldoClientes:,.2f}")


# Presupuesto de producción
# print("\n3.- Presupuesto de producción")
paso3 = [["3.- Presupuesto de producción", "", "", ""], ["", "1er Semestre", "2do Semestre", "Total"]]
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
    paso3.append([producto, "", "", ""])
    paso3.append(
        ["Unidades a Vender", f"{productos[f'{producto}']['ventasProyectadas']['1Sem']:,}",
         f"{productos[f'{producto}']['ventasProyectadas']['2Sem']:,}",
         f"{(productos[f'{producto}']['ventasProyectadas']['1Sem'] + productos[f'{producto}']['ventasProyectadas']['2Sem']):,}"])
    paso3.append(
        ["(+) Inventario Final", f"{productos[f'{producto}']['inventario']['inicial']:,}",
         f"{productos[f'{producto}']['inventario']['final']:,}",
         f"{productos[f'{producto}']['inventario']['final']:,}"])
    paso3.append(
        ["(=) Total de Unidades",
         f"{(productos[f'{producto}']['inventario']['inicial'] + productos[f'{producto}']['ventasProyectadas']['1Sem']):,}",
         f"{(productos[f'{producto}']['inventario']['final'] + productos[f'{producto}']['ventasProyectadas']['2Sem']):,}",
         f"{((productos[f'{producto}']['ventasProyectadas']['1Sem'] + productos[f'{producto}']['ventasProyectadas']['2Sem']) + productos[f'{producto}']['inventario']['final']):,}"])
    paso3.append(
        ["(-) Inventario Inicial", f"{productos[f'{producto}']['inventario']['inicial']:,}",
         f"{productos[f'{producto}']['inventario']['inicial']:,}",
         f"{productos[f'{producto}']['inventario']['inicial']:,}"])
    paso3.append(
        ["(=) Unidades a Producir", f"{unidadesProducir1Sem:,}", f"{unidadesProducir2Sem:,}", f"{unidadesProducir:,}"])
    paso3.append(["", "", "", ""])
    # print(f"Unidades a producir del producto {producto} en el 1er semestre: {unidadesProducir1Sem} unidades.")
    # print(f"Unidades a producir del producto {producto} en el 2do semestre: {unidadesProducir2Sem} unidades.")
    # print(f"Unidades a producir del producto {producto} en el año: {unidadesProducir} unidades.")
    # print("")
paso3.pop()
print(tabulate(paso3, headers="firstrow", tablefmt="rounded_grid"))

# Presupuesto de requerimientos de materias primas
# print("\n4.- Presupuesto de requerimientos de materias primas")
paso4 = [["4.- Presupuesto de requerimientos de materias primas", "", "", ""],
         ["", "1er Semestre", "2do Semestre", "Total"]]
# Requerimientos de materias primas
for producto in productos:
    paso4.append([producto, "", "", ""])
    paso4.append(["Unidades a Producir", f"{productos[f'{producto}']['unidadesProducir']['1Sem']:,}",
                  f"{productos[f'{producto}']['unidadesProducir']['2Sem']:,}",
                  f"{productos[f'{producto}']['unidadesProducir']['total']:,}"])
    paso4.append(["", "", "", ""])
    for materia in materiasPrimas:
        requerimientoMP1Sem = productos[f"{producto}"]["unidadesProducir"]["1Sem"] * \
                              productos[f"{producto}"]["requisitos"][f"{materia}"]
        requerimientoMP2Sem = productos[f"{producto}"]["unidadesProducir"]["2Sem"] * \
                              productos[f"{producto}"]["requisitos"][f"{materia}"]
        requerimientoMP = requerimientoMP1Sem + requerimientoMP2Sem
        materiasPrimas[f"{materia}"]["requerimientos"]["1Sem"] += requerimientoMP1Sem
        materiasPrimas[f"{materia}"]["requerimientos"]["2Sem"] += requerimientoMP2Sem
        materiasPrimas[f"{materia}"]["requerimientos"]["total"] += requerimientoMP

        paso4.append(
            [f"Requerimiento de {materia}", f"{productos[f'{producto}']['requisitos'][f'{materia}']:,}",
             f"{productos[f'{producto}']['requisitos'][f'{materia}']:,}",
             f"{productos[f'{producto}']['requisitos'][f'{materia}']:,}"])
        paso4.append([f"Total requerido de {materia}",
                      f"{productos[f'{producto}']['requisitos'][f'{materia}'] * productos[f'{producto}']['unidadesProducir']['1Sem']:,}",
                      f"{productos[f'{producto}']['requisitos'][f'{materia}'] * productos[f'{producto}']['unidadesProducir']['2Sem']:,}",
                      f"{productos[f'{producto}']['requisitos'][f'{materia}'] * productos[f'{producto}']['unidadesProducir']['total']:,}"])
    paso4.append(["", "", "", ""])

paso4.append(["Total requerido de materias primas", "", "", ""])
for materia in materiasPrimas:
    paso4.append([f"{materia}", f"{materiasPrimas[f'{materia}']['requerimientos']['1Sem']:,}",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['2Sem']:,}",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['total']:,}"])
print(tabulate(paso4, headers="firstrow", tablefmt="rounded_grid"))

# Presupuesto de compra de materias primas
# print("\n5.- Presupuesto de compra de materias primas")
compraTotal1Sem = 0
compraTotal2Sem = 0
compraTotal = 0
paso5 = [["5.- Presupuesto de compra de materias primas", "", "", ""],
         ["", "1er Semestre", "2do Semestre", "Total"]]
for materia in materiasPrimas:
    paso5.append([f"{materia}", "", "", ""])
    paso5.append(["Requerimiento", f"{materiasPrimas[f'{materia}']['requerimientos']['1Sem']:,}",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['2Sem']:,}",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['total']:,}"])
    paso5.append(["(+) Inventario Final", f"{materiasPrimas[f'{materia}']['inventario']['inicial']:,}",
                  f"{materiasPrimas[f'{materia}']['inventario']['final']:,}",
                  f"{materiasPrimas[f'{materia}']['inventario']['final']:,}"])
    paso5.append(["Total requerido",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['1Sem'] + materiasPrimas[f'{materia}']['inventario']['inicial']:,}",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['2Sem'] + materiasPrimas[f'{materia}']['inventario']['inicial']:,}",
                  f"{materiasPrimas[f'{materia}']['requerimientos']['total'] + materiasPrimas[f'{materia}']['inventario']['final']:,}"])
    paso5.append(["(-) Inventario Inicial", f"{materiasPrimas[f'{materia}']['inventario']['inicial']:,}",
                  f"{materiasPrimas[f'{materia}']['inventario']['inicial']:,}",
                  f"{materiasPrimas[f'{materia}']['inventario']['inicial']:,}"])
    paso5.append(["Precio de Compra", f"${materiasPrimas[f'{materia}']['costos']['1Sem']:.2f}",
                  f"${materiasPrimas[f'{materia}']['costos']['2Sem']:.2f}",
                  ""])
    requerimientoMP1Sem = materiasPrimas[f"{materia}"]["requerimientos"]["1Sem"] + \
                          materiasPrimas[f"{materia}"]["inventario"]["inicial"]
    requerimientoMP1Sem -= materiasPrimas[f"{materia}"]["inventario"]["inicial"]
    compraMP1Sem = requerimientoMP1Sem * materiasPrimas[f"{materia}"]["costos"]["1Sem"]
    requerimientoMP2Sem = materiasPrimas[f"{materia}"]["requerimientos"]["2Sem"] + \
                          materiasPrimas[f"{materia}"]["inventario"]["final"]
    requerimientoMP2Sem -= materiasPrimas[f"{materia}"]["inventario"]["inicial"]
    compraMP2Sem = requerimientoMP2Sem * materiasPrimas[f"{materia}"]["costos"]["2Sem"]
    compraMP = compraMP1Sem + compraMP2Sem
    compraTotal1Sem += compraMP1Sem
    compraTotal2Sem += compraMP2Sem
    compraTotal += compraMP
    materiasPrimas[f"{materia}"]["compra"]["1Sem"] = compraMP1Sem
    materiasPrimas[f"{materia}"]["compra"]["2Sem"] = compraMP2Sem
    materiasPrimas[f"{materia}"]["compra"]["total"] = compraMP
    paso5.append(["Material a Comprar", f"{requerimientoMP1Sem:,.2f}", f"${requerimientoMP2Sem:,.2f}",
                  f"{requerimientoMP1Sem + requerimientoMP2Sem:,.2f}"])
    paso5.append([f"Total de {materia} en $", f"${compraMP1Sem:,.2f}", f"${compraMP2Sem:,.2f}", f"${compraMP:,.2f}"])
    paso5.append(["", "", "", ""])

paso5.append(["Compras Totales", f"${compraTotal1Sem:,.2f}", f"${compraTotal2Sem:,.2f}", f"${compraTotal:,.2f}"])
print(tabulate(paso5, headers="firstrow", tablefmt="rounded_grid"))

# 6.- Determinación del saldo de Proveedores y Flujo de Salidas
# print("6.- Determinación del saldo de Proveedores y Flujo de Salidas")
paso6 = [["6.- Determinación del saldo de Proveedores y Flujo de Salidas", "", ""],
         ["Descripción", "Importe", "Total"]]
# Saldo de Proveedores
totalProveedores = proveedoresESF + compraTotal
paso6.append([f"Saldo de Proveedores ESF", "", f"${proveedoresESF:,.2f}", ""])
paso6.append([f"Compras", "", f"${compraTotal:,.2f}"])
paso6.append([f"Total de Proveedores", "", f"${totalProveedores:,.2f}"])
paso6.append(["", "", ""])

# Salidas de efectivo:
totalSalidas = (proveedoresESF * porcentajePagoESF) + (compraTotal * porcentajePagoActual)
paso6.append([f"Salidas de Efectivo", "", ""])
paso6.append([f"Pago de Proveedores ESF", f"{proveedoresESF * porcentajePagoESF:,.2f}", ""])
paso6.append([f"Pago de Proveedores", f"{compraTotal * porcentajePagoActual:,.2f}", ""])
paso6.append([f"Total de Salidas", "", f"{totalSalidas:,.2f}"])
paso6.append(["", "", ""])

# Resultado de la Cuenta de Proveedores
saldoProveedores = totalProveedores - totalSalidas
paso6.append([f"Resultado de la Cuenta de Proveedores", "", f"{saldoProveedores:,.2f}"])
print(tabulate(paso6, headers="firstrow", tablefmt="rounded_grid"))

# 7.- Presupuesto de Mano de Obra Directa
paso7 = [["7.- Presupuesto de Mano de Obra Directa", "", "", ""],
         ["", "1er Semestre", "2do Semestre", "Total"]]

# Costo de mano de obra
totalHoras1Sem = 0
totalHoras2Sem = 0
totalHoras = 0
costoManoObraTotal1Sem = 0
costoManoObraTotal2Sem = 0
costoManoObraTotal = 0
for producto in productos:
    horas1Sem = productos[f"{producto}"]["unidadesProducir"]["1Sem"] * productos[f"{producto}"]["requisitos"]["horas"]
    totalHoras1Sem += horas1Sem
    horas2Sem = productos[f"{producto}"]["unidadesProducir"]["2Sem"] * productos[f"{producto}"]["requisitos"][f"horas"]
    totalHoras2Sem += horas2Sem
    totalHoras += horas1Sem + horas2Sem
    costoManoObra1Sem = horas1Sem * manoObra1Sem
    costoManoObraTotal1Sem += costoManoObra1Sem
    costoManoObra2Sem = horas2Sem * manoObra2Sem
    costoManoObraTotal2Sem += costoManoObra2Sem
    costoManoObra = costoManoObra1Sem + costoManoObra2Sem
    costoManoObraTotal += costoManoObra
    productos[f"{producto}"]["costoManoObra"] = {"1Sem": costoManoObra1Sem, "2Sem": costoManoObra2Sem,
                                                 "total": costoManoObra}
    paso7.append([f"{producto}", "", "", ""])
    paso7.append(["Unidades a Producir", f"{productos[f'{producto}']['unidadesProducir']['1Sem']:,}",
                  f"{productos[f'{producto}']['unidadesProducir']['2Sem']:,}",
                  f"{productos[f'{producto}']['unidadesProducir']['1Sem'] + productos[f'{producto}']['unidadesProducir']['2Sem']:,}"])
    paso7.append(["Horas por Unidad", f"{productos[f'{producto}']['requisitos']['horas']}",
                  f"{productos[f'{producto}']['requisitos']['horas']}",
                  f"{productos[f'{producto}']['requisitos']['horas']}"])
    paso7.append(["Horas Totales", f"{horas1Sem:,}", f"{horas2Sem:,}", f"{horas1Sem + horas2Sem:,}"])
    paso7.append(["Costo por Hora", f"${manoObra1Sem:,.2f}", f"${manoObra2Sem:,.2f}", ""])
    paso7.append(["Costo de Mano de Obra", f"${costoManoObra1Sem:,.2f}", f"${costoManoObra2Sem:,.2f}",
                  f"${costoManoObra:,.2f}"])
    paso7.append(["", "", "", ""])
paso7.append(["Total de Horas", f"{totalHoras1Sem:,}", f"{totalHoras2Sem:,}", f"{totalHoras:,}"])
paso7.append(["Costo Total de Mano de Obra", f"${costoManoObraTotal1Sem:,.2f}", f"${costoManoObraTotal2Sem:,.2f}",
              f"${costoManoObraTotal:,.2f}"])

print(tabulate(paso7, headers="firstrow", tablefmt="rounded_grid"))

# Presupuesto de Gastos Indirectos de Fabricación
# print("\n8.- Presupuesto de Gastos Indirectos de Fabricación")
paso8 = [["8.- Presupuesto de Gastos Indirectos de Fabricación", "", "", ""],
         ["", "1er Semestre", "2do Semestre", "Total"]]
# Por semestre
depreciacionFI1Sem = depreciacionFI / 2
depreciacionFI2Sem = depreciacionFI / 2
paso8.append([f"Depreciación", f"${depreciacionFI1Sem:,.2f}", f"${depreciacionFI2Sem:,.2f}",
              f"${depreciacionFI:,.2f}"])
segurosFI1Sem = segurosFI / 2
segurosFI2Sem = segurosFI / 2
paso8.append([f"Seguros", f"${segurosFI1Sem:,.2f}", f"${segurosFI2Sem:,.2f}", f"${segurosFI:,.2f}"])
variosFI1Sem = variosFI / 2
variosFI2Sem = variosFI / 2
paso8.append(["Mantenimiento", f"${mantenimiento1Sem:,.2f}", f"${mantenimiento2Sem:,.2f}",
              f"${mantenimiento1Sem + mantenimiento2Sem:,.2f}"])
paso8.append(["Energéticos", f"${energeticos1Sem:,.2f}", f"${energeticos2Sem:,.2f}",
              f"${energeticos1Sem + energeticos2Sem:,.2f}"])
paso8.append(["Varios", f"${variosFI1Sem:,.2f}", f"${variosFI2Sem:,.2f}", f"${variosFI:,.2f}"])
totalGIF1Sem = depreciacionFI1Sem + segurosFI1Sem + + mantenimiento1Sem + energeticos1Sem + variosFI1Sem
totalGIF2Sem = depreciacionFI2Sem + segurosFI2Sem + mantenimiento2Sem + energeticos2Sem + variosFI2Sem
totalGIF = totalGIF1Sem + totalGIF2Sem
paso8.append(["Total", f"${totalGIF1Sem:,.2f}", f"${totalGIF2Sem:,.2f}", f"${totalGIF:,.2f}"])

# Determinar costo por hora
costoHoraGIF = totalGIF / totalHoras
paso8.append(["", "", "", ""])
paso8.append(["Total de GIF", "", "", f"${totalGIF:,.2f}"])
paso8.append(["(/) Total de Horas", "", "", f"{totalHoras:,}"])
paso8.append(["Costo por Hora", "", "", f"${costoHoraGIF:,.2f}"])

print(tabulate(paso8, headers="firstrow", tablefmt="rounded_grid"))

# Presupuesto de Gastos de Operación
paso9 = [["9.- Presupuesto de Gastos de Operación", "", "", ""],
         ["", "1er Semestre", "2do Semestre", "Total"]]

depreciacionAV1Sem = depreciacionAV / 2
depreciacionAV2Sem = depreciacionAV / 2
paso9.append(["Depreciación", f"${depreciacionAV1Sem:,.2f}", f"${depreciacionAV2Sem:,.2f}",
              f"${depreciacionAV:,.2f}"])
sueldosYSalarios1Sem = sueldosYSalarios / 2
sueldosYSalarios2Sem = sueldosYSalarios / 2
paso9.append(["Sueldos y Salarios", f"${sueldosYSalarios1Sem:,.2f}", f"${sueldosYSalarios2Sem:,.2f}",
              f"${sueldosYSalarios:,.2f}"])
print(totalVentas)
print(porcentajeComisiones)
comisionesTotal = totalVentas * porcentajeComisiones
comisiones1Sem = ventas1SemTotal * porcentajeComisiones
comisiones2Sem = ventas2SemTotal * porcentajeComisiones
paso9.append(["Comisiones", f"${comisiones1Sem:,.2f}", f"${comisiones2Sem:,.2f}",
              f"${comisionesTotal:,.2f}"])
paso9.append(["Varios", f"${variosAV1Sem:,.2f}", f"${variosAV2Sem:,.2f}",
              f"${variosAV1Sem + variosAV2Sem:,.2f}"])
interesesObligaciones1Sem = interesesObligaciones / 2
interesesObligaciones2Sem = interesesObligaciones / 2
paso9.append(["Intereses por Obligaciones", f"${interesesObligaciones1Sem:,.2f}", f"${interesesObligaciones2Sem:,.2f}",
              f"${interesesObligaciones1Sem + interesesObligaciones2Sem:,.2f}"])
totalGOP1Sem = depreciacionAV1Sem + sueldosYSalarios1Sem + comisiones1Sem + variosAV1Sem + interesesObligaciones1Sem
totalGOP2Sem = depreciacionAV2Sem + sueldosYSalarios2Sem + comisiones2Sem + variosAV2Sem + interesesObligaciones2Sem
totalGOP = depreciacionAV + sueldosYSalarios + (
        totalVentas * porcentajeComisiones) + variosAV1Sem + variosAV2Sem + interesesObligaciones
paso9.append(["Total", f"${totalGOP1Sem:,.2f}", f"${totalGOP2Sem:,.2f}", f"${totalGOP:,.2f}"])

print(tabulate(paso9, headers="firstrow", tablefmt="rounded_grid"))

# Determinación de Costo Unitario de Producto Terminado
paso10 = [["10.- Determinación de Costo Unitario de Producto Terminado", "", "", ""]]

for producto in productos:
    costoMPT = 0
    paso10.append(["", "", f"{producto}", ""])
    paso10.append(["Descripción", "Costo", "Cantidad", "Costo Unitario"])

    for materia in materiasPrimas:
        costoMPT += productos[f"{producto}"]["requisitos"][f"{materia}"] * materiasPrimas[f"{materia}"]["costos"][
            "2Sem"]
        paso10.append([f"{materia}", f"${materiasPrimas[f'{materia}']['costos']['2Sem']:,.2f}",
                       f"{productos[f'{producto}']['requisitos'][f'{materia}']}",
                       f"${materiasPrimas[f'{materia}']['costos']['2Sem'] * productos[f'{producto}']['requisitos'][f'{materia}']:,.2f}"])
    paso10.append(["Mano de Obra", f"${manoObra2Sem:,.2f}", f"{productos[f'{producto}']['requisitos']['horas']}",
                   f"${manoObra2Sem * productos[f'{producto}']['requisitos']['horas']:,.2f}"])
    paso10.append(["Gastos Indirectos de Fabricación", f"${costoHoraGIF:,.2f}",
                   f"{productos[f'{producto}']['requisitos']['horas']}",
                   f"${costoHoraGIF * productos[f'{producto}']['requisitos']['horas']:,.2f}"])
    paso10.append(["", "", "", ""])
    costoUnitarioPT = costoMPT + productos[f"{producto}"]["requisitos"]["horas"] * (costoHoraGIF + manoObra2Sem)
    paso10.append(["Costo Unitario", "", "", f"${costoUnitarioPT:,.2f}"])
    productos[f"{producto}"]["costoUnitarioPT"] = costoUnitarioPT

print(tabulate(paso10, headers="firstrow", tablefmt="rounded_grid"))

# Valuación de inventarios finales
# print("\n11.- Valuación de inventarios finales")
paso11 = [["11.- Valuación de inventarios finales", "", "", ""]]
# Inventario de materias primas
paso11.append(["", "Inventario Final de Materiales", "", ""])
paso11.append(["Descripción", "Unidades", "Costo Unitario", "Costo Total"])
inventarioMPTotal = 0
for materia in materiasPrimas:
    inventarioMPT = materiasPrimas[f"{materia}"]["inventario"]["final"] * materiasPrimas[f"{materia}"]["costos"]["2Sem"]
    inventarioMPTotal += inventarioMPT
    paso11.append([f"{materia}", f"{materiasPrimas[f'{materia}']['inventario']['final']}",
                     f"${materiasPrimas[f'{materia}']['costos']['2Sem']:,.2f}",
                        f"${inventarioMPT:,.2f}"])

# Inventario de productos terminados
paso11.append(["", "", "", ""])
paso11.append(["", "Inventario Final de Productos Terminados", "", ""])
paso11.append(["Descripción", "Unidades", "Costo Unitario", "Costo Total"])
inventarioPTTotal = 0
for producto in productos:
    inventarioPT = productos[f"{producto}"]["inventario"]["final"] * productos[f"{producto}"]["costoUnitarioPT"]
    inventarioPTTotal += inventarioPT
    paso11.append([f"{producto}", f"{productos[f'{producto}']['inventario']['final']}",
                     f"${productos[f'{producto}']['costoUnitarioPT']:,.2f}",
                        f"${inventarioPT:,.2f}"])

print(tabulate(paso11, headers="firstrow", tablefmt="rounded_grid"))

print("II.- Presupuesto Financiero")
presupestoFinanciero = [["", "Estado de Costo de Producción y Ventas", ""]]
#Estado de Costo de Producción y Ventas
presupestoFinanciero.append(["", "", ""])
presupestoFinanciero.append(["Saldo Inicial de Materiales", "", f"${invMaterialesESF:,.2f}"])
presupestoFinanciero.append(["(+) Compras de Materiales", "", f"${compraTotal:,.2f}"])
presupestoFinanciero.append(["(=) Material Disponible", "", f"${invMaterialesESF + compraTotal:,.2f}"])
presupestoFinanciero.append(["(-) Inventario Final de Materiales", "", f"${inventarioMPTotal:,.2f}"])
presupestoFinanciero.append(["(=) Materiales Utilizados", "", f"${invMaterialesESF + compraTotal - inventarioMPTotal:,.2f}"])
presupestoFinanciero.append(["Mano de Obra Directa", "", f"${costoManoObraTotal:,.2f}"])
print(tabulate(presupestoFinanciero, headers="firstrow", tablefmt="rounded_grid"))

print("\nThe End.")
