# Listener interface

This directory demonstrates Robot Frameworks listener interface:

- [stop_on_error.py](stop_on_error.py) is a listener that can be used from
  the command line to stop execution if a test fails:

      robot --listener stop_on_error.py tests.robot

- [Modifier.py](Modifier.py) modifies tests dynamically. It can be used the same way
  as the listener above. It uses the optional `robot.api.interfaces.ListenerV3`
  base class and utilizes type hints.

- [LibraryListener.py](LibraryListener.py) demonstrates how a library can
  register a listener or be a listener itself. The library is used by
  [tests.robot](tests.robot) and doesn't need to be taken into use from
  the command line separately.

For more information see the
[Listener interface](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#listener-interface)
section in the *Robot Framework User Guide*.
