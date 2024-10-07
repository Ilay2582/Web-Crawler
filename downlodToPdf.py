import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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


def download_files(url, folder_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract filename from URL
            filename = url.split("/")[-1]
            # Combine folder path and filename
            file_path = os.path.join(folder_path, filename)

            # Write the content to a file
            with open(file_path, 'wb') as file:
                file.write(response.content)

            print("Downloaded file:", filename)
        else:
            print("Failed to download file. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))


def create_pdf(files, folder_path, pdf_path):
    pdf = FPDF()
    for file in files:
        # Check if the file is a PDF or image
        if file.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
            # Add page to the PDF
            pdf.add_page()
            # Get file path
            file_path = os.path.join(folder_path, file)
            # Add image or PDF to the PDF document
            if file.endswith('.pdf'):
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt=file, ln=True, align='C')
                pdf.set_font("Arial", size=8)
                with open(file_path, 'rb') as f:
                    pdf.set_y(pdf.get_y() + 5)
                    pdf.multi_cell(0, 5, f.read().decode('utf-8'))
            else:
                pdf.image(file_path, x=10, y=None, w=190, h=250)
    # Save the PDF document
    pdf.output(pdf_path)


# Example usage
url = "https://lightinthebox.com/"  # Replace this with the URL of the website you want to scrape
all_links = get_all_links(url)
if all_links:
    print("All links on the page:")
    for link in all_links:
        print(link)
    # Specify folder path to save files
    folder_path = "downloads"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Download interesting files or images
    for link in all_links:
        download_files(link, folder_path)
    # Specify path to save the PDF
    pdf_path = "output.pdf"
    # Create PDF if interesting files or pictures were found
    create_pdf(os.listdir(folder_path), folder_path, pdf_path)
    print("PDF created successfully.")
else:
    print("No links found on the page.")
