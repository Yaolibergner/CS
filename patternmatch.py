"""Check if pattern matches.

Given a "pattern string" starting with "a" and including only "a" and "b"
characters, check to see if a provided string matches that pattern.

For example, the pattern "aaba" matches the string "foofoogofoo" but not
"foofoofoodog".

Patterns can only contain a and b and must start with a:

    >>> pattern_match("b", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("A", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

    >>> pattern_match("abc", "foo")
    Traceback (most recent call last):
    ...
    AssertionError: invalid pattern

The pattern can contain only a's:

    >>> pattern_match("a", "foo")
    True

    >>> pattern_match("aa", "foofoo")
    True

    >>> pattern_match("aa", "foobar")
    False

It's possible for a to be zero-length (a='', b='hi'):

    >>> pattern_match("abbab", "hihihi")
    True

Or b to be zero-length (a='foo', b=''):

    >>> pattern_match("aaba", "foofoofoo")
    True

Or even for a and b both to be zero-length (a='', b=''):

    >>> pattern_match("abab", "")
    True

But, more typically, both are non-zero length:

    >>> pattern_match("aa", "foodog")
    False

    >>> pattern_match("aaba" ,"foofoobarfoo")
    True

    >>> pattern_match("ababab", "foobarfoobarfoobar")
    True

Tricky: (a='foo', b='foobar'):

    >>> pattern_match("aba" ,"foofoobarfoo")
    True
"""

def pattern_match(pattern, astring):
    assert (pattern.replace("a", "").replace("b", "") == ""
            and pattern.startswith("a")), "invalid pattern"


    count_a = pattern.count("a") # num times a appears in pattern
    count_b = pattern.count("b")
    first_b = pattern.find("b")

    # check the possible len of a and b

    for a_len in range(0, len(astring) // count_a + 1):
        if count_b:
            b_len = ((len(astring) - a_len*count_a)) / count_b
        else:
            b_len = 0

    if int(b_len) != b_len or b_len < 0:
        return False

    b_start = first_b * a_len

    return _pattern_match(pattern, astring, a=astring[0: a_len], b=astring[b_start:b_start + int(b_len)])

def _pattern_match(pattern, astring, a, b):
    """Can we make this pattern match this string?"""
    #print(pattern, astring, a, b)
    # if not pattern:
    #     return astring == ""

    # first_char = pattern[0]
    # if first_char == 'a':
    #     token = a
    # elif first_char == 'b':
    #     token = b

    # possible = []
    # if token is not None:
    #     if astring.startswith(token):
    #         possible = [token]
    # else:
    #     possible = []
    #     for i in range(len(astring)+1):
    #         p = astring[0:i]
    #         possible.append(p)

    # for p in possible:
    #     if first_char == 'a':
    #         a = p
    #     elif first_char == 'b':
    #         b = p
    #     if _pattern_match(pattern[1:], astring[len(p):], a=a, b=b):
    #         return True

    # return False

    test_string = ""

    for p in pattern:

        if p =="a":
            test_string += a
        else:
            test_string += b

    return test_string == astring


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WE'RE WELL-MATCHED!\n")
