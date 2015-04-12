from distutils.core import setup
from os import listdir
from os.path import join as path_join

setup(name='markov-words',
      version='0.1',
      packages=['markov_words'],
      scripts=[path_join(path, x) for x in listdir('bin')])
