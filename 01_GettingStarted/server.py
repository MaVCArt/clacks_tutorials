import clacks

# -- import our custom interface
from interface import MyCustomInterface

# -- create a simple server instance.
# -- All keyword arguments can be left to their default in most cases.
server = clacks.ServerBase(identifier='My First Clacks Server')

# -- create a handler. Handlers are how the Server receives input requests.
handler = clacks.JSONHandler(clacks.JSONMarshaller(), server=server)

# -- once a handler has been created, it needs to be registered on a host/port combo.
server.register_handler_by_key(host='localhost', port=9998, handler_key='simple', marshaller_key='simple')

# -- give the server something to do - the "standard" interface contains some basic methods.
server.register_interface_by_key('standard')

# -- now register our custom interface
# -- note how we have to register the INSTANCE, not the class.
server.register_interface('custom', MyCustomInterface())

# -- start the server. By setting "blocking" to True, we block this interpreter instance from progressing.
# -- Setting "blocking" to False instead would not stop this interpreter instance from continuing, so the server
# -- would die if the interpreter instance reaches its exit point.
server.start(blocking=True)
