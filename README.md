Reservas
========

Demo for a lean architecture django setup.

version 0.3.0

## requirements

- python 3.12+

## dev setup

install project dependencies

```
$ python -m venv .venv
$ source .venv/bin/activate
(venv) $ pip install -e .
```
> optional development requirements are included `pip isntall -e .[dev]`.
> pre-commit hooks are provided, install using `pre-commit install`.

setup database

```
reservas migrate
```

> project is configured to use environment variables using django-environ

## contributing

fork, patch, merge, repeat.

## roadmap

- [X] authorization
- [ ] unit test scaffolding.
- [ ] rest interface tests.
- [ ] docker configuration
- [ ] more environment variables. mainly database related.
- [X] better logging.
- [ ] enable mypy.
- [ ] a `CHANGELOG`.
- [ ] remove ModelViewset ussage in favor of specific bussiness cases.

## licence

MIT, read `LICENCE`

author: hola@bigpear.com.ar, matias.iturburu@bigpear.com.ar
