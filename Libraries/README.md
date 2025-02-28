# Library API

In this directory we have examples related to creating libraries:

- [basics.py](basics.py) and [basics.robot](basics.robot) cover the basics of
  the library API. That includes creating a library as a module, creating keyword
  as a function, logging and reporting status.

- [Library.py](Library.py) and [tests.robot](tests.robot) cover more advanced
  features such as library state, passing arguments to libraries, automatic argument
  conversion (incl. enums and custom converters), the `@keyword` and `@library`
  decorators, embedded arguments, skipping tests and continuable failures.

- [Dynamic.py](Dynamic.py) and [dynamic.robot](dynamic.robot) quickly introduce
  the dynamic library API. This API is used, for example, by the
  [Remote library API](https://github.com/robotframework/RemoteInterface) and
  [PythonLibCore](https://github.com/robotframework/PythonLibCore) that in turn
  is used by [SeleniumLibrary](https://github.com/robotframework/SeleniumLibrary)
  and several other bigger libraries.

For more details about these features, and many more, see the
[Creating test libraries](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-libraries)
section in the *Robot Framework User Guide*.
