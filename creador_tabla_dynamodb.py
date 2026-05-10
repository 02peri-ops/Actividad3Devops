# 06_crear_tabla_dynamodb.py
import boto3
import time

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
TABLA = 'lab-productos'

def crear_tabla():
    try:
        respuesta = dynamodb.create_table(
            TableName=TABLA,
            # Clave primaria compuesta: Partition Key + Sort Key
            KeySchema=[
                {'AttributeName': 'producto_id', 'KeyType': 'HASH'},   # Partition Key
                {'AttributeName': 'categoria',   'KeyType': 'RANGE'}   # Sort Key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'producto_id', 'AttributeType': 'S'},  # String
                {'AttributeName': 'categoria',   'AttributeType': 'S'}   # String
            ],
            BillingMode='PAY_PER_REQUEST',  # On-demand: sin capacidad provisionada
            Tags=[
                {'Key': 'Proyecto', 'Value': 'LabAWS'},
                {'Key': 'Entorno',  'Value': 'Desarrollo'}
            ]
        )
        print(f"Tabla '{TABLA}' en creación. Esperando...")

        # Esperar a que la tabla esté disponible
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=TABLA)
        print(f"Tabla '{TABLA}' creada y disponible.")

    except dynamodb.exceptions.ResourceInUseException:
        print(f"ℹ La tabla '{TABLA}' ya existe.")
    except Exception as e:
        print(f"Error: {e}")

def describir_tabla():
    info = dynamodb.describe_table(TableName=TABLA)['Table']
    print(f"\nInformación de la tabla:")
    print(f"  Nombre    : {info['TableName']}")
    print(f"  Estado    : {info['TableStatus']}")
    print(f"  ARN       : {info['TableArn']}")
    print(f"  Elementos : {info.get('ItemCount', 0)}")

crear_tabla()
describir_tabla()