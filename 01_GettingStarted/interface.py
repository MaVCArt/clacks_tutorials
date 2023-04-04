from clacks import ServerInterface


class MyCustomInterface(ServerInterface):

    def hello_world(self) -> str:
        return 'Hello World'
