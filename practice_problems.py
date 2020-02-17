#!/usr/bin/python3

import random

"""Class for representing IP addresses"""
class ip_address:
    def __init__(self,first,second,third,fourth,subnet,hostspace,network_address,top_range):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.subnet = subnet
        self.hostspace = hostspace
        self.network_address = network_address
        self.top_range = top_range

    """Method returns string representation of IP address"""
    def create_address(self):
        return(str(self.first) + "." + str(self.second) + "." + str(self.third) + "." + str(self.fourth) + "/" + str(self.subnet))

"""Generates random subnet"""
def generate_subnet():
    potential_subnets = [8,16,24]
    randNum = random.randint(0,2)
    subnet = potential_subnets[randNum]
    return subnet

"""Generates hostspace based on subnet input"""
def generate_hostspace(subnet):
    host_bits = 32 - subnet
    hostspace = 2**host_bits
    return hostspace

"""Generates random IP address and creates IP object"""
def generate_address():
    first = random.randint(0,255)
    second = random.randint(0,255)
    third = random.randint(0,255)
    fourth = random.randint(0,255)
    subnet = generate_subnet()
    hostspace = generate_hostspace(subnet)
    address = ip_address(first,second,third,fourth,subnet,hostspace,"","")
    network_address = generate_network_address(address)
    address.network_address = network_address
    address_toprange = generate_address_toprange(address)
    address.top_range = address_toprange
    return address

"""Generates network address based on IP address object input"""
def generate_network_address(address):
    if address.subnet == 24:
        return str(address.first) + "." + str(address.second) + "." + str(address.third) + ".0/" + str(address.subnet)
    elif address.subnet == 16:
        return str(address.first) + "." + str(address.second) + ".0.0/" + str(address.subnet)
    else:
        return str(address.first) + ".0.0.0/" + str(address.subnet)

"""Generates top range IP address based on IP address object input"""
def generate_address_toprange(address):
    if address.subnet == 24:
        return str(address.first) + "." + str(address.second) + "." + str(address.third) + ".255/" + str(address.subnet)
    elif address.subnet == 16:
        return str(address.first) + "." + str(address.second) + ".255.255/" + str(address.subnet)
    else:
        return str(address.first) + ".255.255.255/" + str(address.subnet)

"""Checks if address1 < address2. Inputs are string representations of IP addresses"""
def is_less_than(address1,address2):

    address1 = address1.split("/")
    address1 = address1[0].split(".")
    address2 = address2.split("/")
    address2 = address2[0].split(".")

    for i in range(0,4):
        if int(address1[i]) > int(address2[i]):
            return False
    return True

"""Determines if address1 is subnet of address2. Inputs are IP objects. Network address of IP objects are used to determine subnet"""
def is_subnet(address1,address2):
    address1_network = address1.network_address
    address1_top = address1.top_range

    address2_network = address2.network_address
    address2_top = address2.top_range
    return is_less_than(address2_network,address1_network) and is_less_than(address1_top, address2_top)

"""Question 1"""
def subnet_size_question(hostspace,subnet):
    answer = input("\nWhat size subnet can accomodate up to " + str(hostspace) + " hosts? \nAnser: /")

    try:
        if int(answer) == subnet:
            print("Correct. The answer is /" + str(answer) + ".\n")
        else:
            print("Incorrect answer. The correct answer is /" + str(subnet) + ".\n")
    except:
        print("Error: Answer must be an integer. The correct answer is /" + str(subnet) + ".\n")

"""Question 2"""
def network_address_question(address):
    answer = input("\nWhat is the network address if a host's IP address is " + address.create_address() + "? \nAnswer: ")

    if answer == address.network_address:
        print("Correct. The network address is " + answer + ".\n")
    else:
        print("Incorrect. The network address is "+ address.network_address + ".\n")

"""Question 3"""
def address_range_question(address):
    answer = input("\nWhat is the range of addresses in the subnet " + address.network_address + "? (Note: please format answer '0.0.0.0 - 0.0.0.0')\nAnswer: ")
    answer = answer.split(" - ")
    if len(answer) != 2:
        print("Error. Incorrectly formatted answer. The range is " + address.network_address.split("/")[0] + " - " + address.top_range.split("/")[0] + ".\n")
        return

    if answer[0] == address.network_address.split("/")[0] and answer[1] == address.top_range.split("/")[0]:
        print("Correct. The range is " + address.network_address.split("/")[0] + " - " + address.top_range.split("/")[0] + ".\n")
    else:
        print("Incorrect. The range is " + address.network_address.split("/")[0] + " - " + address.top_range.split("/")[0] + ".\n")

"""Question 4"""
def subnet_question(address1,address2):
    answer = input("\nIs " + address1.network_address + " a subnet of " + address2.network_address + "? (Answer either 'y' or 'n')\nAnswer: ")

    if is_subnet(address1,address2):
        if answer == "y":
            print("Correct. " + address1.network_address + " is a subnet of " + address2.network_address + ".\n")
        elif answer == "n":
            print("Incorrect. " + address1.network_address + " is a subnet of " + address2.network_address + ".\n")
        else:
            print("Error: Incorrectly formatted answer. " + address1.network_address + " is a subnet of " + address2.network_address + ".\n")
    else:
        if answer == "y":
            print("Incorrect. " + address1.network_address + " is not a subnet of " + address2.network_address + ".\n")
        elif answer == "n":
            print("Correct. " + address1.network_address + " is not a subnet of " + address2.network_address + ".\n")
        else:
            print("Error: Incorrectly formatted answer. " + address1.network_address + " is not a subnet of " + address2.network_address + ".\n")

def main():

    done_asking_questions = False

    while not done_asking_questions:
        address1 = generate_address()
        randomNum = random.randint(1,4)

        if randomNum == 1:
            subnet_size_question(address1.hostspace,address1.subnet)
        elif randomNum == 2:
            network_address_question(address1)
        elif randomNum == 3:
            address_range_question(address1)
        else:
            done = False
            while not done:
                address2 = generate_address()
                if address1.first == address2.first:
                    done = True
            subnet_question(address1,address2)

        good_input = False
        while not good_input:
            answer = input("Would you like another practice problem? ('y' or 'n'): ")

            if answer == "y":
                good_input = True
            elif answer == 'n':
                good_input = True
                done_asking_questions = True
            else:
                print("Error: Please answer 'y' or 'n'.")


if __name__ == '__main__':
    main()
