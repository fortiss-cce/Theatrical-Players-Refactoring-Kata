from phases.phase4.model.invoice import Invoice

def format_as_dollars(amount):
    amount = amount/100
    return f"${amount:0,.2f}"

class Printer:

    def __init__(self, data: Invoice):
        self.data = data

    def render_plain_text(self) -> str:
        result = f'Statement for {self.data.customer}\n'
        
        for perf in self.data.performances:
            # print line for this order
            result += f' { perf.play.name}: {format_as_dollars(perf.get_amount())} ({perf.audience} seats)\n'
        
        result += f'Amount owed is {format_as_dollars(self.data.total_amount())}\n'
        result += f'You earned {self.data.total_volume_credits()} credits\n'
        return result