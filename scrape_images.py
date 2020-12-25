import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

#checks if a url is VALID
def is_valid(url):
    parse = urlparse(url)
    return bool(parse.netloc) and bool(parse.scheme)

#returns all images found on the webpage
def get_all_images(url):
    soup = bs(requests.get(url).content, 'html.parser')
    img_urls = []
    for img in tqdm(soup.find_all('img'), 'extracting images'):
        img_url = img.attrs.get('src')
        #if image does not have src attr, skip
        if not img_url:
            continue
        #add base website domain to img src
        img_url = urljoin(url, img_url)
        #removing some xtra garbage on some img srcs
        try:
            pos = img_url.index('?')
            img_url = img_url[:pos]
        except ValueError:
            pass
        #validifing the url
        if is_valid(img_url):
            img_urls.append(img_url)
    return img_urls

#downloads the file based on url to the path provided
def download(url, path):
    #if path doesn't exist, it is created
    if not os.path.isdir(path):
        os.makedirs(path)
    #download response
    response = requests.get(url, stream=True)
    #get file size
    file_size = int(response.headers.get("Content-Length", 0))
    #get file name
    file_name = os.path.join(path, url.split('/') [-1])
    #progress bar, changing units to bytes
    progress = tqdm(response.iter_content((1024), f'downloading {file_name}'))
    with open(file_name, 'wb') as f:
        for data in progress:
            #write data read to file
            f.write(data)
            #update progress bar
            progress.update(len(data))

def main(url, path):
    #get all images
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)

if __name__ == '__main__':
    user = 'user'
    website = 'https://weather.com/'
    main(f'{website}', f'C:/Users/{user}/Desktop/IMGS')