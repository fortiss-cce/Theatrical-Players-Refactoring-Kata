# Theatrical Players Refactoring Kata

This repo contains the starting point for an example from 'Refactoring' by Martin Fowler in several languages, with tests, so you can try it out for yourself.

## Background Story

Imagine a company of theatrical players who go out to various events performing plays. Typically, a customer will request a few plays and the company charges them based on the size of the audience and the kind of play they perform. There are currently two kinds of plays that the company performs: tragedies and comedies. The performers store data about their plays in a simple JSON file that looks something like this:

plays.json…

```json
{
    "hamlet": {"name": "Hamlet", "type": "tragedy"},
    "as-like": {"name": "As You Like It", "type": "comedy"},
    "othello": {"name": "Othello", "type": "tragedy"}
}
```

The data for their bills also comes in a JSON file:
invoices.json…

```json
[
    {
        "customer": "BigCo",
        "performances": [
            {
                "playID": "hamlet",
                "audience": 55
            },
            {
                "playID": "as-like",
                "audience": 35
            },
            {
                "playID": "othello",
                "audience": 40
            }
        ]
    }
]
```

As well as providing a bill for the performance, the company gives its customers "volume credits" which they can use for discounts on future performances - think of it as a customer loyalty mechanism.

The code that prints the bill is one simple function.

## Task - What you need to change

In this example the creators of the booking system want to add code to print the statement as HTML in addition to the existing plain text version.
The theatrical players also want to add new kinds of plays to their repertoire, for example history and pastoral.

---

> When you have to add a feature to a program but the code is not structured in a convenient way, first refactor the
>
> program to make it easy to add the feature, then add the feature.

Refactoring is usually driven by a need to make changes. The theatrical players have new requirements for the system.

## Automated tests

In his book Fowler mentions that the first step in refactoring is always the same - to ensure you have a solid set of tests for that section of code. However, Fowler did not include the test code for this example in his book. I have used an [Approval testing](https://medium.com/97-things/approval-testing-33946cde4aa8) approach and added some tests. I find Approval testing to be a powerful technique for rapidly getting existing code under test and to support refactoring. You should review these tests and make sure you understand what they cover and what kinds of refactoring mistakes they would expect to find.

## Acknowledgements

Thank you to Martin Fowler for kindly giving permission to use his code.
