# `pycopy`

[![Join the chat at https://gitter.im/turicas/pycopy](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/turicas/pycopy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License: GPLv3](https://img.shields.io/pypi/l/pycopy.svg)](https://github.com/turicas/pycopy/blob/develop/LICENSE)
[![Current version at PyPI](https://img.shields.io/pypi/v/pycopy.svg)](https://pypi.python.org/pypi/pycopy)
[![Downloads per month on PyPI](https://img.shields.io/pypi/dm/pycopy.svg)](https://pypi.python.org/pypi/pycopy)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/pycopy.svg)
![Software status](https://img.shields.io/pypi/status/pycopy.svg)
[![Donate](https://img.shields.io/gratipay/turicas.svg?style=social&label=Donate)](https://www.gratipay.com/turicas)


## Features

- Dropbox-compatible Python API
- Python3 and PyPy support

## Developing

You can create all needed virtualenvs using `tox` but I prefer to run the tests
by myself (see `runtests.sh` -- it just activates every virtualenv and run
`nosetests` inside it).


## Future Work

- Django storage backend (like
  [django-dropbox](https://pypi.python.org/pypi/django-dropbox))
- FUSE-copy (may replace [copy-fuse](https://github.com/copy-app/copy-fuse/))
- Add a `Provider` to [libcloud
  storage](https://libcloud.readthedocs.org/en/latest/storage/index.html)


## Semantic Versioning

This library uses [semantic versioning](http://semver.org). Note that it means
we do not guarantee API backwards compatibility on `0.x.y` versions.


## License

This library is released under the [GNU General Public License version
3](http://www.gnu.org/licenses/gpl-3.0.html).
