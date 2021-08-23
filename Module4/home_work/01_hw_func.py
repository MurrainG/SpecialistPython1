def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    number_of_numbers = len(ticket_number)
    count1 = 0
    sum_beginning = 0
    sum_end = 0
    while number_of_numbers % 2 == 0:
        sum_beginning += int(ticket_number[count1])
        sum_end += int(ticket_number[number_of_numbers - (count1 + 1)])
        count1 += 1
        if count1 == number_of_numbers / 2:
            break
    while number_of_numbers % 2 == 1:
        sum_beginning += int(ticket_number[count1])
        sum_end += int(ticket_number[number_of_numbers - (count1 + 1)])
        count1 += 1
        if count1 == (number_of_numbers - 1) / 2:
            break
    if sum_beginning == sum_end:
        return 'TRUE'
    return 'FALSE'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
