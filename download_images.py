import requests
from bs4 import BeautifulSoup
import os

def download_images(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                img_name = os.path.basename(img_url)
                img_path = os.path.join(folder_path, img_name)
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    with open(img_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f"Downloaded: {img_name}")
                else:
                    print(f"Failed to download: {img_name}")
    else:
        print("Failed to fetch the page.")

def download_pdfs(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        pdf_links = soup.find_all('a', href=True)
        for link in pdf_links:
            href = link.get('href')
            if href.endswith('.pdf'):
                pdf_url = href
                pdf_name = os.path.basename(pdf_url)
                pdf_path = os.path.join(folder_path, pdf_name)
                pdf_response = requests.get(pdf_url)
                if pdf_response.status_code == 200:
                    with open(pdf_path, 'wb') as f:
                        f.write(pdf_response.content)
                    print(f"Downloaded: {pdf_name}")
                else:
                    print(f"Failed to download: {pdf_name}")
    else:
        print("Failed to fetch the page.")


website_url = "https://www.ecomschool.co.il"
#website_url = "https://www.ecomschool.co.il/course/cyber-2/"

# Example usage to download an image:
output_folder = "images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
#download_images(website_url, output_folder)

# Example usage to download pdf :
output_folder = "pdfs"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
download_pdfs(website_url, output_folder)


