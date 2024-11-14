import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def format_currency(value):
    """
    Formatea un valor numérico a una cadena de texto representativa en términos de miles o millones, 
    dependiendo de su magnitud.

    Parámetros:
    value (float): El valor numérico a formatear.
    Retorna:
    str: El valor formateado como una cadena de texto. Si el valor es mayor o igual a un millón, 
         se expresa en millones con dos decimales. Si es mayor o igual a mil, se expresa en miles 
         con dos decimales. Si es menor a mil, se formatea simplemente con dos decimales.
    """
    if value >= 1_000_000:
        return f"{value / 1_000_000:,.2f} millones"
    elif value >= 1_000:
        return f"{value / 1_000:,.2f} mil"
    else:
        return f"{value:,.2f}"


VENTAS1 = {
      'listarVentas': [
        {
            'id': 'venta1',
            'fecha': '2024-01-15',
            'monto': 500.00,
            'clienteId': 'cliente1',
            'vendedorId': 'vendedor1',
            'cajeroId': 'cajero1',
            'detalles': [
                {'id': 'detalle1', 'producto': {'id': 'prod1', 'nombre': 'Refrigerador', 'precio': 300.00}, 'cantidad': 1},
                {'id': 'detalle2', 'producto': {'id': 'prod2', 'nombre': 'Licuadora', 'precio': 100.00}, 'cantidad': 2}
            ]
        },
        {
            'id': 'venta2',
            'fecha': '2024-01-16',
            'monto': 200.00,
            'clienteId': 'cliente2',
            'vendedorId': 'vendedor2',
            'cajeroId': 'cajero1',
            'detalles': [
                {'id': 'detalle3', 'producto': {'id': 'prod3', 'nombre': 'Microondas', 'precio': 200.00}, 'cantidad': 1}
            ]
        },
        {
            'id': 'venta3',
            'fecha': '2024-01-17',
            'monto': 150.00,
            'clienteId': 'cliente3',
            'vendedorId': 'vendedor1',
            'cajeroId': 'cajero2',
            'detalles': [
                {'id': 'detalle4', 'producto': {'id': 'prod4', 'nombre': 'Tostadora', 'precio': 75.00}, 'cantidad': 2}
            ]
        },
        {
            'id': 'venta4',
            'fecha': '2024-01-18',
            'monto': 300.00,
            'clienteId': 'cliente4',
            'vendedorId': 'vendedor3',
            'cajeroId': 'cajero1',
            'detalles': [
                {'id': 'detalle5', 'producto': {'id': 'prod5', 'nombre': 'Horno', 'precio': 150.00}, 'cantidad': 2}
            ]
        },
        {
            'id': 'venta5',
            'fecha': '2024-01-19',
            'monto': 250.00,
            'clienteId': 'cliente5',
            'vendedorId': 'vendedor2',
            'cajeroId': 'cajero2',
            'detalles': [
                {'id': 'detalle6', 'producto': {'id': 'prod6', 'nombre': 'Aspiradora', 'precio': 250.00}, 'cantidad': 1}
            ]
        }
    ]
}

PAGOS1 = {
        'listarPagos': [
        {
            'id': 'pago1',
            'monto': 500.00,
            'metodoPago': 'Efectivo',
            'descripcion': 'Pago completo de venta1',
            'fecha': '2024-01-15',
            'venta': {'id': 'venta1', 'monto': 500.00, 'clienteId': 'cliente1', 'vendedorId': 'vendedor1', 'cajeroId': 'cajero1'}
        },
        {
            'id': 'pago2',
            'monto': 200.00,
            'metodoPago': 'Transferencia',
            'descripcion': 'Pago completo de venta2',
            'fecha': '2024-01-16',
            'venta': {'id': 'venta2', 'monto': 200.00, 'clienteId': 'cliente2', 'vendedorId': 'vendedor2', 'cajeroId': 'cajero1'}
        },
        {
            'id': 'pago3',
            'monto': 150.00,
            'metodoPago': 'Depósito',
            'descripcion': 'Pago completo de venta3',
            'fecha': '2024-01-17',
            'venta': {'id': 'venta3', 'monto': 150.00, 'clienteId': 'cliente3', 'vendedorId': 'vendedor1', 'cajeroId': 'cajero2'}
        },
        {
            'id': 'pago4',
            'monto': 300.00,
            'metodoPago': 'Efectivo',
            'descripcion': 'Pago completo de venta4',
            'fecha': '2024-01-18',
            'venta': {'id': 'venta4', 'monto': 300.00, 'clienteId': 'cliente4', 'vendedorId': 'vendedor3', 'cajeroId': 'cajero1'}
        },
        {
            'id': 'pago5',
            'monto': 250.00,
            'metodoPago': 'Transferencia',
            'descripcion': 'Pago completo de venta5',
            'fecha': '2024-01-19',
            'venta': {'id': 'venta5', 'monto': 250.00, 'clienteId': 'cliente5', 'vendedorId': 'vendedor2', 'cajeroId': 'cajero2'}
        }
    ]
    }
