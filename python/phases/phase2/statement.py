

from . import statement_data

def format_as_dollars(amount):
    amount = amount/100
    return f"${amount:0,.2f}"

def render_plain_text(data):
    result = f'Statement for {data["customer"]}\n'
    
    for perf in data["performances"]:
        # print line for this order
        result += f' { perf["play"]["name"]}: {format_as_dollars(perf["amount"])} ({perf["audience"]} seats)\n'
    
    result += f'Amount owed is {format_as_dollars(data["total_amount"])}\n'
    result += f'You earned {data["total_volume_credits"]} credits\n'
    return result

def statement(invoice, plays):
    data = statement_data.calculate_data(invoice, plays)
    return render_plain_text(data)





