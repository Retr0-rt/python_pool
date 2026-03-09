def show_day(day: int, total_days: int) -> None:
    if day > total_days:
        print("Harvest time!")
        return
    print(f"Day {day}")
    show_day(day + 1, total_days)


def ft_count_harvest_recursive() -> None:
    total_d = int(input("Days until harvest: "))
    show_day(1, total_d)
