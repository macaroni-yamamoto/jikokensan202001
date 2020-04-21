# coding : utf-8
class Test(object):
    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return 'Hello, world(class ver)'

application = Test()
