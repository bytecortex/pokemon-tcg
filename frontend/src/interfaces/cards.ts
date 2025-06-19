export interface CardImage {
  small: string;
  large?: string;
}

export interface Card {
  id: string;
  name: string;
  images: CardImage;
  series: string;
  rarity: string;
  price: number;
}