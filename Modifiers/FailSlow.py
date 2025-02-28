#!/usr/bin/env python

"""Utility to mark test that take too long time failed.

Can be used either as a separate script or as a pre-Rebot modifier as part of
test execution or when using Rebot.

Usage as a script:
    python FailSlow.py output_file max_seconds

Usage as a modifier:
    robot --prerebotmodifier FailSlow.py:max_seconds path/to/tests.robot
    rebot --prerebotmodifier FailSlow.py:max_seconds path/to/output.xml

Notice that when used as part of test execution, test statuses reported on
the console and in the output file are not affected. Changes are seen only in
the generated log and report files.
"""

import sys
from datetime import timedelta

from robot.api import ExecutionResult, SuiteVisitor
from robot.result import TestCase


class FailSlow(SuiteVisitor):

    def __init__(self, threshold: timedelta):
        self.threshold = threshold.total_seconds()

    def start_test(self, test: TestCase):
        elapsed = test.elapsed_time.total_seconds()
        if test.passed and elapsed > self.threshold:
            test.passed = False
            test.message = f'Execution time was over {self.threshold}s.'


if __name__ == '__main__':
    threshold, path = sys.argv[1:]
    result = ExecutionResult(path)
    visitor = FailSlow(timedelta(seconds=float(threshold)))
    result.suite.visit(visitor)
    result.save()
