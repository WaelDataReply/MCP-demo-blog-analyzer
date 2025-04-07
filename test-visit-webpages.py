import requests
from markdownify import markdownify
import re

def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string."""
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

    except requests.exceptions.RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Test the function
if __name__ == "__main__":
    test_url = "https://medium.com/@wael-saideni/understanding-the-difference-between-context-caching-and-semantic-caching-a-step-toward-optimizing-1a2b44d25c12"  # Replace with the URL you want to test
    result = visit_webpage(test_url)
    print(result)