import os
from mcp.server.fastmcp import FastMCP

# Qonto API configuration
thirdparty_host = None
api_key = None
organization_id = None
staging_token = None
headers = {}

# Single MCP instance
mcp = FastMCP("Qonto MCP")

def setup_qonto_config():
    """Initialize Qonto API configuration with environment variables"""
    global thirdparty_host, api_key, organization_id, staging_token, headers
    
    thirdparty_host = os.getenv("QONTO_THIRDPARTY_HOST")
    if not thirdparty_host:
        raise ValueError("QONTO_THIRDPARTY_HOST environment variable is not set.")

    api_key = os.getenv("QONTO_API_KEY")
    if not api_key:
        raise ValueError("QONTO_API_KEY environment variable is not set.")

    organization_id = os.getenv("QONTO_ORGANIZATION_ID")
    if not organization_id:
        raise ValueError("QONTO_ORGANIZATION_ID environment variable is not set.")

    staging_token = os.getenv("QONTO_STAGING_TOKEN")

    headers = {
        "Accept": "application/json",
        "Authorization": f"{api_key}",
    }

    if staging_token:
        headers["X-Qonto-Staging-Token"] = staging_token
