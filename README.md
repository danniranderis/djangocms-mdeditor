# djangocms-mdeditor

[![PyPI version](https://badge.fury.io/py/djangocms-mdeditor.svg)](https://badge.fury.io/py/djangocms-mdeditor)

djangocms-mdeditor is a ready-for-use addon for django CMS text editor using [Martor](https://github.com/agusmakmun/django-markdown-editor) as markdown-enabled text editor.
The addon provides simple text editing using markdown, or the WYSIWYG-style setup provided by Martor (supports Bootstrap and Semantic-UI).


## Requirements
`djangocms-mdeditor` is only tested with the following requirements.

- `Django>=3.2`
- `Martor>=1.6.4`
- `django-cms>=3.9`

## Installation WIP
`djangocms-mdeditor` is available directly from [PyPi][pypi].

1. Install the package into your project via e.g. `pip install djangocms-mdeditor`.
2. Add `djangocms-mdeditor` to your `INSTALLED_APPS`, similar to:

```python
# settings.py
INSTALLED_APPS = [
    ...
    'djangocms-mdeditor',
]
```

3. urls steps? any important for django-cms? WIP
4. Perform a database migration with `python manage.py migrate djangocms-mdeditor`.
5. If you don't have automatic static-collection configured for deployments, then remember to perform a `python manage.py collectstatic`.


## Usage WIP
Admins, templates etc. Reference to Martor for extra settings etc.?


## Changelog
The release history / changelog is listed in XX.


## Contributing
This is an open-source project. We'll be delighted to receive your feedback in the form of bug reports, bug fixes and new features in the form of issues and pull requests. These can be contributed on the projects [GitHub-page][github].

1. Fork the [repository][github] on GitHub.
2. Make a new branch from the `main`-branch (`git checkout -b feature/fooBar`).
3. And commit your changes to it (`git commit -am 'Add some fooBar'`).
4. WIP (install dev-requirements with pipenv and run tests)
5. Create a Pull Request with your contribution.

WIP - contribution guidelines / code-of-conduct?


## Contributors
The djangocms-mdeditor project was started and developed by [Danni Randeris][github-danni] in 2021.

Distributed under the MIT license. See ``LICENSE`` for more information.




[github]: https://github.com/danniranderis/djangocms-mdeditor
[pypi]: https://pypi.org/project/djangocms-mdeditor/
[github-danni]: https://github.com/danniranderis