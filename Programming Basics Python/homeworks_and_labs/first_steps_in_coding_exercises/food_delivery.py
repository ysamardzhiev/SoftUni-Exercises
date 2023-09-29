chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_vegetarian_menu = vegetarian_menu * 8.15

total_price_menus = price_fish_menu + price_chicken_menu + price_vegetarian_menu

price_dessert = 20 / 100 * total_price_menus

total_price_overall = total_price_menus + price_dessert + 2.50

print(total_price_overall)