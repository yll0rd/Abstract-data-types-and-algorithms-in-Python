from timeADT import Time


tt = Time(1,11,1)
print(tt)
print(tt.hour())
print(tt.get_minutes())
print(tt.get_seconds())
ta = Time(1,11,5)
print(tt.numSeconds(ta))

tb = Time(14,11,1)
print(tb.isPM())
print(ta.isAM())