import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload to test")


channel = grpc.insecure_channel("localhost:63469")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=12.98965,
    longitude=107.12263
)

response = stub.Create(location)