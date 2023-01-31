---
title: "The Decorator"
date: 2023-01-31T17:09:20Z
draft: false
---

The Decorator is used to add behaviour to an existing function. Decorators allow
the programmer to run logic before and after a function runs. In the example below
the `example_decorator` prints `"Before function runs."`, runs the function that 
it decorates (in this case the function `do_something`) then prints `"After function runs."`

Where you find code repeated in multiple functions, a decorator may be useful.

```
from functools import wraps

def example_decorator(func):
    @wraps(func)
    def _inner(*args, **kwargs):
        # do something before function runs.
        print("Before function runs.")
        func(*args, **kwargs)
        # do something after function has run.
        print("After function runs.")
    return _inner
```

```
@example_decorator
def do_something():
    """Pretends to do something.
    """
    print("I'm doing something! (nothing really).")
```
Output:

`
Before function runs.
`

`
I'm doing something! (nothing really).
`

`
After function runs.
`

Additional use cases.

## You can decorate a decorator