import requests
import os
from requests.exceptions import HTTPError
import sys
# program specs
# get the name of the word
# ask whether to download audio of the word
# save the audio of the word to the same folder as the script.
def get_word() -> str:
	'''
	Get word input from user

	:returns: None
	'''
	input_word = input("Input word to find meaning: ")
	try:
		input_word = str(input_word)
	except TypeError:
		raise TypeError("Input is a string")
	except Exception as err:
		raise err
	else:
		return input_word


def get_json(url: str) -> list:
	"""
	Generate json from the API's response object

	:params url: Url of the API's exposed endpoint
	:returns: response.json() - A json tree
	"""
	try:
		response = requests.get(url=url)
	except HTTPError as http_err:
		print(f'HTTP Error occured: {http_err}')
	except Exception as err:
		print(f"Other error occured: {err}")
	else:
		# fetch json from the response object
		return response.json()


def save_audio(audio_url: str, word: str) -> None:
	"""
	Save audio content from url to .mp3 file in the audio folder of the current directory

	:params: audio_url - Url to audio file on the web
	:params: word - Word that is pronounced in the audio
	:returns: None
	"""
	# get the audio contents in bytes
	audio_content = requests.get(url=audio_url).content
	# create a new audio directory to save audio files
	os.makedirs('./audio', exist_ok=True)
	print(f'Creating audio folder in the current directory')
	# incase there's a FileExistsError, pass
	try:
		# open file for writing binary/bytes to it
		with open(rf"./audio/{word}.mp3", mode='wb') as f:
			print(f'Writing/Saving audio file to "{os.getcwd()}/audio/{word}"')
			f.write(audio_content)
	except FileExistsError:
		pass
	return


def get_audio_url(json_content: list) -> str:
	"""
	Generate an http compliant audio url
	:params: json_content:
	:returns: audio_url - https version of the audion url
	"""
	audio_url = json_content[0]['phonetics'][0]['audio']
	audio_url = f"https:{audio_url}"
	return audio_url


def traverse_json(json_content: list) -> None:
	"""
	Traverse through the json tree to fetch relevant data
	:params json_content: A pythonic json object (list containing other python object)
	:returns: None
	"""
	# a loop is created anywhere there is a list object
	for depth in range(len(json_content)):
		word = json_content[depth]['word']
		phonetic = json_content[depth].get("phonetic", None)
		origin = json_content[depth].get('origin', None)

		for i in range(len(json_content[depth]["meanings"])):
			part_of_speech = json_content[depth]["meanings"][i]['partOfSpeech']

			for j in range(len(json_content[depth]["meanings"][i]["definitions"])):
				definition = json_content[depth]["meanings"][i]['definitions'][j]['definition']
				example = json_content[depth]["meanings"][i]['definitions'][j].get('example', None)
				synonyms = json_content[depth]["meanings"][i]['definitions'][j]['synonyms']
				antonyms = json_content[depth]["meanings"][i]['definitions'][j]['antonyms']

				print(f"""
					Meaning of {word} as a {part_of_speech}: {definition}
					Example: {example}
					Phonetic: {phonetic}
					origin: {origin}
					synonyms: {synonyms}
					antonyms: {antonyms}
					""")

	return


def main():
	# get input
	word = get_word()
	if len(word) < 2:
		print('Length of word must be greater than 2. Try again!')
		word = get_word()
		if len(word) < 2:
			print('Quitting program')
			sys.exit()
	else: pass
	# construct url
	url =f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
	# generate json from response object
	json_content = get_json(url=url)
	# traverse the json structure
	audio_url = get_audio_url(json_content)
	# prompt if user would like to save audio
	audio_prompt = input('Save audio pronounciation?(y|n) ')
	if audio_prompt.lower() == 'y':
		save_audio(audio_url=audio_url, word=word)
	else:
		print(f'Audio pronounciation not saved')

	traverse_json(json_content=json_content)

if __name__ == "__main__":
	main()
