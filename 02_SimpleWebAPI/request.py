import requests

# -- with the standard web API, the simple GET method without any path will just be rerouted to the "list_commands"
# -- method.
response = requests.get('http://localhost:9000')
print(response.json()['response'])

# -- with our custom API, we've registered one resource on the GET path, and one on the POST path.
# -- these requests use different "verbs", as they are referred to.

# -- both of these methods effectively do the same thing for this example, but this shows how to route requests
# -- through different paths.
response = requests.get('http://localhost:9000/simple_get', json={'my_arg': 'my_value'})
print(response.json()['response'])

response = requests.post('http://localhost:9000/simple_post', json={'my_arg': 'my_value'})
print(response.json()['response'])
