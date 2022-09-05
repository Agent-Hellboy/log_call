## log_call 

library to log function or bond-method calls

## Installation

    for stable version
       - pip install log_call

    for developement
       - git clone https://github.com/Agent-Hellboy/log_call
       - cd log_call
       - python -m venv .venv
       - source .venv/bin/activate
       
### Example

Import log_call from log_call and decorate your class or function with it
```py
from log_call import log_call

@log_call
class A:
    def __init__(self):
        pass 

    def a(self,*args,**kwargs):
        pass


a=A()
a.a(45,'str',s=34,g=43)

@log_call
def c(a,*args,**kwargs):
    pass

c(34,56,p=23)
```

```
response 
2022-09-04 12:56:08,552 a called with {'args': [45, 'str'], 'kwargs': {'s': 34, 'g': 43}}
2022-09-04 12:56:08,552 c called with {'a': 34, 'args': [56], 'kwargs': {'p': 23}}
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.