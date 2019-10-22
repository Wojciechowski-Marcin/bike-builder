export const SELECT_BIKE_TYPE = "SELECT_BIKE_TYPE";

export function selectBikeType(bikeType: string) {
  return {
    type: SELECT_BIKE_TYPE,
    bikeType
  };
}
