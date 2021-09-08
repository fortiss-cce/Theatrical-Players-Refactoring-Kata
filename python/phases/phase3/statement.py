from typing import Any
from .printer import Printer
from .model.invoice import Invoice


def statement(invoice: dict[str, Any], plays: dict[str, Any]):
    data = Invoice(plays, invoice)
    return Printer(data).render_plain_text()





