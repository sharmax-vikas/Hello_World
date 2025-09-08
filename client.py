#!/usr/bin/env python3
# """
# Simple MCP Client using FastMCP 2.0
# Requirements: pip install fastmcp
# """

# import asyncio
# from fastmcp import Client

# async def test_server():
#     """Test the MCP server"""
#     print("🚀 Testing MCP Server...")
#     print("-" * 30)
    
#     try:
#         # Connect to the server script
#         # async with Client("server.py") as client:
#         async with Client("http://127.0.0.1:8000") as client:
#             print("✅ Connected to server!")
            
#             # Test the tool with parameter
#             print("\n🔧 Testing say_hello tool with name:")
#             result = await client.call_tool("say_hello", {"name": "FastMCP"})
#             print(f"Result: {result.content[0].text}")
            
#             # Test the tool without parameter (should use default)
#             print("\n🔧 Testing say_hello tool without name:")
#             result = await client.call_tool("say_hello", {})
#             print(f"Result: {result.content[0].text}")
            
#             # Test the resource
#             print("\n📚 Testing greeting resource:")
#             resource = await client.read_resource("greeting://hello")
#             print(f"Resource: {resource[0].text}")
            
#             print("\n✅ All tests passed!")
            
#     except Exception as e:
#         print(f"❌ Error: {e}")
#         print("\nTroubleshooting:")
#         print("1. Make sure FastMCP is installed: pip install fastmcp")
#         print("2. Ensure mcp_server.py is in the same directory")
#         print("3. Check that Python 3.10+ is being used")

# if __name__ == "__main__":
#     asyncio.run(test_server())

#!/usr/bin/env python3
"""
Simple MCP Client using FastMCP 2.0
Requirements: pip install fastmcp
"""

import asyncio
from fastmcp import Client

async def test_server():
    """Test the MCP server via SSE"""
    print("🚀 Testing MCP Server via SSE...")
    print("-" * 30)
    
    try:
        # Connect to the SSE server
        # async with Client("server.py") as client: # HTTPs
        # async with Client("http://127.0.0.1:8000/sse") as client: # SSE
        async with Client("http://127.0.0.1:8000/mcp") as client: # HTTPs
        
            print("✅ Connected to SSE server!")

            # List of tools
            tools = await client.list_tools()
            for tool in tools:
                print(f"  • {tool.name}: {tool.description}")
            
            # Test the tool with parameter
            print("\n🔧 Testing say_hello tool with name:")
            result = await client.call_tool("say_hello", {"name": "FastMCP"})
            print(f"Result: {result.content[0].text}")
            
            # Test the tool without parameter (should use default)
            print("\n🔧 Testing say_hello tool without name:")
            result = await client.call_tool("say_hello", {})
            print(f"Result: {result.content[0].text}")
            
            # Test the resource
            print("\n📚 Testing greeting resource:")
            resource = await client.read_resource("greeting://hello")
            print(f"Resource: {resource[0].text}")
            
            print("\n✅ All tests passed!")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure the server is running: python mcp_server.py")
        print("2. Check the server is listening on http://127.0.0.1:8000")
        print("3. Ensure no firewall is blocking port 8000")

if __name__ == "__main__":
    asyncio.run(test_server())