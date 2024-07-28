import threading
import requests
import time

# List of URLs to scrape
urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.djangoproject.com",
    "https://www.flask.palletsprojects.com",
    "https://www.fastapi.tiangolo.com"
]

# Function to download the content from a URL
def download_url(url):
    try:
        response = requests.get(url)
        print(f"Downloaded {len(response.content)} bytes from {url}")
        print(f"response: {response.content}") # html response
        print("=======================================================")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Main function to create and start threads
def main():
    threads = []
    
    # Create a thread for each URL
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url,))
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("All downloads completed.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
