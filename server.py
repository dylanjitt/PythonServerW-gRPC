from concurrent.futures import ThreadPoolExecutor
from grpc_reflection.v1alpha import reflection
import grpc
# Adicionar bibliotecas necesarias
# investigar uuid
import logging
import uuid
import log
import servicio_tecnologico_pb2 as pb
import servicio_tecnologico_pb2_grpc as rpc


def obtener_numero_servicio():
    id_servicio = uuid.uuid4().int & (1<32)-1
    return id_servicio

def costo_total(typeServicio):
    costo_base=10
    costo_final=0
    if typeServicio=="NORMAL":
        costo_final=costo_base
    elif typeServicio=="EXPRESS":
        costo_final=(costo_base*0.25)+costo_base
    elif typeServicio=="NEXT_DAY":
        costo_final=(costo_base*0.75)+costo_base
    return costo_final
    

# CompletaR con el nombre del servicio grpc
class Nombre_servicio(rpc.respuesta_solicServicer):
    # reemplazar el nombre del metodo (A1234) con el nombre del metodo en el archivo.proto
    def calcularCosto(self, request, context):
        #generar un nuevo id para el servicio
        ride_id = obtener_numero_servicio()
        # Generar la respuesta:
        # la respuesta deberia tener la siguiente sintaxis:
        costo_final=costo_total(request.tipoServicio)
        #print(costo_final)
        # pb.StartResponse(arg1 = ... , arg2 = ..)
        # arg1, arg2 definidos en el archivo .proto
        respuesta = pb.detalles_solic(
            id_servicio=ride_id,
            costo_total=costo_final
        )
        return  respuesta 
    
if __name__ == '__main__':
    import config
    # crear una nueva instancia de un servidor gRPC
    # utilizar un ThreadPoolExecutor para manejar las solicitudes entrantes
    server = grpc.server(ThreadPoolExecutor())
    # registrar un servicio gRPC en un servidor gRPC
    # sintaxis: 
    # rpc. NOMBRE_ADD_SERVICER_TO_SERVER(NOMBRE_SERVICIO(), server)
    rpc.add_respuesta_solicServicer_to_server(Nombre_servicio(),server)
    # Adicionar el nombre del servicio definido en en archivo.prot
    names = (
        pb.DESCRIPTOR.services_by_name['respuesta_solic'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    log.info('El servidor esta listo en %s', addr)
    server.wait_for_termination()