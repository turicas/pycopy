# coding: utf-8

from setuptools import setup


setup(name='pycopy',
      description='API wrapper to Copy.com',
      long_description='API wrapper to Copy.com compatible with Dropbox API',
      version='0.1.0-dev',
      author=u'Álvaro Justen',
      author_email='alvarojusten@gmail.com',
      url='https://github.com/turicas/pycopy/',
      py_modules=['pycopy'],
      install_requires=['requests'],
      keywords=['copy', 'file', 'storage', 'dropbox'],
      entry_points = {},
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)
