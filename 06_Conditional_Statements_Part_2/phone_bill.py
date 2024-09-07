base_tariff = 15
call_center_tip = 0.44
TIP = 5
minutes = int(input('Enter minutes: '))
sms = int(input('Enter sms: '))

minutes_price = (minutes - 50) * 0.25 if minutes > 50 else 0
sms_price = (sms - 50) * 0.15 if sms > 50 else 0

total = base_tariff + call_center_tip + minutes_price + sms_price
tip = (total * 0.05)
total = total + tip

if minutes_price or sms_price:
    print('Base:', base_tariff)
    print('Call Center:', call_center_tip)
    print('Minutes:', minutes_price)
    print('Sms:', sms_price)
    print('Tip:', tip)
    print('Total:', total)
else:
    print('Base:', base_tariff)
    print('Call Center:', call_center_tip)
    print('Tip', tip)
    print('Total:', total)