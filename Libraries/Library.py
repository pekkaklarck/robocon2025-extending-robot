from enum import auto, Enum
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Literal

from robot.api.deco import keyword, library
from robot.api.exceptions import ContinuableFailure, SkipExecution


class EuroDate(date):
    """Date represented as dd.mm.yyyy."""

    @classmethod
    def from_string(cls, day: str) -> 'EuroDate':
        dt = datetime.strptime(day, '%d.%m.%Y')
        return cls(dt.year, dt.month, dt.day)


class Direction(Enum):
    """Turn direction."""
    LEFT = auto()
    RIGHT = auto()


@library(scope='SUITE',
         converters={EuroDate: EuroDate.from_string})
class Library:

    def __init__(self, state='INITIAL'):
        self.state = state

    @keyword
    def set_state(self, state: str):
        print(f'Old state was {self.state}.')
        self.state = state
        print(f'New state is {self.state}.')

    @keyword
    def conversion(self, number: Decimal, path: Path,
                   duration: timedelta):
        print(number * 2)
        print(path.name)
        print(duration.total_seconds())

    @keyword
    def move(self, direction: Literal['UP', 'DOWN', 'LEFT', 'RIGHT']):
        print(f'Moving {direction}')

    @keyword
    def turn(self, direction: Direction):
        if direction is Direction.LEFT:
            print('Turning left')
        else:
            print('Turning right')

    @keyword
    def birthday(self, day: EuroDate):
        today = EuroDate.today()
        day = day.replace(year=today.year)
        difference = (day - today).days
        print(f"It's {difference} days to your birthday!")

    @keyword(name='🤖')
    def robot(self):
        print('🤖')

    @keyword('This is a "${kind}" example')
    def example(self, kind):
        print(kind)

    @keyword('Number of ${animal} is')
    def number_of_animals_is(self, animal, count: int):
        print(animal, count)

    @keyword
    def skip_me(self):
        raise SkipExecution('Some good reason...')

    @keyword
    def continuable_failure(self, message):
        raise ContinuableFailure(message)

    @keyword
    def html_error(self):
        raise AssertionError('*HTML* Something <b>bad</b> happened!')
