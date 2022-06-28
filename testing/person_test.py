#!/usr/bin/env python

from lib.person import Person

import io
import sys
import types

class TestDog:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        guido = Person()
        assert(type(guido) == Person)

class TestTalk:
    '''Person.talk() in person.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        assert(type(guido.talk) == types.MethodType)

    def test_prints_hello_world(self):
        '''prints "Hello world!"'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.talk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello world!\n")

class TestWalk:
    '''Person.walk() in walk.py'''

    def test_is_method(self):
        '''is an instance method'''
        guido = Person()
        assert(type(guido.walk) == types.MethodType)

    def test_prints_the_person_is_walking(self):
        '''prints "The person is walking."'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.walk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The person is walking.\n")
