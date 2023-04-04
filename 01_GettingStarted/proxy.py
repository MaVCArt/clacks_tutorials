import clacks

# -- first we create a handler / marshaller pair.
# -- as we know the server used the "simple" handler / marshaller combination on this port, we recreate its exact
# -- copy here. Otherwise, the handler will not be able to talk to the server.
handler = clacks.SimpleRequestHandler(clacks.SimplePackageMarshaller())

# -- now we can create a proxy for the "simple" server port.
proxy = clacks.ClientProxyBase(('localhost', 9998), handler=handler, connect=True)

print(proxy.list_commands().response)

# -- now we can call our custom method.
print(proxy.hello_world().response)
