# 02_versionado.py
import boto3

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'stf-artefactos-<TUS_INICIALES>'

def habilitar_versionado():
    s3.put_bucket_versioning(
        Bucket=BUCKET_NAME,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print("Versionado habilitado.")

def verificar_versionado():
    respuesta = s3.get_bucket_versioning(Bucket=BUCKET_NAME)
    estado = respuesta.get('Status', 'No configurado')
    print(f"Estado del versionado: {estado}")

habilitar_versionado()
verificar_versionado()
