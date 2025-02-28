"""Pre-run modifier to select only every Xth test for execution.

Usage:
    robot --prerunmodifier SelectEveryXth.py[:x][:start] path/to/tests.robot

Also demonstrates modifying tests and using the new GROUP syntax programmatically.
"""

from robot.api import SuiteVisitor
from robot.running import TestCase, TestSuite


class SelectEveryXth(SuiteVisitor):

    def __init__(self, x: int = 2, start: int = 0):
        self.x = x
        self.start = start

    def start_suite(self, suite: TestSuite):
        suite.tests = suite.tests[self.start::self.x]

    def visit_test(self, test: TestCase):
        group = test.body.create_group('New group')
        group.body.create_keyword('Log', ['Hello!'])
        group.body.create_keyword('Log', ['Hi, again!'])
