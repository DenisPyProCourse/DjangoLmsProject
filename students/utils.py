
def qs2html(qs):
    lst = []
    if qs is not None:
        for line in qs:
            lst.append(f'<a href="update/{line.pk}/">Edit</a>&nbsp;&nbsp;{line}')
    else:
        lst.append('QuerySet is empty')

    return lst
