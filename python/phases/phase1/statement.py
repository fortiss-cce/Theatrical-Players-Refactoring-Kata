import math

def playFor(plays, performance):
    return plays[performance["playID"]]


def calculate_amount_for_performance(performance, play):
    result = 0
    if play['type'] == "tragedy":
            result = 40000
            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
    elif play['type'] == "comedy":
        result = 30000
        if performance['audience'] > 20:
            result += 10000 + 500 * (performance['audience'] - 20)

        result += 300 * performance['audience']
    else:
        raise ValueError(f'unknown type: {play["type"]}')
    return result


def calculate_volume_credits_for_performance(plays, performance):
    result = max(performance['audience'] - 30, 0)
    # add extra credit for every ten comedy attendees
    if "comedy" == playFor(plays, performance)["type"]:
        result += math.floor(performance['audience'] / 5)
    return result


def format_as_dollars(amount):
    amount = amount/100
    return f"${amount:0,.2f}"


def total_volume_credits(plays, invoice): 
    volume_credits = 0
    for perf in invoice['performances']:
        # add volume credits
        volume_credits += calculate_volume_credits_for_performance(plays, perf)
    return volume_credits

def total_amount(plays, invoice):
    result = 0
    for perf in invoice['performances']:
        # print line for this order
        result += calculate_amount_for_performance(perf, playFor(plays, perf))
    return result


def statement(invoice, plays):
    result = f'Statement for {invoice["customer"]}\n'
    
    for perf in invoice['performances']:
        # print line for this order
        result += f' { playFor(plays, perf)["name"]}: {format_as_dollars(calculate_amount_for_performance(perf, playFor(plays, perf)))} ({perf["audience"]} seats)\n'
    
    result += f'Amount owed is {format_as_dollars(total_amount(plays, invoice))}\n'
    result += f'You earned {total_volume_credits(plays, invoice)} credits\n'
    return result


