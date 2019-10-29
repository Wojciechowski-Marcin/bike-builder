export interface IBikeBuild {
  [key: string]: ISelectedBikePart;
}

interface ISelectedBikePart {
  id: number;
  price: number;
}
