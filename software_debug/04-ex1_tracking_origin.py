__author__ = 'cloudlite'

#
# Modify `remove_html_markup` so that it actually works!
#

def remove_html_markup(s):
    tag = False
    double_quoted = False
    single_quoted = False
    out = ""

    for c in s:
        # print c, tag, quote
        quoted = double_quoted and single_quoted
        if c == '<' and not quoted:
            tag = True
        elif c == '>' and not quoted:
            tag = False
        elif c == "'" and tag:
            single_quoted = not single_quoted
        elif c == '"' and tag:
            double_quoted = not double_quoted
        elif not tag:
            out = out + c

    return out


def test():
    assert remove_html_markup('<a href="don' + "'" + 't!">Link</a>') == "Link"


test()