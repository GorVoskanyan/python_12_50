class Time:
    def __init__(self, seconds):
        self.s = seconds
    
    def convert_to_minues(self):
        m, s = divmod(self.s, 60)
        return f"{m}:{s}"

    def convert_to_hours(self):
        m, s = divmod(self.s, 60)
        h, m = divmod(m, 60)
        return f"{h}:{m}:{s}"
        
time = Time(seconds=21365)
# print(time.s)
converted_minutes = time.convert_to_minues()
converted_hours = time.convert_to_hours()

print(converted_minutes)
print(converted_hours)