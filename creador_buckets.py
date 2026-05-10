# 01_crear_bucket.py
import boto3
import json

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'stf-artefactos-SEA'

def crear_bucket():
    try:
        s3.create_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket creado: {BUCKET_NAME}")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"El bucket '{BUCKET_NAME}' ya existe y te pertenece.")
    except Exception as e:
        print(f"Error: {e}")

crear_bucket()

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'stf-artefactos-<TUS_INICIALES>'

def bloquear_acceso_publico():
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    print("Acceso público bloqueado. Los artefactos financieros están protegidos.")

bloquear_acceso_publico()