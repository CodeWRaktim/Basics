class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def __sub__(self, other):
        total_minutes1 = self.hours * 60 + self.minutes
        total_minutes2 = other.hours * 60 + other.minutes
        total_minutes = total_minutes1 - total_minutes2
        total_hours = total_minutes // 60
        total_minutes = total_minutes % 60
        return Time(total_hours, total_minutes)

    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes"

# Example usage
time1 = Time(2, 45)
time2 = Time(1, 30)

print("Time 1:", time1)
print("Time 2:", time2)

time_sum = time1 + time2
print("Sum of Time 1 and Time 2:", time_sum)

time_diff = time1 - time2
print("Difference of Time 1 and Time 2:", time_diff)