# 03_carga_automatica.py
import boto3
import os
from pathlib import Path

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'lab-bucket-<TUS_INICIALES>'
DIRECTORIO_LOCAL = Path.home() / 'lab-s3' / 'datos'
PREFIJO_S3 = 'uploads/automaticos/'

def subir_directorio(directorio_local, prefijo_s3):
    archivos = list(Path(directorio_local).glob('*'))
    print(f"Encontrados {len(archivos)} archivos para subir...\n")

    exitosos = 0
    fallidos = 0

    for archivo in archivos:
        if archivo.is_file():
            clave_s3 = prefijo_s3 + archivo.name
            try:
                s3.upload_file(
                    str(archivo),
                    BUCKET_NAME,
                    clave_s3,
                    ExtraArgs={'ServerSideEncryption': 'AES256'}
                )
                print(f"Subido: {archivo.name} → s3://{BUCKET_NAME}/{clave_s3}")
                exitosos += 1
            except Exception as e:
                print(f"Error con {archivo.name}: {e}")
                fallidos += 1

    print(f"\nResumen: {exitosos} exitosos, {fallidos} fallidos.")

subir_directorio(DIRECTORIO_LOCAL, PREFIJO_S3)