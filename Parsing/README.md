# Parsing API

This directory quickly introduced Robot Framework's parsing API.

- [tokens.py](tokens.py) shows how to parse a test case file into tokens. This
  is a pretty low level API that can be used, for example, by syntax highlighters.
  Token values could be written back to the disk and modified on the fly. Run
  the script like `python tokens.py tests.robot` to get tokens in
  [tests.robot](tests.robot) printed to the console.

- [model.py](model.py) demonstrates using a higher level parsing API that returns
  a model that is easier to inspect and modify than raw tokens. The model is
  implemented on top of Python's [ast](https://docs.python.org/3/library/ast.html)
  module and internally contains the lower level tokens. Run
  `python model.py tests.robot` to get the model from [tests.robot](tests.robot) shown
  on the console. The script also modifies the model, writes modified data back
  to the disk, and creates an executable suite based on the model and runs it.

For more information see the
[parsing API documentation](https://robot-framework.readthedocs.io/en/stable/autodoc/robot.api.html#module-robot.api.parsing).
