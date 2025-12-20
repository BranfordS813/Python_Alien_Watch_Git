# to_hexidecimal

def to_hexdecimal(nums):

    """A function that generates a hexidecimal number from regular base 10 numbers based on the 
       hexidecimal system: [1 2 3 4 5 6 7 8 9 A B C D E F 10]
       The fucntion converts numbers 1 - 16 with a match (swtich) case. For numbers larger 
       than 12, the divmod() method is used to extract the quotient and remainder from the number
       whereupon it's converted to hexudecimal form via reducing remainders till the quotient is zero;
       converting remainders to hexidecimal form via the swtich case, and then appending the hexidecimal
       remainders to one single hexidceimal number.
       
       All hexidecimal numbers are output as strings.
    """

    # hexidecimal constant
    HEX_BASE = 16

    ##### determine if the entered number is a single integer #####

    # define a swtich case function for converting singular digits to hexidecimal (should help with converting
    # larger numbers to hexidecimal with preceding hexidecimal values, especilly for X and E.

    def single_hexdecimal(value):
        "Function that converts base 10 numbers into hexidecimal (base-16) numberes as string values"
        match value:
                case 1:
                    hex_1 = "1"
                    value = hex_1
                case 2: 
                    hex_2 = "2"
                    value = hex_2
                case 3: 
                    hex_3 = "3"
                    value = hex_3
                case 4: 
                    hex_4 = "4"
                    value = hex_4
                case 5: 
                    hex_5 = "5"
                    value = hex_5
                case 6: 
                    hex_6 = "6"
                    value = hex_6
                case 7:
                    hex_7 = "7"
                    value = hex_7
                case 8: 
                    hex_8 = "8"
                    value = hex_8
                case 9: 
                    hex_9 = "9"
                    value = hex_9
                case 10:
                    hex_A = "A"
                    value = hex_A
                case 11:
                    hex_B = "B"
                    value = hex_B
                case 12: 
                    hex_C = "C"
                    value = hex_C
                case 13: 
                    hex_D = "D"
                    value = hex_D
                case 14: 
                    hex_E = "E"
                    value = hex_E
                case 15: 
                    hex_F = "F"
                    value = hex_F
                case 16: 
                    hex_10 = "10"
                    value = hex_10
                    
        
        return value

    if type(nums) == int: 
        if nums <= 12:
            nums_hex = single_hexdecimal(nums)
            return nums_hex       
        else: 
        # For hexidecimal numbers larger than 16, the hexidecimal number is formed breaking down 
        # the real number the divmod() method. From there, the quotient is used to 
        # find other quotients and remainders to break down the number until the quotient equates to zero. 
        # from there, the hexidecimal number is construed by reconstructing the remainders to to form the number

            # initialize an empty list for covnerting larger individual numberes into hexidecimal format
            nums_hex_value = []

            # use divmod to find the quotient and remainder of the entered number
            quotient_remainder = divmod(nums, HEX_BASE)
            
            # original quotient and remainder values
            quotient_original = quotient_remainder[0]
            remainder_original = quotient_remainder[1]

            # rename values for the while loop
            quotient = quotient_original
            remainder = remainder_original

            # collect the first remainder before starting the while loop
            init_hex_remainder = single_hexdecimal(remainder)
            nums_hex_value.append(str(init_hex_remainder))

            # construe hexidecimal number as a string using the 'single_hexidecimal' funciton
            while quotient != 0: 

                # refresh quotient and remiander
                quotient_remainder_refresh = divmod(quotient, HEX_BASE)
                quotient = quotient_remainder_refresh[0]
                remainder = quotient_remainder_refresh[1]
                
                # convert refreshed remainder to hexidecimal format
                hex_remainder = single_hexdecimal(remainder)
                # appened refreshed hexidecimal number
                nums_hex_value.append(str(hex_remainder))

            # reverse the order of the list and join it as one string
            nums_hex_value.reverse()

            nums_hex = "".join(nums_hex_value)
            return nums_hex
        
    ##### determine if the entered number is a list of integers (if not a single interger) #####
    if type(nums) == list: 
        nums_iterable = nums

        # initialize an empty list for covnerting larger individual numberes into hexidecimal format
        nums_hex_list = []
        
        for i in list(range(len(nums_iterable))): 

            if nums_iterable[i] in range(0,12):

                nums_single_value = nums_iterable[i]
                nums_hex_list.append(single_hexdecimal(nums_single_value))
            elif nums_iterable[i] not in range(0,12): 

                # initialize empty list for holding values converted to hexidecimal to be appended to 
                # output list
                nums_hex_value =  []
                
                # use divmod to find the quotient and remainder of the entered number
                quotient_remainder = divmod(nums_iterable[i], HEX_BASE)
                
                # original quotient and remainder values
                quotient_original = quotient_remainder[0]
                remainder_original = quotient_remainder[1]

                # rename values for the while loop
                quotient = quotient_original
                remainder = remainder_original

                # collect the first remainder before starting the while loop
                init_hex_remainder = single_hexdecimal(remainder)
                nums_hex_value.append(str(init_hex_remainder))

                # construe hexidecimal number as a string using the 'single_hexidecimal' funciton
                while quotient != 0: 

                    # refresh quotient and remiander
                    quotient_remainder_refresh = divmod(quotient, HEX_BASE)
                    quotient = quotient_remainder_refresh[0]
                    remainder = quotient_remainder_refresh[1]
                    
                    # convert refreshed remainder to hexidecimal format
                    hex_remainder = single_hexdecimal(remainder)
                    # appened refreshed hexidecimal number
                    nums_hex_value.append(str(hex_remainder))

                # reverse the order of the list and join it as one string
                nums_hex_value.reverse()
                nums_hex_iterable = "".join(nums_hex_value)
                
                # append converted hexiceimal value to nums_hex_list
                nums_hex_list.append(nums_hex_iterable)
                    
        return nums_hex_list