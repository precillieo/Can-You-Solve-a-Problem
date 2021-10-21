# xkcd-comics-scraper

Retrieve comic images from xkcd [website](https://xkcd.com/#)  

### Usage:
- Retrieve just one comic image into the directory /usr/folder  

	```bash
	$ python xkcd-comics.py /usr/folder  
	```
- Retrieve "n" number of comic images into the directory /usr/folder  
> "n" must be an integer  

	```bash
	$ python xkcd-comics.py /usr/folder n
	```
- Retrieve one comic image printing out logs (verbosity)

	```bash
	$ python xkcd-comics.py /usr/folder -v
	```

> Note: Always use Unix/Linux file paths.
> Example: */usr/folder* not C:\usr\folder
> If Windows file paths is to be used escape the "\" character
> Example: *C:\\\\usr\\\\folder*

Contributor: [0th](https://github.com/0-th) ✌🏽
