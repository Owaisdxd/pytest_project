#what is test fixture
import pytest

#setup_function is a keyword
def setup_function(function):       #this function will run before the tetsing of each function
  print("Starting to test function")
#teardown_fucntion is keyword
def teardown_function(function):    #this function will run before ending the test of every function
  print("Ending function testing")

def setup_module(module):   #this function will run before starting the whole test
  print("Starting the test")

def teardown_module(module):  #this function will run before ending the whole test
  print("Ending the test")

def test1():
  print("Test one")
def test2():
  print("test 2")
