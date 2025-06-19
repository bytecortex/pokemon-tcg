export interface CardImage {
  small: string;
  large?: string;
}

export interface CardSet {
  id: string;
  name: string;
}

export interface Card {
  id: string;
  name: string;
  images: CardImage;
  set: CardSet;
}