from typing import List, Optional
from app.schemas.cards_schema import CardSchema, CardImage
from app.db.cards_repository import CardRepository

class CardService:
    def __init__(self):
        self.repository = CardRepository()

    def list_cards(self, name: Optional[str], types: Optional[str], limit: int) -> List[CardSchema]:
        results = self.repository.get_cards(name, types, limit)
        return [
            CardSchema(
                id=row["id"],
                name=row["name"],
                images=CardImage(small=row["small"]),
                series=row["series"],
                rarity=row["rarity"],
                price=row["price"]
            )
            for row in results
        ]
