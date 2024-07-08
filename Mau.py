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

productos = {}

numeroProductos = validacionInt("Ingrese el número de productos que se fabrican: ")


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
    }

print("\n7.- Presupuesto de Mano de Obra Directa")

manoDeObra1Sem = validacionFloat("Ingrese el costo de la mano de obra por hora del 1er semestre: ")
manoDeObra2Sem = validacionFloat("Ingrese el costo de la mano de obra por hora del 2do semestre: ")
totalHoras = 0

for producto in productos:
    horas1Sem = productos[f"{producto}"]["unidadesProducir"]["1Sem"] * productos[f"{producto}"]["requisitos"]["horas"]
    horas2Sem = productos[f"{producto}"]["unidadesProducir"]["2Sem"] * productos[f"{producto}"]["requisitos"]["horas"]
    totalHoras += horas1Sem + horas2Sem
    costoMDO1Sem = horas1Sem * manoDeObra1Sem
    costoMDO2Sem = horas2Sem * manoDeObra2Sem
    cuota_total_mdo = costoMDO1Sem + costoMDO2Sem
    productos[f"{producto}"]["costoManoObra"] = {"1Sem": costoMDO1Sem, "2Sem": costoMDO2Sem,
                                                 "total": cuota_total_mdo}
    print(f"Costo de mano de obra del producto {producto} en el año: ${cuota_total_mdo:,.2f}")