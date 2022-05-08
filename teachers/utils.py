
def qs2html(qs):
    lst = []
    if qs is not None:
        for line in qs:
            lst.append(str(line))

    else:
        lst.append('Queryset is empty')

    return '<br>'.join(lst)

def gen2html(gen):
    lst = []
    if gen is not None:
        for line in gen:
            lst.append(str(line))
    else:
        lst.append('Queryset is empty')
    return '<br>'.join(lst)