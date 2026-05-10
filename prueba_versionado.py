# 02b_prueba_versionado.py
import boto3

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'stf-artefactos-<TUS_INICIALES>'
ARCHIVO = 'app/release-notes.txt'

# Simular release v1.0
s3.put_object(Bucket=BUCKET_NAME, Key=ARCHIVO, Body=b'Release v1.0 - Funcionalidad base')
print("Release v1.0 registrado.")

# Simular release v1.1
s3.put_object(Bucket=BUCKET_NAME, Key=ARCHIVO, Body=b'Release v1.1 - Correccion de errores financieros')
print("Release v1.1 registrado.")

# Listar versiones disponibles
respuesta = s3.list_object_versions(Bucket=BUCKET_NAME, Prefix=ARCHIVO)
versiones = respuesta.get('Versions', [])
print(f"\nHistorial de versiones para '{ARCHIVO}':")
for v in versiones:
    print(f"  VersionId: {v['VersionId']} | {v['LastModified'].strftime('%Y-%m-%d %H:%M:%S')}")