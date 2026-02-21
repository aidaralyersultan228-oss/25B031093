# 1 *args
def sum_all(*numbers):
    return sum(numbers)

# 2 **kwargs
def print_info(**data):
    for key, value in data.items():
        print(key, value)

# 3 mixed
def example(a, *args):
    print(a, args)

# 4
def example2(a, **kwargs):
    print(a, kwargs)

# 5 both
def full_example(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)