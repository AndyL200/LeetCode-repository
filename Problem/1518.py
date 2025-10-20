def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    drink = numBottles
    numBottles = 0
    exchange = drink
    while(exchange//numExchange > 0):
        full_bottles = exchange//numExchange
        drink += full_bottles
        exchange = exchange % numExchange
        exchange += full_bottles
    return drink
