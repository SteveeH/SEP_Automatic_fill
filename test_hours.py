from sep_autofill import hour_float2str, hour_str2float

print("Testing hour_float2str")
print(hour_float2str(8.5), "8:30")
print(hour_float2str(8.75), "8:45")
print(hour_float2str(8.00), "8:00")
print(hour_float2str(16.2), "16:12")


print("Testing hour_str2float")
print(hour_str2float("8:30"), 8.5)
print(hour_str2float("8:45"), 8.75)
print(hour_str2float("8:00"), 8.00)
print(hour_str2float("16:12"), 16.2)
