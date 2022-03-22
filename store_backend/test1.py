


def younger_person():
    ages = [12,42,32,50,56,14,78,30,51,89,12,38,67,10]

    solution = ages[0]
    for age in ages:
        if age < solution:
            solution=age
        
    print(solution)

def statistics():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]

    count = 0
    total = 0
    negative = 0
    over_500 = 0
    for num in data:
        count += 1
        total += num

        if num < 0:
            negative = negative + 1

        if(num > 500):
            over_500 += 1


    print(f"2 solutions is {len(data)}")
    print(f"2 solution is: {total}")


def print_some_nums():
    for num in range(1, 11):
        print(num * 10)

    for x in range(10, 110, 10): # range(start, stop, increment)
        print(x)



print("Test test test")
younger_person()
statistics()
print_some_nums()