from phases.phase4.model.play import Play
from phases.phase4.model.performance import Performance
from typing import Any

def init_play(plays: dict[str, Any], id: str) -> Play:
    play = plays[id]
    return Play(id, play["name"], play["type"])

class Invoice:

    def __init__(self, plays: dict[str, Any], invoice: dict[str, Any]):
        self.customer: str = invoice["customer"]
        self.performances: list[Performance] = [Performance(performance, init_play(plays, performance["playID"])) for performance in invoice["performances"]]



    def total_volume_credits(self) -> int: 
        result = 0
        for perf in self.performances:
            result += perf.get_volume_credits()
        return result

    def total_amount(self) -> int:
        result = 0
        for perf in self.performances:
            result += perf.get_amount()
        return result