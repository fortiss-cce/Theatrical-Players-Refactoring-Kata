from .model.invoice import Invoice

def format_as_dollars(amount):
    amount = amount/100
    return f"${amount:0,.2f}"

class Printer:

    def __init__(self, invoice: Invoice):
        self.data = invoice

    def render_plain_text(self) -> str:
        result = f'Statement for {self.data.customer}\n'
        
        for performance in self.data.performances:
            result += f' { performance.play.name}: {format_as_dollars(performance.get_amount())} ({performance.audience} seats)\n'
        
        result += f'Amount owed is {format_as_dollars(self.data.total_amount())}\n'
        result += f'You earned {self.data.total_volume_credits()} credits\n'
        return result