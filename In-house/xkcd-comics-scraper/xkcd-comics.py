'''
Program logic:
- Get user input as argument on the number of comics to generate and a path to the directory to store image file containing the comic
- Make requests to the url that'll generate these different pages and links for the image file
- Get the image file link by making a request to the image file url
- Store the binary content into a file with a name that is equal to that of the image file link on the web
'''

import requests
from bs4 import BeautifulSoup
import argparse
import sys
import os


def get_args() -> argparse.ArgumentParser:
	"""
	Parse cmd-line arguments

	:returns: parser - ArgumentParser object containing cmd-line arguments
	"""
	parser = argparse.ArgumentParser(description="Scrape xkcd-comics images into a folder")

	# positional cmd-line argument for the directory path to store comic images
	parser.add_argument("dir_path", help="Directory path to store comic images")

	# optional cmd-line argument to get the number of comic images to retrieve
	parser.add_argument("n", type=int, help="Number of comic images to retrieve", default=1)

	# add optional parameter to print logs
	parser.add_argument("-v", "--verbose", action="store_true")

	return parser


def get_image_url() -> str:
	"""
	Retrieve the comic image file url
	returns: imag_url - str object containing image url
	"""
	# request the random comic page url
	rand_img_response = requests.get(url="https://c.xkcd.com/random/comic")
	# create beautiful soup object from response object's text
	rand_img_soup = BeautifulSoup(rand_img_response.text, 'lxml')
	# retrieve the url of the png comic image file
	image_url = rand_img_soup.find("div", attrs={"id":"middleContainer"}).findAll('a')[-1]["href"]

	return image_url


def save_image(dir_path: str, img_url: str, verbose: bool) -> None:
	"""
	Save the image from the url to the specified local directory

	:param dir_path: Specify directory path to save the comics folder containing the comic images into
	:param img_url: Url of the comic image file on the internet
	:param verbose: Print log messages (True | False)

	:returns: None
	"""
	# if verbose is true print log messages
	if verbose:
		print(f"Checking file path {dir_path}")
	else: pass

	# if the path is not valid create new path else exit the program
	if not os.path.isdir(dir_path):
		print(f"The directory path {dir_path} is invalid/broken.")
		new_path_decision = input("Create a directory with this path? [y|n] ").casefold()
		# create a new directory if prompt response is y
		if new_path_decision == "y":
			# construct file path string
			dir_path = os.path.join(dir_path, "comics")
			# create the file path's directory
			os.makedirs(dir_path, exist_ok=False)
			print(f'Creating new directory at {dir_path}')
		# close the program if prompt response is n
		else:
			print(f"-"*15, "Closing Program", "-"*15)
			sys.exit()
	else: pass

	# if verbose is true print log messages
	if verbose:
		print(f"File path {dir_path} is valid")
	else: pass

	# get the file name from the file url
	img_file_name = img_url.split("/")[-1]

	# if verbose is true print log messages
	if verbose:
		print(f"[+] Retriving {img_file_name} comic")
	else: pass

	# create path string to store the comics
	comic_path = os.path.join(dir_path, "comics")
	# create a comic folder within the valid specified directory from the path string
	os.makedirs(comic_path, exist_ok=True)
	# create an absolute path for the image
	file_path = os.path.abspath(os.path.join(comic_path, img_file_name))

	# request the image
	img_response = requests.get(url=img_url)
		# if verbose is true print log messages
	if verbose:
		print(f"[+] Comic retrieved; Saving comic to {file_path}")
	else: pass
	# open and create a file and write the binary of the image requested to it
	with open(file_path, mode="wb+") as f:
		f.write(img_response.content)

		# if verbose is true print log messages
	if verbose:
		print(f"[+] Comic image saved...\n")
	else: pass


def main():

	# get the arguments
	arg_parser = get_args()
	args = arg_parser.parse_args()
	# make path string usable across multiple devices
	dir_path = os.path.join(args.dir_path)
	no_imgs = args.n
	verbose = args.verbose
	# get the images the number of times requested
	for _ in range(no_imgs):
		rand_img_url = get_image_url()
		save_image(dir_path=dir_path, img_url=rand_img_url, verbose=verbose)

	print(f"[ + ] Retrived {no_imgs} comics. Check {dir_path} for comics 😎👌🏽.")

if __name__ == '__main__':
	main()
