def mulf(*vars):
    """ggd

    >>> mulf(1, 2)
    2
    >>> mulf(1,2,3,4)
    24

    """

    v = 1
    for i in vars:
        v *= i
    return v
