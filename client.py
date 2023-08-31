
import websockets
import asyncio

# This function will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:6503"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send intended message
        await ws.send("Ping me back.")
        # creates a forever loop 
        while True:
            msg = await ws.recv()
            print(msg)

# Starts the connection
asyncio.get_event_loop().run_until_complete(listen())
