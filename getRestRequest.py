#!/usr/bin/python

# Example of how to make a REST call using GET (or POST) method, thanks to: 
# https://www.gngrninja.com/code/2017/6/16/python-simple-rest-api-example-and-string-formatting
# https://realpython.com/python-requests/#query-string-parameters

import requests 
  
def GetRequest(theURL, theParams):
	try:
		response = requests.get(theURL, params = theParams)
		# If the response was successful, no Exception will be raised
		response.raise_for_status()
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')  # Python 3.6
	except Exception as err:
		print(f'Other error occurred: {err}')  # Python 3.6
	else:
		#responseText = response.text
		responseJson = response.json()
		
		# On Windows the encoding is likely utf-8, which can cause problems
		# For example the "TM" unicode symbol will cause an exception
		# Verify encoding with this: 
		print(response.encoding) 
		
		# The rest of this code is specific to the Github json schema ...
		# Update accordingly depending on expected schema of the response.
		repository = responseJson['items'][2]
		print(f'Repository name: {repository["name"]}')  # Python 3.6+
		print(f'Repository description: {repository["description"]}')  # Python 3.6+
		
		
# api-endpoint 
# https://api.github.com/search/repositories?q=requests&language=python
api_url = 'https://api.github.com/search/repositories'
parameters = {'q': 'requests+language:python'}

GetRequest(api_url, parameters)