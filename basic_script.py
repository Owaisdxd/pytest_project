#install pip install pytest==7.1.3
#it is a recommended version and it is being used large scale companies

import pytest

def test1():
  print("Hello World")

def test2():
  print("Test me")

#important thing to note if you name the function not starting with test login or logic then pytest will not test it 
#now you can run pytest -m basic_script.py  (if the pytest is not in your environment variable)
#python basic_script.py (if the pytest is in your envronment variable)
