# python-header

Parses module headers

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Examples](#examples)
- [License](#license)

## Features

- Gets author (from @author)
- Gets version (from @version)

## Setup

```bash
git clone https://github.com/hankadler/python-header header
cd header
mkdir .venv
pipenv shell
pipenv install
```

## Examples

Let **module.py** contain the following docstring at the beginning:

```python
"""
module.py
    A python module.

@author   John Smith
@version  0.1.0  2020-01-01
"""
```

Open python interpreter on directory containing **module.py** and:

### Get Author

```
>>> import header
>>> author = header.getAuthor('./module.py')
>>> author
'John Smith'
```

### Get Version

```
>>> import header
>>> version = header.getVersion('./module.py')
>>> version
'0.1.0'
```

## License

[MIT](LICENSE)
