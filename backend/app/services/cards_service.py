from typing import List, Optional
from app.schemas.cards_schema import CardSchema, CardImage
from app.db.cards_repository import CardRepository

class CardService:
    def __init__(self):
        self.repository = CardRepository()

    def list_cards(self, name: Optional[str], types: Optional[str], limit: int, in_stock_only: bool) -> List[CardSchema]:
        results = self.repository.get_cards(name, types, limit, in_stock_only)
        return [
            CardSchema(
                id=row["id"],
                supertype=row["supertype"],
                subtypes=row["subtypes"],
                name=row["name"],
                images=CardImage(small=row["small"], large=row["large"]),
                series=row["series"],
                rarity=row["rarity"],
                price=row["price"],
                stock=row['stock'],
                hp=row['hp'],
                types=row['types'],
                flavor_text=row['flavor_text']
            )
            for row in results
        ]
