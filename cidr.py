#!usr/bin/python3

# This is a short program to 'calculate' subnet
# masks from CIDR notation. Operation is pretty
# straightforward, enter a number between 1 and
# 32 and it will return the subnet mask. Typing
# 00 exits the script. 


import os
import time

def clear():
    os.system('clear')

def title():
    clear()
    print('****************************')
    print('* CIDR to Subnet converter *')
    print('*   By P. Gresham          *')
    print('****************************')
    time.sleep(2)
    clear()

def cidr():
    clear()
    
    def subloop():
        print('Enter CIDR notation to return subnet mask\nor 00 to exit')
        return str(input('/'))
    
    def again():
        print('Enter another or 00 to exit')
        return str(input('/')).upper()
        
    n = subloop()
    while n != '00':
        if n == '1':
            print('128.0.0.0')
        elif n == '2':
            print('192.0.0.0')
        elif n == '3':
            print('224.0.0.0')
        elif n == '4':
            print('240.0.0.0')
        elif n == '5':
            print('248.0.0.0')
        elif n == '6':
            print('252.0.0.0')
        elif n == '7':
            print('254.0.0.0')
        elif n == '8':
            print('255.0.0.0')
        elif n == '9':
            print('255.128.0.0')
        elif n == '10':
            print('255.192.0.0')
        elif n == '11':
            print('255.224.0.0')
        elif n == '12':
            print('255.240.0.0')
        elif n == '13':
            print('255.248.0.0')
        elif n == '14':
            print('255.252.0.0')
        elif n == '15':
            print('255.254.0.0')
        elif n == '16':
            print('255.255.0.0')
        elif n == '17':
            print('255.255.128.0')
        elif n == '18':
            print('255.255.192.0')
        elif n == '19':
            print('255.255.224.0')
        elif n == '20':
            print('255.255.240.0')
        elif n == '21':
            print('255.255.248.0')
        elif n == '22':
            print('255.255.252.0')
        elif n == '23':
            print('255.255.254.0')
        elif n == '24':
            print('255.255.255.0')
        elif n == '25':
            print('255.255.255.128')
        elif n == '26':
            print('255.255.255.192')
        elif n == '27':
            print('255.255.255.224')
        elif n == '28':
            print('255.255.255.240')
        elif n == '29':
            print('255.255.255.248')
        elif n == '30':
            print('255.255.255.252')
        elif n == '31':
            print('255.255.255.254')
        elif n == '32':
            print('255.255.255.255\nYou have no addresses left!')
        elif n == '00':
            break
        else:
            clear()
            cidr()    
        if str(input('press any key to go again or 00 to exit ')) == '00':
            break
        else:
            clear()
            n = subloop()



if __name__ == '__main__':
    title()
    cidr()
