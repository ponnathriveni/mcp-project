from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ResearchAgent")

@mcp.tool()
def web_search(query: str) -> str:
    return f"Web search results for: {query}"

@mcp.tool()
def pdf_search(query: str) -> str:
    return f"PDF search results for: {query}"

@mcp.tool()
def summarize(text: str) -> str:
    return f"Summary:\n{text[:200]}"

if __name__ == "__main__":
    mcp.run()