# 04_cifrado.py
import boto3

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'stf-artefactos-<TUS_INICIALES>'

def configurar_cifrado():
    s3.put_bucket_encryption(
        Bucket=BUCKET_NAME,
        ServerSideEncryptionConfiguration={
            'Rules': [{
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                },
                'BucketKeyEnabled': True
            }]
        }
    )
    print("Cifrado AES-256 habilitado. Los datos financieros están protegidos en reposo.")

def verificar_cifrado():
    respuesta = s3.get_bucket_encryption(Bucket=BUCKET_NAME)
    reglas = respuesta['ServerSideEncryptionConfiguration']['Rules']
    for regla in reglas:
        alg = regla['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
        print(f"Algoritmo activo: {alg}")

def verificar_objeto_cifrado(clave_s3):
    respuesta = s3.head_object(Bucket=BUCKET_NAME, Key=clave_s3)
    cifrado = respuesta.get('ServerSideEncryption', 'Sin cifrado')
    print(f"Cifrado del artefacto '{clave_s3}': {cifrado}")

configurar_cifrado()
verificar_cifrado()
verificar_objeto_cifrado('releases/v1.1/config.json')