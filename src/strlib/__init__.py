# SPDX-FileCopyrightText: 2023-present Joshua Rose <joshuarose@gmx.com>
#
# SPDX-License-Identifier: MIT


def reverse(string: str):
    """
    Reverse the contents of a string.

    string: A string where the contents will be reversed in order.


    # Examples

    ```python
    >>> reverse("foobar")
    "raboof"

    >>> reverse("python")
    "nohtyp"

    >>> reverse("Anne")
    "ennA"

    >>> reverse({1, 2, 3})
    TypeError
    ```
    """

    if not isinstance(string, str):
        raise TypeError("Cannot reverse a given type (requires string): %s" % type(string))
