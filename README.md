# pytest-setuppy-err
Minimal working example for "unrecognized arguments" error

When running this on Linux, pytest will not accept arguments, see: [StackOverflow question](https://stackoverflow.com/questions/47095053/pytest-unrecognized-argument-on-cli-invocation-despite-being-defined?noredirect=1#comment81177490_47095053)

```
python setup.py --addopts "-s"  # OK

python setup.py --addopts "-s --config foobar.does-not-exist"  # OK

python setup.py --addopts "-s --config foo.bar"  # FAIL 

#usage: pytest [options] [file_or_dir] [file_or_dir] [...]
#pytest: error: unrecognized arguments: --config
#  inifile: None
#  rootdir: /uupmaker


```

This error happens when invoking tests via `pytest -s --config foo.bar` as well. Not limited to setup.py invocation.
