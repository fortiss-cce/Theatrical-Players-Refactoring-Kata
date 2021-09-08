import math
from phases.phase4.calculation.performance_calculator import PerformanceCalculator, PerformanceCalculatorFactory
from typing import Any
from phases.phase4.model.play import Play


class Performance:
    def __init__(self, performance: dict[str, Any], play: Play):
        self.audience: int = performance["audience"]
        self.play: Play = play
        self.performance_calculator: PerformanceCalculator = PerformanceCalculatorFactory.create(play.type)


    def get_amount(self) -> int:
        return self.performance_calculator.get_amount(self)
        

    def get_volume_credits(self) -> int:
        return self.performance_calculator.get_volume_credits(self)
        