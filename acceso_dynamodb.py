# 08_acceso_dynamodb.py
import boto3, json

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
TABLA = 'stf-despliegues'
LAB_ROLE_ARN = 'arn:aws:iam::<ACCOUNT_ID>:role/LabRole'  # Reemplazar

tabla_arn = dynamodb.describe_table(TableName=TABLA)['Table']['TableArn']

politica = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LecturaLabRole",
            "Effect": "Allow",
            "Principal": {"AWS": LAB_ROLE_ARN},
            "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:Scan"],
            "Resource": tabla_arn
        },
        {
            "Sid": "EscrituraLabRole",
            "Effect": "Allow",
            "Principal": {"AWS": LAB_ROLE_ARN},
            "Action": ["dynamodb:PutItem", "dynamodb:UpdateItem", "dynamodb:DeleteItem"],
            "Resource": tabla_arn
        }
    ]
}

def aplicar_politica():
    dynamodb.put_resource_policy(
        ResourceArn=tabla_arn,
        Policy=json.dumps(politica)
    )
    print("Politica aplicada. Solo LabRole puede operar la tabla de despliegues.")

def verificar_politica():
    respuesta = dynamodb.get_resource_policy(ResourceArn=tabla_arn)
    p = json.loads(respuesta['Policy'])
    print("\nPolitica activa en stf-despliegues:")
    for stmt in p['Statement']:
        print(f"  {stmt['Sid']}: {', '.join(stmt['Action'])}")

aplicar_politica()
verificar_politica()