import requests

r = requests.get('https://github.com/saviosousa2/aprendendo-python')

print (r.text)