from typing import List, Optional
from app.schemas.cards_schema import CardSchema, CardImage, CardUpdateRequest
from app.db.cards_repository import CardRepository

class CardService:
    def __init__(self):
        self.repository = CardRepository()

    def list_cards(self, name: Optional[str], types: Optional[str], limit: int, in_stock_only: bool, hyper_rare: bool) -> List[CardSchema]:
        results = self.repository.get_cards(name, types, limit, in_stock_only, hyper_rare)
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
        
    def get_card_by_id(self, card_id: str) -> CardSchema:
        row = self.repository.get_card_by_id(card_id)
        if not row:
            raise ValueError("Card not found")

        return CardSchema(
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


    def update_card(self, card_id: str, update_data: CardUpdateRequest):
        return self.repository.update_card(card_id, update_data.stock, update_data.price)
