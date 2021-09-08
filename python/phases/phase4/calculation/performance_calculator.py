import abc
import math
from phases.phase4.model.performance import Performance
from phases.phase4.model.play import PlayType


class PerformanceCalculator(abc.ABC):

    @abc.abstractmethod
    def get_amount(self, performance: "Performance") -> int:
        pass

    def get_volume_credits(self, performance: "Performance") -> int:
        return max(performance.audience - 30, 0)


class ComedyCalculator(PerformanceCalculator):

    def get_amount(self, performance: "Performance") -> int:
        result = 30000
        if performance.audience > 20:
            result += 10000 + 500 * (performance.audience - 20)

        result += 300 * performance.audience
        return result

    def get_volume_credits(self, performance: "Performance") -> int:
        result = super().get_volume_credits(performance)
        # add extra credit for every ten comedy attendees
        result += math.floor(performance.audience / 5)
        return result


class TragedyCalculator(PerformanceCalculator):

    def get_amount(self, performance: "Performance") -> int:
        result = 40000
        if performance.audience > 30:
            result += 1000 * (performance.audience - 30)
        return result
        

class PerformanceCalculatorFactory:

    @staticmethod
    def create(type: PlayType) -> PerformanceCalculator:
        switcher = {
            PlayType.COMEDY: ComedyCalculator,
            PlayType.TRAGEDY: TragedyCalculator
        }
        calculator = switcher.get(type)
        if calculator is None:
            raise ValueError(f'unknown type: {type}')
        return calculator()