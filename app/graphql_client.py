from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
    
# Configuración del cliente para el microservicio auth Spring Boot
def create_graphql_client():
    transport = RequestsHTTPTransport(
        url="http://localhost:9091/graphql",  # URL del servicio GraphQL de Spring Boot
        use_json=True,
    )
    
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client


# Convertir la consulta a gql y ejecutar con las variables proporcionadas
def fetch_data(query, variables=None):
    try:
        client = create_graphql_client()
        query = gql(query)
        result = client.execute(query, variable_values=variables)
        return result
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None



# Configuración del cliente para el microservicio producto Spring Boot
def create_graphql_client_productos():
    transport = RequestsHTTPTransport(
        url="http://localhost:8001/graphql",  # URL del servicio GraphQL de Spring Boot
        use_json=True,
    )
    
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client

# Convertir la consulta a gql y ejecutar con las variables proporcionadas
def fetch_data_producto(query, variables=None):
    try:
        client = create_graphql_client_productos()
        query = gql(query)
        result = client.execute(query, variable_values=variables)
        return result
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
