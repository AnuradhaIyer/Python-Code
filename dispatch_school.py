from pprint import pp
import logging
import time
import json
 
logging.basicConfig(
    level = logging.INFO,
    format = '%(levelname)-8s %(asctime)s %(message)s',
    filename = 'server.log',
)
 
_dispatch_get = {}
_dispatch_post = {}
 
class Response:
    content_type = 'text/html'
    code = 200
    content = ''
    def __str__(self):
        rows = [
            f'HTTP/1.1 {self.code}',
            f'Date: {time.ctime()}',
            f'Server: IntermediatePython Server',
            f'Content-Type: {self.content_type}',
            f'Content-Length: {len(self.content)}',
            f'Connection: close',
            '',
        ]
        if self.content:
            rows.append(self.content)
        return '\n'.join(rows)
     
class get:
 
    def __init__(self, short_name):
        self.short_name = short_name
 
    def __call__(self, func):
        _dispatch_get[self.short_name] = func
        return func
 
class post:
 
    def __init__(self, short_name):
        self.short_name = short_name
 
    def __call__(self, func):
        _dispatch_post[self.short_name] = func
        return func
 
def run():
    global response
 
    while True:
        command = input('\nPath: ')
        response = Response()
        if command in _dispatch_get:
            action = _dispatch_get[command]
            try:
                rv = action()
            except Exception:
                logging.exception('Failed command: %r', command)
                response.code = 500
            else:
                logging.info('Successful command: %r', command)
                if isinstance(rv, dict):
                    response.content_type = 'application/json'
                    rv = json.dumps(rv)
                response.content = rv
        else:
            response.code = 404
        print(response)
 
######################################################
 
import time
 
@get('/')
def welcome():
    return '<h1> Hello </h1>'
 
@get('/now')
def what_time_is_it():
    return dict(clock=time.ctime(), float_time=time.time())
 
@get('/leave')
def farewell():
    return "<p> C'ya!"
 
@post('/leave')
def farewell():
    return "<p> So long and thanks for all the fish"
 
@get('/straight')
def plain_truth():
    response.content_type = 'text/plain'
    return 'The answer\nmy friend\nis blowing in the wind\n'
 
@get('/ouch')
def broken():
    return 32 / 0
 
run()
