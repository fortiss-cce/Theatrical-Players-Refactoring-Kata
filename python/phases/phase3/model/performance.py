import abc
import math
from typing import Any
from phases.phase3.model.play import Play, PlayType

class Performance:
    def __init__(self, performance: dict[str, Any], play: Play):
        self.audience: int = performance["audience"]
        self.play: Play = play


    def get_amount(self) -> int:
        result = 0
        if self.play.type == PlayType.TRAGEDY:
                result = 40000
                if self.audience > 30:
                    result += 1000 * (self.audience - 30)
        elif self.play.type == PlayType.COMEDY:
            result = 30000
            if self.audience > 20:
                result += 10000 + 500 * (self.audience - 20)

            result += 300 * self.audience
        else:
            raise ValueError(f'unknown type: {self.play.type}')
        return result


    def get_volume_credits(self) -> int:
        result = max(self.audience - 30, 0)
        # add extra credit for every ten comedy attendees
        if self.play.type == PlayType.COMEDY:
            result += math.floor(self.audience / 5)
        return result