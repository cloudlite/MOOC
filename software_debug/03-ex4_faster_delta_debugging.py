__author__ = 'cloudlite'
#
# Finish the simplify function.
# Have it deal with the case where test(s1) doesn't fail
#
# If neither s1 or s2 cause the test to fail then return
# the original string, s.

import re

test_count = 0


def test(s):
    global test_count
    test_count += 1
    print test_count, repr(s), len(s)
    s_merged = ''.join(s)
    if re.search("<SELECT[^>]*>", s_merged) >= 0:
        return "FAIL"
    else:
        return "PASS"


def my_dd(s):
    assert test(s) == 'FAIL'
    n = 2

    while len(s) >= 2:
        start = 0
        subset_len = len(s) / n
        some_compliment_fail = False
        while start < len(s):
            complement = s[:start] + s[start + subset_len:]
            if test(complement) == 'FAIL':
                s = complement
                n = max(n - 1, 2)
                some_compliment_fail = True
                break
            start += subset_len

        if not some_compliment_fail:
            n = min(2 * n, len(s))
            if n == len(s):
                break

    return s


# html_input = '<SELECT><OPTION VALUE="simplify"><OPTION VALUE="beautify"></SELECT>'
html_input = ['<SELECT>', 'foo', '</SELECT>']
print my_dd(html_input)