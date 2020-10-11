# Uses python3
import sys

def get_change(money):
  min_coins_number = [0] * (money + 1)
  dominations = [0, 1, 3, 4]

  for m in range(1, money + 1):
    number_of_coin = money
    for c in range(1, len(dominations)):
      if m >= dominations[c]:
        number_of_coin = min(number_of_coin, min_coins_number[m - dominations[c]] + 1)
    min_coins_number[m] = number_of_coin
    print(number_of_coin)
  return min_coins_number[money]


if __name__ == '__main__':
  m = int(sys.stdin.read())
  print(get_change(m))
