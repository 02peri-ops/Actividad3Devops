# 07_crud_dynamodb.py
import boto3
from decimal import Decimal
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('stf-despliegues')

def insertar_despliegues():
    despliegues = [
        {
            'release_id': 'v1.1-20240101',
            'ambiente': 'produccion',
            'aplicacion': 'stf-app-financiera',
            'estado': 'EN_PROGRESO',
            'iniciado_por': 'LabRole',
            'timestamp': datetime.utcnow().isoformat(),
            'duracion_seg': Decimal('0')
        },
        {
            'release_id': 'v1.0-20231201',
            'ambiente': 'produccion',
            'aplicacion': 'stf-app-financiera',
            'estado': 'EXITOSO',
            'iniciado_por': 'LabRole',
            'timestamp': '2023-12-01T10:00:00',
            'duracion_seg': Decimal('142')
        },
        {
            'release_id': 'v1.1-20240101',
            'ambiente': 'staging',
            'aplicacion': 'stf-app-financiera',
            'estado': 'EXITOSO',
            'iniciado_por': 'LabRole',
            'timestamp': '2024-01-01T08:00:00',
            'duracion_seg': Decimal('98')
        }
    ]

    for d in despliegues:
        tabla.put_item(Item=d)
        print(f"  Registrado: {d['release_id']} | {d['ambiente']} | {d['estado']}")

    print(f"\n{len(despliegues)} despliegues registrados.")

insertar_despliegues()

def leer_despliegue(release_id, ambiente):
    respuesta = tabla.get_item(
        Key={'release_id': release_id, 'ambiente': ambiente}
    )
    item = respuesta.get('Item')
    if item:
        print("\nDespliegue encontrado:")
        for k, v in item.items():
            print(f"  {k}: {v}")
    else:
        print("Despliegue no encontrado.")
    return item

def listar_despliegues():
    respuesta = tabla.scan()
    items = respuesta.get('Items', [])
    print(f"\nHistorial de despliegues ({len(items)} registros):")
    for item in items:
        print(f"  [{item['release_id']}] {item['ambiente']} -> {item['estado']}")

leer_despliegue('v1.1-20240101', 'produccion')
listar_despliegues()

def actualizar_estado_despliegue(release_id, ambiente, nuevo_estado, duracion):
    respuesta = tabla.update_item(
        Key={'release_id': release_id, 'ambiente': ambiente},
        UpdateExpression='SET estado = :e, duracion_seg = :d',
        ExpressionAttributeValues={
            ':e': nuevo_estado,
            ':d': Decimal(str(duracion))
        },
        ReturnValues='UPDATED_NEW'
    )
    cambios = respuesta.get('Attributes', {})
    print("Despliegue actualizado:")
    for k, v in cambios.items():
        print(f"  {k}: {v}")

actualizar_estado_despliegue('v1.1-20240101', 'produccion', 'EXITOSO', 178)

def eliminar_despliegue(release_id, ambiente):
    item = leer_despliegue(release_id, ambiente)
    if not item:
        return
    tabla.delete_item(
        Key={'release_id': release_id, 'ambiente': ambiente}
    )
    print(f"Registro '{release_id}/{ambiente}' eliminado.")

eliminar_despliegue('v1.1-20240101', 'staging')
listar_despliegues()