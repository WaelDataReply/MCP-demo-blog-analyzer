# MCP Quick Start Demo: Client-Server Approach with Amazon Bedrock

## Overview

This repository demonstrates a client-server approach using the Model Context Protocol (MCP) of Anthropic and Amazon Bedrock. The demo showcases how to build a server with web-related tools and a client that leverages these tools in conjunction with Amazon Bedrock to generate enriched AI responses.

The demo implements a server with two key tools:
- `visit_webpages`: Fetches and processes content from web pages
- `validate_links`: Checks the validity of URLs provided

The client script communicates with the server to use these tools and leverages Amazon Bedrock's AI capabilities to generate comprehensive answers.

## Prerequisites

- Python 3.8+
- AWS account with Amazon Bedrock access
- Properly configured AWS credentials

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
Install the UV package manager:
```bash
pip install uv
```
Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```
## Running the Demo
Run both the client and server scripts simultaneously using UV:
```bash
uv run --verbose client.py server.py
```
This command will:

Start the server with the web-related tools
Launch the client that connects to both the server and Amazon Bedrock
Process requests using the tools and generate responses
## Project Structure 
server.py: Implements the server with the visit_webpages and validate_links tools  
client.py: Connects to the server, utilizes the tools, and communicates with Amazon Bedrock  

## Configuration
Ensure your AWS credentials are properly configured to allow access to Amazon Bedrock. You can configure your credentials using:

aws configure
## Notes
This is a demo implementation intended for quick-start purposes
For production use, implement appropriate security measures and error handling
License