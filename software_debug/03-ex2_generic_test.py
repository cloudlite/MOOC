__author__ = 'cloudlite'

import re


def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    assert out.find('<') == -1
    return out


test_count = 0


def test(s):
    global test_count
    test_count += 1
    print test_count, repr(s), len(s)
    try:
        result = remove_html_markup(s)
        print 'PASS'
        return 'PASS'
    except AssertionError:
        print 'FAIL'
        return 'FAIL'


def delta_debug(s):
    assert test(s) == 'FAIL'
    n = 2
    while len(s) >= 2:
        start = 0
        subset_length = len(s) / n
        some_complement_fail = False
        while start < len(s):
            complement = s[:start] + s[start + subset_length:]
            if test(complement) == 'FAIL':
                s = complement
                n = max(n - 1, 2)
                some_complement_fail = True
                break

            start += subset_length

        if not some_complement_fail:
            n = min(n * 2, len(s))
            if n == len(s):
                break

    return s


htmp_input = '"<b>foo</b>"'
print delta_debug(htmp_input)