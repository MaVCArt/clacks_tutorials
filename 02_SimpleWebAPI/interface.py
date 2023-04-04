from clacks import ServerInterface
from clacks_web import get, post


class MySimpleRESTAPI(ServerInterface):

    @get('/simple_get')
    def simple_get(self, *args, **kwargs):
        print(args, kwargs)
        return f'Simple GET method that returns some kind of resource. Can take arguments: {args}, {kwargs}, but you ' \
               f'will note that all arguments are provided as keyword arguments, as HTTP requests do not allow simple ' \
               f'positional arguments.'

    @post('/simple_post')
    def simple_post(self, *args, **kwargs):
        return f'Simple POST method that takes some arguments and makes some kind of server-side alteration.' \
               f'This kind of method is usually reserved for database alterations and most commonly used in ' \
               f'web form submission.'