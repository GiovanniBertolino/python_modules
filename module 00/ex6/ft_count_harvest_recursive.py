def ft_count_harvest_recursive():
    number_days = int(input("Days until harvest: "))

    def helper(current_day=1):
        if current_day > number_days:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        helper(current_day + 1)

    helper()
