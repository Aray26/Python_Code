def func1(x, y, z):
    print x
    print y 
    print z                 

def func2(*args):
    # Convert args tuple to a list so we can modify it
    print str(type(args))
    args = list(args)
    args[0] = 'Hello'
    args[1] = 'awesome'
    func1(*args)
    
def echo_args(*args):
    for arg in args:
        print arg

func2('Goodbye', 'cruel', 'world!')

echo_args('1', '2', 'go!')


def display_stuff_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print key, '==>', value
            
display_stuff_kwargs(police= 'jetbird', movie= 'killing')