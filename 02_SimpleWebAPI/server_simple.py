import clacks_web

# -- as you can see, with the clacks_web library, making a simple REST API web server is dead easy.
server = clacks_web.simple_rest_api('My First Web Server', 'localhost', 9000)
server.start(blocking=True)
