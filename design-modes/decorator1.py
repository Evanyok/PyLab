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

def decorator(fn):
    def handler(*args, **kvargs):
        print(args)
        print(kvargs)
        print('de')
        fn()
    return handler

@decorator
def foo():
    print('foo')

foo()


