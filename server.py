import websockets
import asyncio

PORT = 6503

print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")
    async for message in websocket:
        print("Received message from client: " + message)
        await websocket.send("Pong: " + message)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
