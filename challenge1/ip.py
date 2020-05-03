import ipaddress


def check_ip(ip):
    try:
        if ipaddress.ip_address(ip):
            return f"{ip} is a Valid IP Address"
        else:
            return f"{ip} is not a Valid IP Address"
    except ValueError as e:
        # print(e)
        return f"{ip} is not a Valid IP Address"


if __name__ == '__main__':
    print('Check for a valid IP Address')

    while True:
        ip_address = input('Enter IP Address (Type x to End): ')
        if ip_address == 'x' or ip_address == 'X':
            break
        else:
            print(check_ip(ip_address))

