# Python Learning Notes

## Introduction

- There are some notes about Python learning for author.
- It contains three parts: *Grammar, Function, and Tips.*
- In this page, **str** means *class string*, and *str* means string.


## Grammar

- About *String* :
  - """*str*""" : *Keep string as it is including newlines, escape characters.*
      ```py
      # For example:
      # >>> a = """this is first line,
      #     this is second line.\n\n"""
      # >>> print(a)
      this is first line,
      this is second line.\n\n
      ```
  - r"*str*"&nbsp; : *Automatically skip escape characters.*
- About *Operation* :
  - a ** b : *It means $a^{b}$.*
  - a // b : *It means $\lfloor\frac{a}{b}\rfloor$ and keep the original type like 2.5 // 2 == 1.0.*
- About different with other language :
  - `else if` in C++ is equal to `elif` in Python.
  - `x if x < y else y` is a Ternary Operator. It has the same function with `x < y ? x : y` in C++ language.
- About list : a = [ ]
  - a[[start=0]:[end=len]] : *Gets a sublist of the index from start to end-1. It is used to get a copy.*
  - a * **constant** : *Gets a list of **constant** times the length and **constant** times the content.*


## Function

- isinstance (var, type) : *When the type of variable is equal to type, return true.*
- assert *Expression* : *If the value of expression is `False`, exit program and return `Exception: AssertionError`.* 
- range([start], stop, [step=1]) : *By using this function, we can get a sequence of numbers from the parameter 'start' value to the end of the parameter 'stop' value.*
    ```html
    The parameter 'start' and 'step' can be defaulted, and the default step is 1.
    eg. range(0, 5) is equal to range(5).
        In fact, you can get [0, 5) after running.
    ```
- About List : a = [ ]
  - append(*element*) : *Adds an element to the end of list. The length of the list will increase by one.*
  - extend(*list*) : *Adds all elements of another list to the end of the list. The length of the list will increase by the length of another list. By the way, `(list1 + list2) == list1.extend(list2)`*
  - insert(*index, element*) : *Adds an element to the position of index in list.*
    ```py
    # For example:
    >>> a = ['a', 1]
    >>> a.append('Peace')
    >>> print(a)
    ['a', 1, 'Peace']
    >>> a.extend([2, 3])
    >>> print(a)
    ['a', 1, 'Peace', 2, 3]
    >>> a.append([2, 3])
    >>> print(a)
    ['a', 1, 'Peace', 2, 3, [2, 3]]
    >>> a.insert(1, 'b')
    >>> print(a)
    ['a', 'b', 1, 'Peace', 2, 3, [2, 3]]
    ```
  - remove(*element*) : *Takes a single element as an argument and removes it from list. If this element does not exist, valueRrror exception is thrown.*
  - **del** *object/variable/list[index]* : **del** *can be used to delete an object, a variable and an element in a list.*
  - pop([index=len-1]) : *Removes the element at the given index from the list. The default index is len-1.*
  - count(*element*) : *Get the number of occurrences of an element in a list.*
  - index(*element*, [start=0], [end=len]) : *Get the index of element between the start and the end-1 in a list.*

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

- Due to unique indentation format requirements, Python language can avoid "*ambiguity of else*". 
    - The following code will get an unexpected running in C++ but it will be correct in Python.
        ```C++
        if (a > b) 
            if (c > d)
                ...
        else
            ...
        ```

