#You work at Len’s Slice, a new pizza joint in the neighborhood.
#You are going to use your knowledge of Python lists to organize 
#some of your sales data.

#creates a list of pizza types
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#creates a list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

#count and print the number of topping options
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
print('\n')

#combine the two lists prices and pizza into one list named pizzas
pizzas = list(zip(prices, toppings))
print(pizzas)
print('\n')

#sort pizzas from lowest to highest price
pizzas.sort()

#find lowest cost pizza
cheapest_pizza = pizzas[0]

#find highest price pizza
priciest_pizza = pizzas[-1]

#find three lowest prices pizza and display it
three_cheapest = pizzas[:3]
print("The three cheapest pizzas are: " + str(three_cheapest) + "\n")

#find out how many occurance of two appears in the prices list
num_two_dollar_slices = prices.count(2)

print("There were " + str(num_two_dollar_slices) + " of the prices of $2")
print('\n')