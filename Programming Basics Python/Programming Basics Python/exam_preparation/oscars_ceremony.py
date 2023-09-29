hall_rent = int(input())

price_for_statuette = hall_rent * (1 - 0.3)
price_for_catering = price_for_statuette * (1 - 0.15)
price_for_audio = 0.5 * price_for_catering
total_sum = hall_rent + price_for_statuette + price_for_catering + price_for_audio

print(f'{total_sum:.2f}')