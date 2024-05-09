import servicio_tecnologico_pb2 as pb

solic_usuario = pb.solic_usuario(
  id=1,
  nombre="Antonio Perez",
  numero_cliente=333,
  tipoServicio='NORMAL',
)

print(solic_usuario)