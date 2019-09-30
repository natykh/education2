# короч ти пишеш касовий апарат.
# приходить клієнт з певною кількістю готівки і набором товарів.
# в магазині працює скиндка - перші три товари оплачуєш повністю, а решту зі скидкою в 30%
# визнач, чи вистачить покупцю грошей.
# якщо так - напиши скільки коштувати вся покупка. якщо ні - напиши скільки не вистачає клієнту


initial_cash = 100                     # це скільки грошей у покупця
prices = [10, 22, 14.5, 80, 4, 9, 33]   # це вартість кожного товару

# solution goes here

# SOLUTION  #1
#
# position = 0
# remained_cash = initial_cash
# for price in prices:
#     position = position + 1
#     if position <= 3:
#         remained_cash = remained_cash - price
#     else:
#         discount_price = 0.7 * price
#         remained_cash = remained_cash - discount_price

# SOLUTION #2
#
# remained_cash = initial_cash
# if len(prices) > 3:
#     remained_cash = remained_cash - prices[0] - prices[1] - prices[2]
#     for i in range(3, len(prices)):
#         remained_cash = remained_cash - 0.7 * prices[i]
# else:
#     remained_cash = remained_cash - prices[0] - prices[1] - prices[2]


# SOLUTION #3
#
# remained_cash = initial_cash
# for i in range(3):
#     remained_cash = remained_cash - prices[i]
# for i in range(3, len(prices)):
#     remained_cash = remained_cash - 0.7* prices[i]

if remained_cash >= 0:
    print("You have enough money. Your purchase will cost you " + str(initial_cash - remained_cash) + " dollars")
else:
    print("You don't have enough money. You need " + str(-1 * remained_cash) + " more dollars")
