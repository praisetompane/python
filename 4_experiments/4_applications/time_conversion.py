"""
implementation: 25 minutes
"""


def convert_from_24_hours(hour_int: int, minutes_int: int):
    def convert_to_pm(hour_in_24_time: int, minutes: int):
        def build_string(minutes, time_difference):
            return f"{time_difference:02d}:{minutes:02d}PM"

        DIFFERENCE = 12

        if hour_int == 12 or hour_int == 24:
            return build_string(DIFFERENCE, minutes)
        else:
            time_difference = hour_in_24_time - DIFFERENCE
            return build_string(minutes, time_difference)

    def convert_to_am(hour_in_24_time: int, minutes: int):
        return f"{hour_in_24_time:02d}:{minutes:02d}AM"

    if hour_int == 12:
        return convert_to_pm(24, minutes_int)
    if hour_int == 24:
        return convert_to_am(12, minutes_int)
    elif hour_int < 12:
        return convert_to_am(hour_int, minutes_int)
    elif hour_int > 12:
        return convert_to_pm(hour_int, minutes_int)


if __name__ == "__main__":
    user_time = input("Please supply time in 24 hour format: ")
    hour, minutes = user_time.split(":")

    hour_int = int(hour)
    minutes_int = int(minutes)

    time_converted = convert_from_24_hours(hour_int, minutes_int)
    print(f"{time_converted = }")
