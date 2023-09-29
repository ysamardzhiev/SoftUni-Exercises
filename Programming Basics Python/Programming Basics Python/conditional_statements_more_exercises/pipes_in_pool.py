volume_pool = int(input())
debit_first_pipe_per_hour = int(input())
debit_second_pipe_per_hour = int(input())
hours_missing = float(input())

first_pipe_return = hours_missing * debit_first_pipe_per_hour
second_pipe_return = hours_missing * debit_second_pipe_per_hour
total_return = first_pipe_return + second_pipe_return
diff = total_return - volume_pool
total_return_percent = (total_return / volume_pool) * 100
first_pipe_percent = (first_pipe_return / total_return) * 100
second_pipe_percent = (second_pipe_return / total_return) * 100

if total_return > volume_pool:
    print(f"For {hours_missing:.2f} hours the pool overflows with {diff:.2f} liters.")
else:
    print(f"The pool is {total_return_percent:.2f}% full. Pipe 1: {first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%.")