def mark_bold(function):
    def wrapper(string):
        return '<b>' + function(string) + '</b>'
    return wrapper

def mark_italic(function):
    def wrapper(string):
        return '<i>' + function(string) + '</i>'
    return wrapper


@mark_bold
def contents(string):
    return string

@mark_italic
def contents2(string):
    return string

@mark_bold
@mark_italic
def contents3(string):
    return string

print (contents('안녕'))
print (contents2('안녕'))
print (contents3('안녕'))