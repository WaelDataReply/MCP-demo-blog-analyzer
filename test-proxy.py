import requests

proxies = {
    "http": "http://localhost:3128",
    "http": "http://localhost:3128"
}

try:
    response = requests.get("https://medium.com/@wael-saideni/understanding-the-difference-between-context-caching-and-semantic-caching-a-step-toward-optimizing-1a2b44d25c12", proxies=proxies, timeout=30)
    print(response.status_code)
    #print(response.json())
    print("Response Text:", response.text)  # Print raw response content
    print("Response Headers:", response.headers)  # Print response headers
except Exception as e:
    print(f"Error: {e}")