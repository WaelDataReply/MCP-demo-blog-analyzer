from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

import re
import requests
from markdownify import markdownify
from requests.exceptions import RequestException

# Initialize FastMCP server
mcp = FastMCP("analyzer")

@mcp.tool()
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    proxies = {
        "http://": "http://localhost:3128",
        "https://": "http://localhost:3128"
    }
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=30, proxies=proxies, verify=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

@mcp.tool()
def validate_links(urls: list[str]) -> list[str, bool]:
    """Validates that the links are valid webpages.

    Args:
        urls: The URLs of the webpages to visit.

    Returns:
        A list of the url and boolean of whether or not the link is valid.
    """
    proxies = {
        "http://": "http://localhost:3128",
        "https://": "http://localhost:3128"
    }
    output = []
    for url in urls:
        try:
            # Send a GET request to the URL
            response = requests.get(url, timeout=30, proxies=proxies, verify=False)
            response.raise_for_status()  # Raise an exception for bad status codes
            print('validateResponse',response)
            # Check if the response content is not empty
            if response.text.strip():
                output.append([url, True])
            else:
                output.append([url, False])
        except RequestException as e:
            output.append([url, False])
            print(f"Error fetching the webpage: {str(e)}")
        except Exception as e:
            output.append([url, False])
            print(f"An unexpected error occurred: {str(e)}")
    return output


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')