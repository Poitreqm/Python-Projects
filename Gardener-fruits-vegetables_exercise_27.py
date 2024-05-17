#
# Садовник продает урожай своего сада на овощной бирже.
# Продает овощи по цене N левов за килограмм и фрукты по цене M левов за килограмм.
# Напишите программу, которая будет подсчитывать доход от урожая в евро (при условии, что один евро равен 1.95 лв.).
#

price_vegetables = 1.63  # Цена за килограм
price_fruits = 2.03  # Цена за килограм

kg_vegetables = 10  # кг
kg_fruits = 10  # кг

income_vegetables = price_vegetables * kg_vegetables
income_fruits = price_fruits * kg_fruits


converter = 0.51  # 1 лев равен 0.51 евро или 1 евро равен 1.95

total = (income_vegetables * converter) + (income_vegetables * converter)

print(f"Total income: {total} euro")
