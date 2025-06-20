export interface CardImage {
  small: string;
  large?: string;
}

export interface Card {
  id: string;
  supertype: string;
  subtypes: string;
  name: string;
  images: CardImage;
  series: string;
  rarity: string;
  price: number;
  stock: number;
  hp: number;
  types: string;
  flavor_text: string;
}