#funciona
def obtener_cantidad_empleados(empleados):
    cantidad_empleados = len(empleados['obtenerEmpleados'])
    if cantidad_empleados == None:
        cantidad_empleados = 0
    return cantidad_empleados

def obtener_cantidad_clientes(clientes):
    cantidad_clientes = len(clientes['obtenerClientes'])
    if cantidad_clientes == None:
        cantidad_clientes = 0
    return cantidad_clientes

def obtener_cantidad_productos(productos):
    cantidad_productos = len(productos['obtenerProductos'])
    if cantidad_productos == None:
        cantidad_productos = 0
    return cantidad_productos

def grafico_ventas_categoria(ventas):

    if ventas == "" :
        ventas = VENTAS1
    
    # Lista para almacenar los datos procesados
    ventas_por_categoria = []

    # Iterar sobre las ventas y procesar los detalles
    for venta in ventas['listarVentas']:
        for detalle in venta['detalles']:
            producto = detalle['producto']
            categoria = producto['nombre']  # Asumiendo que el nombre del producto es la categoría
            monto_venta = producto['precio'] * detalle['cantidad']
            ventas_por_categoria.append({
                'categoria': categoria,
                'monto_venta': monto_venta
            })

    # Crear un DataFrame con los datos procesados
    df = pd.DataFrame(ventas_por_categoria)

    # Sumar las ventas por categoría
    #df_ventas = df.groupby('categoria').agg({'monto_venta': 'sum'}).reset_index()
    df_ventas = df.groupby('categoria')['monto_venta'].sum().reset_index()

    # Crear el gráfico
    fig = px.bar(
        df_ventas, 
        x='categoria', 
        y='monto_venta', 
        labels={'categoria': 'Categoría', 'monto_venta': 'Total'},
        color='categoria',
        color_discrete_sequence=px.colors.qualitative.Prism ,
        height=400 
    )
      # Configuración de diseño
    fig.update_layout(
        height=380,
        plot_bgcolor='black', 
        paper_bgcolor='black', 
        font=dict(color='white')  
    )
    # Ocultar etiquetas del eje X
    fig.update_layout(xaxis=dict(showticklabels=False))

    # Convertir el gráfico a HTML
    graph = fig.to_html(full_html=False)
    
    return graph


def grafico_ventas_pagos(pagos): 

    if pagos =="":
        pagos= PAGOS1

    pagos_por_metodo = []

    # Procesar cada pago y extraer el monto y método de pago
    for pago in pagos['listarPagos']:
        metodo_pago = pago['metodoPago']
        monto = pago['monto']
        pagos_por_metodo.append({'metodo_pago': metodo_pago, 'monto': monto})

    # Crear un DataFrame con los datos procesados
    df = pd.DataFrame(pagos_por_metodo)

    # Sumar los montos por método de pago
    df_montos = df.groupby('metodo_pago')['monto'].sum().reset_index()

    # Crear el gráfico de torta
    fig = px.pie(
        df_montos, 
        names='metodo_pago', 
        values='monto',
        color_discrete_sequence=px.colors.qualitative.Prism
    )

    # Ajustar diseño del gráfico
    fig.update_layout(
        height=290,
        showlegend=True,
                legend=dict(
            orientation="h",  
            yanchor="bottom",
            y=-0.5,
            xanchor="center",
            x=0.5
        ),
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white')
    )

    # Convertir el gráfico a HTML
    graph = fig.to_html(full_html=False)
    
    return graph

def productos_mas_vendidos_pareto(ventas):
    
    if ventas == "":
        ventas = VENTAS1
    # Lista para almacenar los datos de productos y cantidades
    productos_cantidades = []

    # Recorrer cada venta y los detalles de productos
    for venta in ventas['listarVentas']:
        for detalle in venta['detalles']:
            producto = detalle['producto']
            cantidad = detalle['cantidad']
            productos_cantidades.append({
                'producto': producto['nombre'],
                'cantidad': cantidad
            })

    # Crear un DataFrame para agrupar y sumar las cantidades por producto
    df = pd.DataFrame(productos_cantidades)
    productos_agrupados = df.groupby('producto')['cantidad'].sum().reset_index()

    # Ordenar los productos por cantidad en orden descendente
    productos_agrupados = productos_agrupados.sort_values(by='cantidad', ascending=False)

    # Calcular el porcentaje acumulado
    productos_agrupados['porcentaje_acumulado'] = productos_agrupados['cantidad'].cumsum() / productos_agrupados['cantidad'].sum() * 100

    # Crear el gráfico de Pareto
    fig = go.Figure()

    # Añadir las barras (cantidad vendida por producto)
    fig.add_trace(go.Bar(
        x=productos_agrupados['producto'],
        y=productos_agrupados['cantidad'],
        name='Cantidad Vendida',
        marker_color='blue'
    ))

    # Añadir la línea del porcentaje acumulado
    fig.add_trace(go.Scatter(
        x=productos_agrupados['producto'],
        y=productos_agrupados['porcentaje_acumulado'],
        name='Porcentaje Acumulado',
        yaxis='y2',
        mode='lines+markers',
        line=dict(color='orange')
    ))

    # Configuración de diseño
    fig.update_layout(
        title="Gráfico de Pareto: Productos Más Vendidos",
        xaxis=dict(title="Producto"),
        yaxis=dict(title="Cantidad Vendida"),
        yaxis2=dict(title="Porcentaje Acumulado", overlaying='y', side='right'),
        plot_bgcolor='black', 
        paper_bgcolor='black',
        font=dict(color='white')
    )
      # Convertir el gráfico a HTML
    graph = fig.to_html(full_html=False)
    
    return graph


