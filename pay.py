hrs = raw_input("Enter Hours:")
h = float(hrs)
rt=raw_input("Enter rates:")
rates=float(rt)
mt=1.5
if h>40:
    over_time=mt*rates*(h-40)
    gross_pay=over_time + (rates*40)
    print gross_pay
else:
    gross_pay=h*rates
    print gross_pay
