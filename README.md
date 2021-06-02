# Theatrical Players Refactoring Kata

This repo contains the starting point for an example from 'Refactoring' by Martin Fowler in several languages, with tests, so you can try it out for yourself.

## Background Story
-----------------
Image a company of theatrical players who go out to various events performing
plays. Typically, a customer will request a few plays and the company charges
them based on the size of the audience and the kind of play they perform. There
are currently two kinds of plays that the company performs: tragedies and
comedies. As well as providing a bill for the performance, the company gives its
customers “volume credits” which they can use for discounts on future performances—think of it as a customer loyalty mechanism.
The performers store data about their plays in a simple JSON file that looks
something like this:
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
The code that prints the bill is one simple function.

## Task - What you need to change
-----------------------

>When you have to add a feature to a program but the code
is not structured in a convenient way, first refactor the
program to make it easy to add
the feature, then add the
feature.


Refactoring is usually driven by a need to make changes. The theatrical players have new requirements for the system.
Your task is **NOT** to implement these requirements but to refactor the code to enable fast and easy implementation
of the requirements later on. You should therefore extract methods and classes and implements suitable restructurings 
that enhance the overall code quality
but especially prepare the system for the wanted changes.

**Tip**:
* Do start with adding structure by extracting logical units/methods from the large ``statement method`` (including Session 1)
* Separate concerns by splitting formatting and calculation logic
* Add object orientation (if not already done)
* Prepare for change by adding polymorphism and applying patterns



### Wanted change (do not implement them)
In this example the creators of the booking system want to add code to print the statement as HTML in addition to the existing plain text version.
The theatrical players also want to add new kinds of plays to their repertoire, for example history and pastoral.

In this case, we have a couple of changes that the users would like to make.
1. They want a statement printed in HTML.
Consider what impact this change would
have. I’m faced with adding conditional
statements around every statement that
adds a string to the result. That will add
a host of complexity to the function.
2. The players are looking to perform more
kinds of plays: they hope to add history, pastoral, pastoral-comical, historical-pastoral, 
tragical-historical, tragical-comical-historical-pastoral, scene individable,
and poem unlimited to their repertoire. They haven’t exactly decided yet what
they want to do and when. This change will affect both the way their plays are
charged for and the way volume credits are calculated. 
Furthermore, as the rules grow in complexity, it’s going to be harder to figure out where to make the
changes and harder to do them without making a mistake.

## Automated tests
---------------
In his book Fowler mentions that the first step in refactoring is always the same - to ensure you have a solid set of tests for that section of code. However, Fowler did not include the test code for this example in his book. I have used an [Approval testing](https://medium.com/97-things/approval-testing-33946cde4aa8) approach and added some tests. I find Approval testing to be a powerful technique for rapidly getting existing code under test and to support refactoring. You should review these tests and make sure you understand what they cover and what kinds of refactoring mistakes they would expect to find.

## Acknowledgements
----------------
Thank you to Martin Fowler for kindly giving permission to use his code.
