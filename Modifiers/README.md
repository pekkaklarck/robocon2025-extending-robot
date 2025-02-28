# Model modifiers

This directory demonstrates modifying tests and results using model modifiers
and otherwise.

Examples:

    robot --prerunmodifier SelectEveryXth.py tests.robot
    robot --prerunmodifier SelectEveryXth.py:2:1 tests.robot
    robot --prerebotmodifier FailSlow.py:0.1s tests.robot

See docstrings of [SelectEveryXth.py](SelectEveryXth.py) and
[FailSlow.py](FailSlow.py) for more details about their usage.

Using model modifiers is explained in the
[Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#programmatic-modification-of-test-data).
The visitor interface as well as model objects used by modifiers are  documented
as part of the [Robot Framework API docs](http://robot-framework.readthedocs.org/).
