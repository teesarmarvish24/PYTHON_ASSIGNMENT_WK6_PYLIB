# PYTHON_ASSIGNMENT_WK6_PYLIB
This is for the ubuntu enhanced python library by plp academy 

Ubuntu_Requests Image Fetcher

"I am because we in are." - Ubuntu Philosophy

This project is a simple Python script, inspired by the Ubuntu philosophy of community and sharing. It connects to the global community of the internet to respectfully fetch and save shared image resources from a URL.


Ubuntu Principles in Action

1. Community: Connects to the wider web to fetch shared resources.

2. Respect: Handles connection errors, server errors (like 404s), and timeouts gracefully without crashing.

3. Sharing & Practicality: Organizes the fetched images into a Fetched_Images directory for later appreciation and use.


Features

1. Prompts the user for a direct image URL.

2. Automatically creates a Fetched_Images directory if one doesn't exist.

3. Downloads the image from the URL with a 10-second timeout.

4. Handles HTTP and Connection errors gracefully.

5. Extracts the original filename from the URL.

6. If no filename is found, it inspects the content-type header to create a fallback name (e.g., downloaded_image.png).


Setup and Installation

Clone the repository:
(Once you have created it on GitHub)

git clone [https://github.com/YOUR-USERNAME/Ubuntu_Requests.git](https://github.com/YOUR-USERNAME/Ubuntu_Requests.git)
cd Ubuntu_Requests

Create a virtual environment (Recommended): This isolates the project's dependencies.

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
py -m venv venv
.\venv\Scripts\activate

Install dependencies:
This script requires the requests library.

pip install requests


How to Run

Make sure your virtual environment is activated.

Run the script from your terminal:

python image_fetcher.py

When prompted, paste a direct URL to an image.
Example: https://images.unsplash.com/photo-1516214104703-d870798883c5

The script will connect, download the image, and save it to the Fetched_Images directory.

Example Output

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: [https://example.com/ubuntu-wallpaper.jpg](https://example.com/ubuntu-wallpaper.jpg)

Connecting to [https://example.com/ubuntu-wallpaper.jpg](https://example.com/ubuntu-wallpaper.jpg)...
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
