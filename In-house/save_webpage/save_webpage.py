import os
import requests
import argparse
from requests.exceptions import HTTPError


def get_args() -> argparse.ArgumentParser:
	"""
	Create cmd-line args that would be accepted by the program

	:returns: parser - A cmd-line argument argparse object
	"""
	parser = argparse.ArgumentParser(description="Save the image of a webpage from it's url")
	# add positional argument - API_key
	parser.add_argument("api_key", help="API_KEY")
	# add positional argument - url
	parser.add_argument("url", help="Url of the webpage")
	# add optional argument nocookie
	parser.add_argument("--nocookie", type=bool, help="option to activate cookies popups and banners", default=True)
	# add optional argument noads
	parser.add_argument("--noads", type=bool, help="option to prevent ads", default=True)
	# add optioonal argument - format to specify image file type
	parser.add_argument("--format", type=str, help="format to export the image", choices=['jpeg', 'png', 'jpg'], default='jpeg')

	return parser

def get_image(api_key: str, webpage_url: str, nocookie: bool, noads: bool, img_format: str) -> bytes:
	"""
	Get image from api
	:params api_key: Private key assigned to a user on https://www.abstractapi.com
	:params webpage_url: Url of the webpage to be screenshot
	:params nocookie: option to add cookies pop-ups.
	:params noads: option whether to add ads on the page to the screenshot
	:params img_format: format to store the screenshot image jpeg or png

	:returns: img_content - Bytes content of the screen shot image
	"""
	# define the payload or the parameters to be requested alongside the url
	query= {
	"key": api_key,
	"q": webpage_url,
	"nocookie": nocookie,
	"noads": noads,
	"format": img_format
	}

	# try getting a request
	try:
		response = requests.get(url="https://api.savepage.io/v1", params=query)
		print(f"[+] Retrieved image screenshot of {webpage_url}")
	except HTTPError as http_err:
		print(f"HTTP error occured {http_err}")
	except Exception as err:
		print(f"Error occured {err}")
	img_content = response.content

	return img_content


def save_image(img_content, webpage_url, img_format) -> None:
	"""
	Save screenshot image in local storage
	:params img_content: Bytes content of the screenshot that'll be written to img file
	:params webpage_url: Url of webpage screenshot, to name the screeenshot img file
	:params img_format: Image format to add the screenshot img file as extension
	"""
	# create a new image directory to store screenshot
	os.makedirs("./image", exist_ok=True)
	print(f"[+] Creating new folder '/image' to store screenshot image")

	# strip / and \ to prevent OSError
	webpage_url = webpage_url.split('.')[-2].strip("https://")
	print(webpage_url)
	# open file for writiing binary/bytes to it
	try:
		with open(fr'./image/{webpage_url}.{img_format}', mode="wb") as f:
			f.write(img_content)
			print(f"[+] Writiing to image data to {os.getcwd}/image/{webpage_url}.{img_format}")
			print(f"Saving file....")
	except FileExistsError:
		pass

	return


def main():
	# get the args
	args = get_args().parse_args()
	# get api key from environment variable
	# api_key = os.environ.get('SAVE_PAGE_API_KEY')

	# retrieve the image content and set preferences/options
	img_content = get_image(api_key=args.api_key, webpage_url=args.url, noads=args.noads, nocookie=args.nocookie, img_format=args.format)
	# save the image
	save_image(img_content=img_content, webpage_url=args.url, img_format=args.format)
	print(f"--------------------DONE------------------")
if __name__ == '__main__':
	main()
