# -*- coding: UTF-8 -*-

customer = 0
aircon = False

def condition():
    global customer
    global aircon
    if aircon == True:
        print "현재 손님은" + str(customer) + "명입니다. 에어컨은 켜져있습니다\n"
    else:
        print "현재 손님은" + str(customer) + "명입니다. 에어컨은 꺼져있습니다\n"


def customer_in (num_of_customer):
    global customer
    global aircon
    customer += num_of_customer
    if customer >= 4:
        aircon = True
    return condition()

def customer_out (num_of_customer):
    global customer
    global aircon
    customer -= num_of_customer
    if customer == 0:
        aircon = False
    return condition()


for i in range(5):
    customer_in(1)

for i in range(5):
    customer_out(1)