"""
simple restructuring to be extensible for different play types.

if things need to get more complicated, the PERFORMANCES dict
should become a class, and one could even start inheritance then.
"""


def tragedy_price(audience_size):
    amount = 40000
    if audience_size > 30:
        amount += 1000 * (audience_size - 30)
    return amount


def comedy_price(audience_size):
    amount = 30000
    if audience_size > 20:
        amount += 10000 + 500 * (audience_size - 20)

    amount += 300 * audience_size
    return amount


PERFORMANCES = {
    "tragedy": {
        "price": tragedy_price,
        "volume_credits": lambda _: 0,
    },
    "comedy": {
        "price": comedy_price,
        "volume_credits": lambda audience: audience // 5,
    },
}


def calculate_price(invoice, plays):
    total_amount = 0
    volume_credits = 0
    play_prices = list()

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        audience = perf['audience']

        prices = PERFORMANCES.get(play['type'])
        if prices is None:
            raise ValueError(f'unknown performance type: {play["type"]}')

        # base price + extra price depending on audience size
        this_amount = prices['price'](audience)

        # generate volume credits, starting at 30 watchers
        volume_credits += max(audience - 30, 0)

        # extra atendee credits
        volume_credits += prices['volume_credits'](audience)

        # print line for this order
        play_prices.append((play['name'], this_amount, audience))
        total_amount += this_amount

    return play_prices, volume_credits, total_amount


def format_as_dollars(amount):
    return f"${amount/100:0,.2f}"


def statement(invoice, plays):
    result = list()
    result.append(f'Statement for {invoice["customer"]}')

    play_prices, volume_credits, total_amount = calculate_price(invoice, plays)
    for name, amount, audience in play_prices:
        result.append(f' {name}: {format_as_dollars(amount)} '
                      f'({audience} seats)')

    result.append(f'Amount owed is {format_as_dollars(total_amount)}')
    result.append(f'You earned {volume_credits} credits')
    return "\n".join(result)
