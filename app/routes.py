from flask import Blueprint, jsonify, request, render_template, redirect, url_for
import requests
from .graphql_client import fetch_data, fetch_data_producto
import logging
from .utils.graficos import * 
main_routes = Blueprint('main', __name__)

@main_routes.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')  

@main_routes.route('/dashboard/', methods=['GET'])
def dashboard():
    
    clientes = obtenerClientes()
    empleados = obtenerEmpleados()
    pagos= obtenerPagos()
    productos = obtenerProductos()
    ventas = obtenerVentas()

    if not clientes:
        clientes =""
    
    if not empleados:
        empleados =""

    if not productos:
        productos= ""
    if not ventas:
        ventas =""
    if not pagos:
        pagos = ""

#    cantidad_productos = obtener_cantidad_productos(productos)
    grafico_categoria = grafico_ventas_categoria(ventas)

    grafico_tipo_pagos = grafico_ventas_pagos(pagos)
    grafico_bonificaciones = calcular_bonificaciones(ventas)
    grafico_productos_vendidos = productos_mas_vendidos_pareto(ventas)
    monto_total = calcular_monto_total_ventas(ventas)
    # return render_template('dashboard.html',clientes =clientes, empleados =empleados)
    return render_template('dashboard.html', 
                          #empleados= empleados, 
                          #cantidad_empledos=cantidad_empledos,
                          grafico_categoria =grafico_categoria,
                          grafico_tipo_pagos =grafico_tipo_pagos,
                          grafico_bonificaciones=grafico_bonificaciones,
                          grafico_productos_vendidos = grafico_productos_vendidos,
                          monto_total= monto_total
                          )

@main_routes.route('/login', methods=['POST'])
def login():   
    email =  request.form.get("email")
    password =  request.form.get("password")
    response = inicioSesion(email, password)
    # Verificar si la respuesta es exitosa y devolverla
    if "login" in response:
        token = response["login"]["token"]
        user = response["login"]["user"]
        return jsonify({
            "message": "Login exitoso",
            "token": token,
            "id": user["id"],
            "nombre": user["nombre"],
            "email": user["email"]
        }), 200
    else:
        return jsonify({"error": "Error en la autenticación"}), 401

def inicioSesion(email, password):
    # Definir la mutación como una plantilla sin valores directos
    mutation = """
        mutation login($email: String!, $password: String!) {
          login(email: $email, password: $password) {
            token
            user {
              id
              nombre
              apellidos
              email
              imageUrl
              roles {
                name
              }
            }
          }
        }
    """
    
    # Crear las variables de la mutación
    variables = {
        "email": email,
        "password": password
    }
    
    # Llamar a fetch_data con la mutación y las variables
    response = fetch_data(mutation, variables)
    return response
    
def obtenerClientes():
    queryCliente = """
    query {
            obtenerClientes {
              id
              nombre
              apellidos
              email
              telefono
              direccion
              imageUrl
            }
          }
    """
    
    clientes = fetch_data(queryCliente)
    return clientes

def obtenerEmpleados():
    queryEmpleado = """
    query {
            obtenerEmpleados {
              id
              nombre
              apellidos
              email
              telefono
              direccion
            }
          }
    """    
    empleados = fetch_data(queryEmpleado)
    return empleados

def obtenerProductos():
    queryProducto = """
        query {
          listarProductos {
            id,
            nombre,
            descripcion,
            precio,
            stock,
            estado,
            foto_url,
            longitud,
            ancho,
            altura,
            peso,
            categoria{
              id,
              nombre
            },
            marca {
              id,
              nombre
            }
          }
        }
    """    
    productos = fetch_data_producto(queryProducto)
    return productos

def obtenerCaterorias():
    queryCategoria = """
    query {
            obtenerCategorias {
              id
              nombre
            }
          }
    """    
    categorias = fetch_data(queryCategoria)
    return categorias

def obtenerMarcas():  
    queryMarca = """
    query {
            obtenerMarcas {
              id
              nombre
            }
          }
    """    
    marcas = fetch_data(queryMarca)
    return marcas

def obtenerVentas():
    queryVenta = """
     query {
            listarVentas {
              id
              fecha
              monto
              clienteId
              vendedorId
              cajeroId
              detalles {
                id
                producto {
                  id
                  nombre
                  precio
                }
                cantidad
              }
            }
          }
    """    
    ventas = fetch_data_producto(queryVenta)
    return ventas

def obtenerPagos():
    queryPago = """
      query {
            listarPagos {
              id
              monto
              metodoPago
              descripcion
              fecha
              venta {
                id
                monto
                clienteId
                vendedorId
                cajeroId
                detalles {
                  producto {
                    id
                    nombre
                    precio
                  }
                  cantidad
                }
              }
            }
          }
    """    
    pagos = fetch_data_producto(queryPago)
    return pagos

