"""
Ubuntu-Inspired Image Fetcher
This script respectfully fetches an image from a provided URL
and saves it to a local directory, embodying the Ubuntu
principles of community and sharing.
"""

import requests
import os
from urllib.parse import urlparse

def main():
    """Main function to run the image fetching process."""
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get URL from user
    url = input("Please enter the image URL: ")
    
    try:
        # --- Ubuntu Principle: Sharing (Organizing) ---
        # Create a directory for our shared resources.
        # os.makedirs with exist_ok=True is a "respectful" way
        # to create a directory: it doesn't fail if it's already there
        
        output_dir = "Fetched_Images"
        os.makedirs(output_dir, exist_ok=True)
        
        # --- Ubuntu Principle: Community (Connecting) ---
        # Connect to the web community to fetch the resource.
        # We set a timeout to be respectful of our own resources.

        print(f"\nConnecting to {url}...")
        response = requests.get(url, timeout=10)
        
        # --- Ubuntu Principle: Respect (Error Handling) ---
        # Check if the connection was successful (status code 200-299).
        # This respects the server by checking its response
        # before trying to process the data.
        response.raise_for_status()
        
        # --- Practicality: File Naming ---
        # Extracting a filename from the URL.
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If the URL doesn't have a clear filename (e.g., a query),
        # create a fallback name. We'll try to get the extension.
        if not filename:
            # A simple way to try and get a file extension
            content_type = response.headers.get('content-type')
            ext = '.jpg' # default
            if content_type and 'image/jpeg' in content_type:
                ext = '.jpg'
            elif content_type and 'image/png' in content_type:
                ext = '.png'
            elif content_type and 'image/gif' in content_type:
                ext = '.gif'
            filename = f"downloaded_image{ext}"
            
        # --- Practicality: Saving the File ---
        # Create the full path to save the file
        filepath = os.path.join(output_dir, filename)
        
        # Save the image content. We use 'wb' (write binary)
        # mode because images are binary data, not plain text.
        with open(filepath, 'wb') as f:
            f.write(response.content)
            
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
        
    except requests.exceptions.HTTPError as e:
        # Handle bad responses from the server (e.g., 404 Not Found, 403 Forbidden)
        print(f"✗ HTTP Error: Could not fetch image. The server responded with: {e.response.status_code}")
    except requests.exceptions.ConnectionError:
        # Handle network-level errors (e.g., DNS failure, no internet)
        print("✗ Connection error: Could not connect to the URL. Please check your internet connection.")
    except requests.exceptions.Timeout:
        # Handle the case where the server didn't respond in time
        print("✗ Connection error: The request timed out.")
    except requests.exceptions.RequestException as e:
        # A general catch-all for other `requests` library errors
        print(f"✗ Connection error: {e}")
    except Exception as e:
        # Handle other unexpected errors (e.g., permission error saving file)
        print(f"✗ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
