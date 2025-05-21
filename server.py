from mcp.server.fastmcp import FastMCP
from app import getColor

# Initialize MCP server
mcp = FastMCP("color.mcp")

@mcp.tool()
async def  get_color(color: str) -> str:
    """
    Get the color name from the color code.
    """
    return getColor(color)



if __name__ == "__main__":
    mcp.run(transport="stdio")