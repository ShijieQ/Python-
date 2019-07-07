# Python Learning Notes

## Introduction
- There are some notes about Python learning for author.
- It contains three parts: *Grammar, Function, and Tips.*
- In this page, **str** means *class string*, and *str* means string.

## Grammar
- """*str*""" : *Keep string as it is including newlines, escape characters.*
```py
    >>> a = """this is first line,
        this is second line.\n\n"""
    >>> print(a)
    this is first line,
    this is second line.\n\n
```
- r"*str*"&nbsp; : &emsp;*Automatically skip escape characters.*
- a ** b : &emsp;*It means $a^{b}$.*
- a // b : &emsp;*It means $\lfloor\frac{a}{b}\rfloor$ and keep the original type like 2.5 // 2 == 1.0.*

## Function
- isinstance (var, type) : *When the type of variable is equal to type, return true.*

## Tips
- The operator '`-`' has a lower priority than the operator '`**`'. For example, -3 ** 2 == -9.
- Priority order table :

    |         Type         |       Operator       | Precedence |
    | :------------------: | :------------------: | :--------: |
    |    Power operator    |          **          |     1      |
    |   Unary plus/minus   |        +x, -x        |     2      |
    | Arithmetic operators |    *, /, //, +, -    |     3      |
    | Comparison operators | <, <=, >, >=, ==, != |     4      |
    |   Logical operator   |     not, and, or     |     5      |