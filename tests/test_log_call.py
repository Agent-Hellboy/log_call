import os
import pytest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from log_call import log_call

@pytest.fixture
def log_call_fixture():

    def func(param1,*args,**kwargs):
       pass
    
    class TestClass:
       def __init__(self):
           pass 

       def method(self,*args,**kwargs):
           pass
    
    # someone may subclass int/bool and try to decorate it
    test_int = 2
    test_bool = True

    fixture1 = log_call(func)
    fixture2 = log_call(TestClass)
    fixture3 = log_call(test_int)
    fixture4 = log_call(test_bool)
    
    return fixture1,fixture2,fixture3,fixture4

def test_with_fixture(log_call_fixture):
    assert log_call_fixture[0].__module__ == 'tests.test_log_call'
    assert log_call_fixture[1].__dict__['__module__'] == 'log_call'
    assert log_call_fixture[2] is None
    assert log_call_fixture[3] is None 