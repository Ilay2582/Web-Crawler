import requests
from bs4 import BeautifulSoup
def get_all_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find all <a> tags which contain links
            links = soup.find_all('a')

            # Extract the href attribute from each <a> tag
            all_links = [link.get('href') for link in links]

            return all_links
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
            return []
    except Exception as e:
        print("An error occurred:", str(e))
        return []


# Example usage
url = "https://example.com"  # Replace this with the URL of the website you want to scrape
all_links = get_all_links(url)
if all_links:
    print("All links on the page:")
    for link in all_links:
        print(link)
else:
    print("No links found on the page.")