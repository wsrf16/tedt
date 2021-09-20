
def unicode2str(unicode):
    return unicode.encode('unicode_escape').decode('unicode_escape')


def bytes2str(bytes):
    return bytes.decode(encoding="utf-8")


