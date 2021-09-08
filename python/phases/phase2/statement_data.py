import math

def playFor(plays, performance):
    return plays[performance["playID"]]

def amountFor(performance):
    result = 0
    if performance["play"]['type'] == "tragedy":
            result = 40000
            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
    elif performance["play"]['type'] == "comedy":
        result = 30000
        if performance['audience'] > 20:
            result += 10000 + 500 * (performance['audience'] - 20)

        result += 300 * performance['audience']
    else:
        raise ValueError(f'unknown type: {performance["play"]["type"]}')
    return result

def volumeCreditsFor(performance):
    result = max(performance['audience'] - 30, 0)
    # add extra credit for every ten comedy attendees
    if "comedy" == performance["play"]["type"]:
        result += math.floor(performance['audience'] / 5)
    return result

def total_volume_credits(performances): 
    result = 0
    for perf in performances:
        # add volume credits
        result += perf["volumeCredits"]
    return result

def total_amount(performances):
    result = 0
    for perf in performances:
        # print line for this order
        result += perf["amount"]
    return result

def enrich_performance(plays, performance):
    performance["play"] = playFor(plays, performance)
    performance["amount"] = amountFor(performance)
    performance["volumeCredits"] = volumeCreditsFor(performance)
    return performance

def calculate_data(invoice, plays):
    calculated_data = {
        "customer": invoice["customer"],
        "performances": [enrich_performance(plays, performance) for performance in invoice["performances"]],
    }
    calculated_data["total_amount"] = total_amount(calculated_data["performances"])
    calculated_data["total_volume_credits"] = total_volume_credits(calculated_data["performances"])
    return calculated_data