def calcular_bonificaciones(ventas, porcentaje_bonificacion=0.05):
    
    if ventas=="":
        ventas= VENTAS1

   # Crear lista para almacenar información de ventas con bonificación por vendedor
    ventas_por_vendedor = []

    # Calcular la bonificación para cada venta y sumar ventas por vendedor
    for venta in ventas['listarVentas']:
        vendedor = venta['vendedorId']
        monto_venta = venta['monto']
        bonificacion = monto_venta * porcentaje_bonificacion
        ventas_por_vendedor.append({'vendedor': vendedor, 'monto_venta': monto_venta, 'bonificacion': bonificacion})

    # Convertir a DataFrame
    df_ventas = pd.DataFrame(ventas_por_vendedor)

    # Agrupar por vendedor, sumando montos y bonificaciones
    df_vendedores = df_ventas.groupby('vendedor').agg(
        total_ventas=('monto_venta', 'sum'),
        total_bonificacion=('bonificacion', 'sum')
    ).reset_index()

    # Seleccionar los tres vendedores con más ventas
    top_vendedores = df_vendedores.nlargest(3, 'total_ventas')

    # Crear gráfico de barras
    fig = px.bar(
        top_vendedores,
        x='vendedor',
        y=['total_ventas', 'total_bonificacion'],
        labels={'value': 'Monto ($)', 'vendedor': 'Vendedor'},
        barmode='group'
    )

    # Configuración de diseño
    fig.update_layout(
        height=400,
        plot_bgcolor='black',
        paper_bgcolor='black',
        font=dict(color='white')
    )

    # Convertir gráfico a HTML
    graph = fig.to_html(full_html=False)
    return graph

    """
    Calcula el total de ventas y lo devuelve en un formato legible (miles o millones).

    Parámetros:
    df (pandas.DataFrame): El DataFrame que contiene una columna 'Total' con los valores de las ventas.

    Retorna:
    str: El total de ventas, formateado en miles o millones, dependiendo del valor.
    """
    
    total_monto = df['Monto Total'].sum()
    total_monto_formatted = format_currency(total_monto )
    return total_monto_formatted


def calcular_monto_total_ventas(ventas):
    
    if ventas =="":
        ventas =VENTAS1

    # Sumar los montos de todas las ventas
    monto_total = sum(venta['monto'] for venta in ventas['listarVentas'])
    return monto_total

def obtener_cantidad_empleados_excel(df):
    return df['Empleado'].nunique()

def obtener_cantidad_categorias(categorias):
    cantidad_categorias = len(categorias)
    return cantidad_categorias

def obtener_cantidad_categorias_excel(df):
    return df['Categoría'].nunique()

    
def obtener_cantidad_productos_excel(df):
    return df['Producto'].nunique()


def graph_categorias(df):
    """
    Genera un gráfico de torta de las ventas totales agrupadas por sucursales.
    
    Parámetros:
    df (pd.DataFrame): Un DataFrame de pandas que contiene los datos de ventas, 
                       con una columna llamada 'Total' que representa el total de ventas
                       y una columna 'Sucursal' que indica la sucursal de las ventas.

    Retorna:
    str: Un gráfico de torta en formato HTML generado con plotly.                       
    """
    #Convierte la columna 'Total' a un tipo numérico para asegurarse de que los valores sean números.
    df['Monto Total'] = pd.to_numeric(df['Monto Total'], errors='coerce')

    #Agrupa los datos por la columna 'Categoría' y suma los valores de la columna 'Total' para cada sucursal.
    ventas_por_categoria = df.groupby('Categoría')['Monto Total'].sum().reset_index()
    
    # Generación del gráfico de torta
    fig = px.pie(
        ventas_por_categoria, 
        names='Categorias',       
        values='Total',        
        labels={'Categoría': 'Categoría', 'Total': 'Total de Ventas'},
        color_discrete_sequence=px.colors.sequential.RdBu  # Esquema de color
    )

    # Añadir más configuraciones para controlar la posición del texto
    fig.update_traces(
        textposition='outside',    
        textinfo='label+percent' 
    )

    # Configuración de diseño
    fig.update_layout(
        height=200,
        showlegend=False,
        margin=dict(t=0, b=0, l=0, r=0),  # Ajustar márgenes: reducir espacio superior e inferior
        title_y=0.55,
        plot_bgcolor='black', 
        paper_bgcolor='black',
        font=dict(color='white')
    )

    fig.update_layout(xaxis=dict(showticklabels=False))
    
    # Convertir el gráfico a HTML
    grafico_torta_html = fig.to_html(full_html=False)

    return grafico_torta_html

