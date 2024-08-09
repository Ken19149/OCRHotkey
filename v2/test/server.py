# x/server.py

import asyncio
import websockets

# A sample data-generating function that sends data to the client every second.
async def send_data(websocket, path):
    counter = 0
    while True:
        # Create a sample message (e.g., a counter value)
        message = f"Counter value: {counter}"
        # Send the message to the connected client
        await websocket.send(message)
        # Print the message to the server console
        print(f"Sent: {message}")
        # Wait for 1 second
        await asyncio.sleep(1)
        # Increment the counter
        counter += 1

# Start the WebSocket server
start_server = websockets.serve(send_data, "localhost", 6789)

# Run the server
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
