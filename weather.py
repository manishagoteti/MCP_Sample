from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location:str)->str:
    """Get the weather of the location."""
    return "It is always raining in California"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")