# image-downloader
Scrapes images from a URL with BeautifulSoup and downloads them

Followed this tutorial to get the final program working: https://www.thepythoncode.com/article/download-web-page-images-python

I had a few semi-working programs that were trying to download images found on a given URL, but it was only working on certain websites and often got overloaded. The tutorial here used BeautifulSoup to get the HTML for the base URL and parse it into a readable json. The next step involved finding all of the "img" tags in the code and separating the src extention I wanted. Adding that to the original website's URL created the URL for the image. It was then written to a specific directory, I made it create an images folder on the desktop for easy access. 
