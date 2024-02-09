def negative_vs_positive(*args):
    negative_nums = []
    positive_nums = []

    for num in args:
        if num < 0:
            negative_nums.append(num)
        else:
            positive_nums.append(num)

    negatives_sum = sum(negative_nums)
    positives_sum = sum(positive_nums)

    print(negatives_sum)
    print(positives_sum)

    if abs(negatives_sum) > positives_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
negative_vs_positive(*numbers)