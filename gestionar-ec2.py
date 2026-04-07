import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
def listar_instancias():  #Consulta y muestra el ID y el estado de todas las instancias EC2 en la región especificada.
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print(f"ID: {instance['InstanceId']}, Estado: {instance['State']['Name']}")

def gestionar_instancia(instance_id, accion):  #Inicia o detiene una instancia EC2 según la acción especificada.
    if accion == 'iniciar': 
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instancia {instance_id} iniciada.")
    elif accion == 'detener':
        ec2.stop_instances(InstanceIds= [instance_id])
        print(f"Instancia {instance_id} detenida.")
    
if __name__ == "__main__":
    listar_instancias()
    gestionar_instancia("ID_DE_LA_INSTANCIA", "iniciar")  # Reemplaza con el ID de tu instancia y la acción deseada (iniciar/detener    )
