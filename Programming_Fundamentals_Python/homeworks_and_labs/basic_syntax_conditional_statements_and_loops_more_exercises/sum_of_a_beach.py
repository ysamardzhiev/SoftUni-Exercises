word = input().lower()

beach_sum = 0

beach_sum += word.count('sand') + word.count('water') + word.count('fish') + word.count('sun')
print(beach_sum)