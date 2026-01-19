from pydantic import Field, BaseModel, model_validator
from uuid import uuid4, UUID
from decimal import Decimal
from pathlib import Path

import json
class Item(BaseModel):
    item_number: str
    qty: int = Field(..., gt=0)
    price: Decimal = Field(..., gt=0)


class PurchaseOrder(BaseModel):
    order_number: str = Field(..., description="purchase order number")
    customer_id: int = Field(..., description="unique customer id")
    items: list[Item] = Field(..., description="list of purchase item")
    total: Decimal | None = Field(default=None, description="total purchase amount")
    payment_id: UUID = Field(..., description="payment reference id")

    @model_validator(mode='after')
    def calculate_total(self):
        self.total = Decimal(sum(item.qty * item.price for item in self.items))
        return self


PO1 = PurchaseOrder(order_number="PO1001", customer_id=123, items=[Item(item_number="101", qty=10, price=12)],payment_id="6f1d7e9e-4d4a-4b1a-b9a9-1f2e8cce0a1f")
 # PO1 Pydantic model (not JSON serializable)
 # model_dump() Converts to Python dict
 # json.dumps() Converts dict → JSON string


# x= json.dumps(PO1.model_dump(), indent=2, default=str)
x= PO1.model_dump_json(indent=2)
path= Path("purchase_order.json")
with path.open("w", encoding="utf-8") as f:
   f.write(x)

with path.open("r", encoding="utf-8") as r:
    order= json.load(r)
    print(order)