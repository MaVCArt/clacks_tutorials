import requests

# -- with the standard web API, the simple GET method without any path will just be rerouted to the "list_commands"
# -- method.
response = requests.get('http://localhost:9000')
print(response.json()['response'])
