#!/usr/bin/env python

import asyncio
import websockets

async def test_websocket():
    uri = "ws://localhost:5000/document_readiness"
    async with websockets.connect(uri) as websocket:
        await websocket.send("38aeafca-80e1-4496-b584-354fb5bb07c4")
        response = await websocket.recv()
        print(f"Response from server: {response}")

asyncio.run(test_websocket())

