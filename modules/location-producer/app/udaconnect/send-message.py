import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload...")


channel = grpc.insecure_channel("localhost:63469")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=10.842642,
    longitude=106.7503897
)

response = stub.Create(location)