def wrapper(tag):
    def handler(fn):
        def inner(*args, **kvargs):
            print('wrapper: %s' % tag)
            setattr(args[0], 'tag', tag)
            fn(args[0], args[1])
        return inner
    return handler
    
class ts:    
    tag = 'tag'
    @wrapper('p')    
    def foo1(self, arg):
        if hasattr(self, 'tag'):
            print('%s - %s' % (getattr(self, 'tag'), arg))

f = ts()
f.foo1('h')

class wrap(object):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, fn):
        def wrapped(*args, **kvargs):
            setattr(args[0], 'tag', self.tag)
            fn(*args, **kvargs)
        return wrapped

class tso:
    @wrap(tag= 'hi')
    def foo(self):
        if hasattr(self, 'tag'):
            print('%s' % getattr(self, 'tag'))
        
ff = tso()
ff.foo()