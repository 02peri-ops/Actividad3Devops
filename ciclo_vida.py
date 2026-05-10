# 05_ciclo_vida.py
import boto3

s3 = boto3.client('s3', region_name='us-east-1')
BUCKET_NAME = 'stf-artefactos-<TUS_INICIALES>'

configuracion = {
    'Rules': [
        {
            'ID': 'LimpiezaReleases',
            'Status': 'Enabled',
            'Filter': {'Prefix': 'releases/'},
            'Expiration': {'Days': 30},
            'NoncurrentVersionExpiration': {
                'NoncurrentDays': 7
            }
        },
        {
            'ID': 'LimpiezaLogs',
            'Status': 'Enabled',
            'Filter': {'Prefix': 'logs/'},
            'Expiration': {'Days': 90}
        },
        {
            'ID': 'AbortoMultipart',
            'Status': 'Enabled',
            'Filter': {'Prefix': ''},
            'AbortIncompleteMultipartUpload': {
                'DaysAfterInitiation': 3
            }
        }
    ]
}

def aplicar_ciclo_vida():
    s3.put_bucket_lifecycle_configuration(
        Bucket=BUCKET_NAME,
        LifecycleConfiguration=configuracion
    )
    print("Politicas de ciclo de vida aplicadas.")

def verificar_ciclo_vida():
    respuesta = s3.get_bucket_lifecycle_configuration(Bucket=BUCKET_NAME)
    print("\nReglas activas:")
    for regla in respuesta['Rules']:
        print(f"  {regla['ID']} | Estado: {regla['Status']}")
        if 'Expiration' in regla:
            print(f"  Expiracion: {regla['Expiration'].get('Days')} dias")

aplicar_ciclo_vida()
verificar_ciclo_vida()