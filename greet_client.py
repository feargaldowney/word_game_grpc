import greet_pb2_grpc
import greet_pb2
import time
import grpc
import FergTest

"""
NOTE:
1. Changed instances of 'hello' to 'guess'
2. Changed instances of 'name' to 'game_phrase'


TODO:
"""
def get_client_stream_requests():

    phrase = FergTest.start()
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = greet_pb2.helloRequest(greeting = "LETTER", name = "DEBUGGING ------ FergTest.start()")
        yield hello_request
        time.sleep(1)

def run():
    phrase = FergTest.start()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        rpc_call = input("Please guess a letter > ") #"Which rpc would you like to make: "

        if rpc_call.isalpha():
            hello_request = greet_pb2.HelloRequest(greeting = rpc_call, name = phrase)
            hello_reply = stub.SayHello(hello_request)
            print("Guess Response Received:")
            print(hello_reply)
        else:
            print("YOU DIED.... just kidding, try guessing a letter next time :) ")

        

        # elif rpc_call == "2":
        #     hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = "Ferg")
        #     hello_replies = stub.ParrotSaysHello(hello_request)

        #     for hello_reply in hello_replies:
        #         print("ParrotSaysHello Response Received:")
        #         print(hello_reply)
        # elif rpc_call == "3":
        #     delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

        #     print("ChattyClientSaysHello Response Received:")
        #     print(delayed_reply)
        # elif rpc_call == "4":
        #     responses = stub.InteractingHello(get_client_stream_requests())

        #     for response in responses:
        #         print("InteractingHello Response Received: ")
        #         print(response)

if __name__ == "__main__":
    run()