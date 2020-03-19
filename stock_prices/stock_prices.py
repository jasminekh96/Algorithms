#!/usr/bin/python

import argparse

def find_max_profit(prices):
        cost = prices[0]
        profit = prices[1] - cost

        for price in prices[1:]:
            if (price - cost) > profit:
                profit = price - cost
            if price < cost:
                cost = price

        return profit
    # Another way:
    # min_ = 0
    # max_ = len(prices)-1
    # for i in range(len(prices)-1):
    #     if prices[min_] > prices[i]:
    #         min_ = i
    # for i in range(min_+1, len(prices)-1):
    #     if prices[max_] < prices[i]:
    #         max_ = i
    # return prices[max_] - prices[min_]
    #A different attempt that didn't work:
    # min_value = None
    # for value in prices:
    #     if not min_value:
    #         min_value = value
    #     elif value < min_value:
    #         min_value = value
    # max_value = None
    # for value in prices:
    #         if not max_value:
    #             max_value = value
    #         elif value < max_value:
    #             max_value = value
    # return prices[min_value] - prices[max_value]

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))