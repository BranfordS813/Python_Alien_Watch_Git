# to_duodecimal.py

def to_duodecimal(nums):

    """A function that generates a duodemical number from regular base 10 numbers based on the 
       duodecimal system: [1 2 3 4 5 6 7 8 9 X E 10]
       The fucntion converts numbers 1 - 12 with a match (swtich) case. For numbers larger 
       than 12, the divmod() method is used to extract the quotient and remainder from the number
       whereupon it's converted to duodecimal form via reducing remainders till the quotient is zero;
       converting remainders to duodecimal form via the swtich case, and then appending the duodecimal
       remainders to one single duodceimal number.
       
       All duodecimal numbers are output as strings.
    """

    # duodecimal constant
    DUO_BASE = 12

    ##### determine if the entered number is a single integer #####

    # define a swtich case function for converting singular digits to duodecimal (should help with converting
    # larger numbers to duodecimal with preceding duodecimal values, especilly for X and E.

    def single_duodecimal(value):
        "Function that converts base 10 numbers into duodecimal (base-12) numberes as string values"
        match value:
                case 1:
                    duo_1 = "1"
                    value = duo_1
                case 2: 
                    duo_2 = "2"
                    value = duo_2
                case 3: 
                    duo_3 = "3"
                    value = duo_3
                case 4: 
                    duo_4 = "4"
                    value = duo_4
                case 5: 
                    duo_5 = "5"
                    value = duo_5
                case 6: 
                    duo_6 = "6"
                    value = duo_6
                case 7:
                    duo_7 = "7"
                    value = duo_7
                case 8: 
                    duo_8 = "8"
                    value = duo_8
                case 9: 
                    duo_9 = "9"
                    value = duo_9
                case 10:
                    duo_X = "X"
                    value = duo_X
                case 11:
                    duo_E = "E"
                    value = duo_E
                case 12: 
                    duo_12 = "10"
                    value = duo_12
        
        return value

    if type(nums) == int: 
        if nums <= 12:
            nums_duo = single_duodecimal(nums)
            return nums_duo       
        else: 
        # For duodecimal numbers larger than 12, the duodecimal number is formed breaking down 
        # the real number with the divmod() method. From there, the quotient is used to 
        # find other quotients and remainders to break down the number until the quotient equates to zero. 
        # from there, the duodecimal number is construed by reconstructing the remainders to to form the number

            # initialize an empty list for covnerting larger individual numberes into duodecimal format
            nums_duo_value = []

            # use divmod to find the quotient and remainder of the entered number
            quotient_remainder = divmod(nums, DUO_BASE)
            
            # original quotient and remainder values
            quotient_original = quotient_remainder[0]
            remainder_original = quotient_remainder[1]

            # rename values for the while loop
            quotient = quotient_original
            remainder = remainder_original

            # collect the first remainder before starting the while loop
            init_duo_remainder = single_duodecimal(remainder)
            nums_duo_value.append(str(init_duo_remainder))

            # construe duodecimal number as a string using the 'single_duodecimal' funciton
            while quotient != 0: 

                # refresh quotient and remiander
                quotient_remainder_refresh = divmod(quotient, DUO_BASE)
                quotient = quotient_remainder_refresh[0]
                remainder = quotient_remainder_refresh[1]
                
                # convert refreshed remainder to duoddecimal format
                duo_remainder = single_duodecimal(remainder)
                # appened refreshed duodecimal number
                nums_duo_value.append(str(duo_remainder))

            # reverse the order of the list and join it as one string
            nums_duo_value.reverse()

            nums_duo = "".join(nums_duo_value)
            return nums_duo
        
    ##### determine if the entered number is a list of integers (if not a single interger) #####
    if type(nums) == list: 
        nums_iterable = nums

        # initialize an empty list for covnerting larger individual numberes into duodecimal format
        nums_duo_list = []
        
        for i in list(range(len(nums_iterable))): 

            if nums_iterable[i] in range(0,12):

                nums_single_value = nums_iterable[i]
                nums_duo_list.append(single_duodecimal(nums_single_value))
            elif nums_iterable[i] not in range(0,12): 

                # initialize empty list for holding values converted to duodecimal to be appended to 
                # output list
                nums_duo_value =  []
                
                # use divmod to find the quotient and remainder of the entered number
                quotient_remainder = divmod(nums_iterable[i], DUO_BASE)
                
                # original quotient and remainder values
                quotient_original = quotient_remainder[0]
                remainder_original = quotient_remainder[1]

                # rename values for the while loop
                quotient = quotient_original
                remainder = remainder_original

                # collect the first remainder before starting the while loop
                init_duo_remainder = single_duodecimal(remainder)
                nums_duo_value.append(str(init_duo_remainder))

                # construe duodecimal number as a string using the 'single_duodecimal' funciton
                while quotient != 0: 

                    # refresh quotient and remiander
                    quotient_remainder_refresh = divmod(quotient, DUO_BASE)
                    quotient = quotient_remainder_refresh[0]
                    remainder = quotient_remainder_refresh[1]
                    
                    # convert refreshed remainder to duoddecimal format
                    duo_remainder = single_duodecimal(remainder)
                    # appened refreshed duodecimal number
                    nums_duo_value.append(str(duo_remainder))

                # reverse the order of the list and join it as one string
                nums_duo_value.reverse()
                nums_duo_iterable = "".join(nums_duo_value)
                
                # append converted duodceimal value to nums_duo_list
                nums_duo_list.append(nums_duo_iterable)
                    
        return nums_duo_list