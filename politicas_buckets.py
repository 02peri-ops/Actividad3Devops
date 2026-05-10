# 06_crear_tabla_dynamodb.py
import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
TABLA = 'stf-despliegues'

def crear_tabla():
    try:
        dynamodb.create_table(
            TableName=TABLA,
            KeySchema=[
                {'AttributeName': 'release_id', 'KeyType': 'HASH'},
                {'AttributeName': 'ambiente',   'KeyType': 'RANGE'}
            ],
            AttributeDefinitions=[
                {'AttributeName': 'release_id', 'AttributeType': 'S'},
                {'AttributeName': 'ambiente',   'AttributeType': 'S'}
            ],
            BillingMode='PAY_PER_REQUEST',
            Tags=[
                {'Key': 'Proyecto', 'Value': 'STF-DevOps'},
                {'Key': 'Entorno',  'Value': 'Produccion'},
                {'Key': 'Sector',   'Value': 'Financiero'}
            ]
        )
        print(f"Tabla '{TABLA}' en creacion. Esperando...")
        waiter = dynamodb.get_waiter('table_exists')
        waiter.wait(TableName=TABLA)
        print(f"Tabla '{TABLA}' lista.")
    except dynamodb.exceptions.ResourceInUseException:
        print(f"La tabla '{TABLA}' ya existe.")
    except Exception as e:
        print(f"Error: {e}")

def describir_tabla():
    info = dynamodb.describe_table(TableName=TABLA)['Table']
    print(f"\nTabla  : {info['TableName']}")
    print(f"Estado : {info['TableStatus']}")
    print(f"ARN    : {info['TableArn']}")

crear_tabla()
describir_tabla()