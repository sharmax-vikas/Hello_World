#!/usr/bin/env python3
"""
Simplest MCP Server using FastMCP 2.0
Requirements: pip install fastmcp
"""

from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Hello World Server")

@mcp.tool
def say_hello(name: str = "World") -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

@mcp.resource("greeting://hello")
def get_greeting() -> str:
    """A simple greeting resource"""
    return "Hello from MCP Server!"

if __name__ == "__main__":
    # mcp.run() # stdio
    # mcp.run(transport="sse", host="127.0.0.1", port=8000) # sse
    mcp.run(transport="http", host="127.0.0.1", port=8000) # http