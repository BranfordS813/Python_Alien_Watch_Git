# alientime.py

"""A class module that creates instances and handles displays of fictional chronological time keeping
   systems found on alien planets. As such, they parameters can be entered for varying lengths
   of time ranging in: seconds, minutes, hours, days, weeks, months, years, in addition to meridian 
   time periods. also, the time can be expressed in duodecimal or hexidecimal format. Time can be output
   as either a digital display or as an analog display.
"""

# Imports
import time
import math

# Import rich library to assist with multi-line string update
from rich.live import Live 
from rich.console import Console
from rich.text import Text

# Import turtle for analog display
import turtle
import time
import datetime # Using datetime for more robust time management

# Import custom to_duodecimal funciton that converts base-10 numbers to base-12 duodecimal format
from to_duodecimal import to_duodecimal
# Improt custom to_hexdecimal fucntion that converts base-10 numbers to base-16 hexidecimal format
from to_hexdecimal import to_hexdecimal

class AlienTime(): 
    """A class that models and displays different alien time systems."""

    def __init__(self, planet_name, time_constants, date_constants, meridian_segment, day_names, month_names, meridian, seasons='', base=10, canon_year=2000, tick_interval=''):
        """Initialize attributes for class arguments. Note that the arguments are dictionaries, save
           for meridian. 
        """

        self.planet_name = planet_name
        self.time_constants = time_constants
        self.date_constants = date_constants
        self.meridian_segment = meridian_segment
        self.day_names = day_names
        self.month_names = month_names
        self.meridian = meridian
        self.seasons = seasons
        self.base = base
        self.tick_interval = tick_interval
        self.canon_year = canon_year

        # # Previous init defs 
        #self.month_days = month_days
        #self.analog_time = analog_time
        #self.military_time = military_time
        #self.seconds = seconds
        #self.minutes = minutes
    
    def digital_disp(self): 
        """Run an analog display of the alien time system"""

        ##### Set Constants and Dictionaries #####

        # Set constants for time based on dictionary
        SECONDS_PER_MINUTE = self.time_constants["Seconds Per Minute"]
        MINUTES_PER_HOUR = self.time_constants["Minutes Per Hour"]
        HOURS_PER_DAY = self.time_constants["Hours Per Day"]

        # Set constants for date based on dictionary
        DAYS_PER_WEEK = self.date_constants["Days Per Week"]
        WEEKS_PER_MONTH = self.date_constants["Weeks Per Month"]
        MONTHS_PER_YEAR = self.date_constants["Months Per Year"]
        DAYS_PER_SEASON = self.date_constants["Days Per Season"]
        DAYS_PER_MONTH = self.date_constants["Days Per Month"]

        # set tick interval
        TICK_INTERVAL = self.tick_interval

        # set canon year
        CANON_YEAR = self.canon_year 

        # set meridian segment 
        MERIDIAN_SEGMENT = self.meridian_segment

        # set day names
        DAY_NAMES = self.day_names

        # Set month names 
        MONTH_NAMES = self.month_names
        
        # Set meridian dictionary
        MERIDIAN = self.meridian 

        # Set Seasons
        SEASONS = self.seasons

        # Set base system (default is 10)  
        BASE = self.base

        # set planet name 
        PLANET_NAME = self.planet_name

        ##### Initialize elapsed time variables 

        # Initialize time elapsed
        total_seconds_elapsed = 0
        total_minutes_elapsed = 0 
        total_hours_elapsed = 0
        total_days_elapsed = 0 
        total_weeks_elapsed = 0
        total_months_elapsed = 0
        total_years_elapsed = 0
        total_seasons_elapsed = 0

        # Initialize canon year
        canon_year = CANON_YEAR 

        # import time.monotonic() and time.time() to run the clock.
        # time.monotonic() is used to measure time intervals

        start_time = time.monotonic()

        # Create a Console instance for the multi-line print for the analog clock
        console = Console()
        try: 
                # Use the Live context manager to handle the continuous updating
                # Put it inside the try-except block to account for error handling
                # after clock interruption.
                with Live(console=console, screen=True) as live:

                    # Initiate the display    
                    input("Press Any key to start")

                    while True:

                        # 2. Calculate the exact time this tick should finish
                        # The next tick should be at the start_time + (total_seconds_elapsed + 1) * TICK_INTERVAL
                        target_time = start_time + (total_seconds_elapsed + 1) * TICK_INTERVAL

                        # 3. Calculate how long we still need to sleep
                        time_to_sleep = target_time - time.monotonic()
                        
                        # 4. Only sleep if the target time hasn't passed (it shouldn't)
                        if time_to_sleep > 0:
                            time.sleep(time_to_sleep)

                            # keep this line of code inside the if block if you want more precision; 
                            # keep it the line of code outside the if block if you want the clock to run
                            # despite system lag; in other words, if you want the clock to run despite the 
                            # the computer being slow (or for game/simulation time) keep the line
                            # outside of the if block

                        # Seconds advanced ONLY after the sleep completes
                        total_seconds_elapsed += 1
                        
                        # Minute Logic
                        if total_seconds_elapsed > 0 and (total_seconds_elapsed % SECONDS_PER_MINUTE) == 0:
                            total_minutes_elapsed += 1
                            
                            # Hour Logic
                            if total_minutes_elapsed > 0 and (total_minutes_elapsed % MINUTES_PER_HOUR) == 0:
                                total_hours_elapsed += 1
                                
                                # Days Logic
                                if total_hours_elapsed > 0 and (total_hours_elapsed % HOURS_PER_DAY) == 0:
                                    total_days_elapsed += 1

                                    # Weeks Logic
                                    if total_days_elapsed > 0 and (total_days_elapsed % DAYS_PER_WEEK) == 0:
                                        total_weeks_elapsed += 1

                                        # Months Logic 
                                        if total_weeks_elapsed > 0 and (total_weeks_elapsed % WEEKS_PER_MONTH) == 0:
                                            total_months_elapsed += 1

                                            # Years Logic 
                                            if total_months_elapsed > 0 and (total_months_elapsed % MONTHS_PER_YEAR) == 0:
                                                total_years_elapsed += 1
                                                # Current Year
                                                canon_year += 1

                                    # Seasons Logic
                                    if total_days_elapsed > 0 and (total_days_elapsed % DAYS_PER_SEASON) == 0:
                                        total_seasons_elapsed += 1

                                            
                        
                        # Time Rollovers --> display if no duo/hex conversion is used
                        second = total_seconds_elapsed % SECONDS_PER_MINUTE
                        hour_military = total_hours_elapsed % HOURS_PER_DAY
                        # for hour_meridian rollover, increase the index display from 0
                        # to 1: first hour to the specified MERIDIAN SEGMENT
                        hour_meridian_raw = total_hours_elapsed % MERIDIAN_SEGMENT
                        hour_meridian = hour_meridian_raw + 1
                        minute = total_minutes_elapsed % MINUTES_PER_HOUR
                        # apply same index increase method to days, weeks, and months.
                        days_raw = total_days_elapsed % DAYS_PER_WEEK
                        days = days_raw + 1
                        weeks_raw = total_weeks_elapsed % WEEKS_PER_MONTH
                        weeks = weeks_raw + 1
                        months_raw = total_months_elapsed % MONTHS_PER_YEAR
                        months = months_raw + 1
                        seasons = total_seasons_elapsed % DAYS_PER_SEASON
                
                        # Rollover for the day of the month (previous version)
                        day_of_month = total_days_elapsed % DAYS_PER_MONTH
                        
                        # --- MAPPING MODULO RESULTS TO NAMES ---
                        # Use get() method: https://www.w3schools.com/python/ref_dictionary_get.asp
                        # Use the dictionary to map the modulo result to the name.
                        # If the result is 0, the dictionary correctly maps it to the last item.
                        # rollback the days and months by -1 to get the correct month and day names (0th Index)
                        days_name_disp = DAY_NAMES.get(days-1) # Omit "N/A" to avoid math domain errors
                        months_name_disp = MONTH_NAMES.get(months-1)

                        # to find the correct suffix for the day of the month, the last digits
                        # of the days needs to be found. In general, numbers ending in the th suffix are:
                        # 11, 12, 13, 0, 4-9; numbes ending in the 1st suffix are 1 (but not 11) 
                        # numbes ending in the nd suffix are 2 (but not 12), and numbers ending in the 3rd
                        # suffix are 3 (but not 13) for this, the modulo operator can be used with 10: %10
                        # to find the last digits for an integer with two numbers. But, if the integer is larger
                        # than two numbers, then a modulo operator with 100: %100 needs to be used to find two digit
                        # ending numbers. For example 43 % 10 = 3, hence 43rd; but 1313%10 = 3; so it needs to be 
                        # expressed as 1313%100 = 13, hence 1313th. the same logic follows for larger numbes than three or
                        # four integers: 1313131313%100 = 13. %10 also holds up for three integer numbers: 
                        # 113%10 = 13; 104%10 = 4. A switch statement should suffice with conditionals 
                        
                        # # Results in Error ❌
                        # # find the number of integers within the day number. This will be done with using the 
                        # # logarthim with base 10, imported from the math module
                        # day_len = math.floor(math.log10(days))+1

                        # Find appropriate last integer digit numbers str() and len() methods

                        def day_suf_len(day_input):
                            day_string = str(day_input)
                            day_len = len(day_string)

                            if day_len == 1 or day_len == 2:
                                day_suffix = days % 10
                                return day_suffix
                            else:
                                day_suffix2 = days % 100
                                if day_suffix2 !=11 or day_suffix2 !=12 or day_suffix != 13:
                                    day_suffix = days % 10
                                    return day_suffix
                                else:
                                    day_suffix = day_suffix2
                                    return day_suffix

                        # define a switch (match) case that handles adding suffix strings to the end of days

                        def suffix(day_post_len):
                            """function that serves as a match case (switch statement) for assiging a suffix string
                               to a number
                            """
                            match day_post_len: 
                                case 0 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13: 
                                    suffix = "th"
                                    return suffix 
                                case 1:
                                    suffix = "st"
                                    return suffix
                                case 2: 
                                    suffix = "nd"
                                    return suffix
                                case 3: 
                                    suffix = "rd"
                                    return suffix
                        
                        # create a variable to insert in custom suffix method that gives the approprite suffix string for the last integer(s) digits
                        days_post_suf_len = day_suf_len(days)
                        day_suffix_assigned = str(suffix(days_post_suf_len)) 

                        # For proper digital display without the brakets jumping from single to multiple digits of 
                        # an integer, use the zfill() method to pad out the numbers: 01, 02, 03 ... 10, etc.
                        # but for this, the appropriate length of the digit must be found, especially for scalable
                        # alien planet time systems with seconds, hours, and minutes in the three+ digit range. The 
                        # width (zlen(width)) will be found with the str() and len() methods

                        def z_width(time_unit_input):
                            width_str = len(str(time_unit_input))
                            # return width_str as type int
                            width_int = int(width_str)
                            return width_int
                        

                        # Apply z_width definition to seconds, minutes, hours (military and meridian) 
                        # and months ... you know what, everything + months and weeks (save for days)
                        # just for the sake of scalability
                        seconds_width = z_width(SECONDS_PER_MINUTE)
                        minutes_width = z_width(MINUTES_PER_HOUR)
                        hour_military_width = z_width(HOURS_PER_DAY)
                        hour_meridian_width = z_width(MERIDIAN_SEGMENT)
                        weeks_width = z_width(WEEKS_PER_MONTH)
                        months_width = z_width(MONTHS_PER_YEAR)

                        # Apply z_widths to seconds, minutes, hours, etc, for BASE-12 
                        seconds_width_duo = len(str(to_duodecimal(SECONDS_PER_MINUTE-1)))
                        minutes_width_duo = len(str(to_duodecimal(MINUTES_PER_HOUR-1)))
                        hours_military_width_duo = len(str(to_duodecimal(HOURS_PER_DAY-1)))
                        hours_meridian_width_duo = len(str(to_duodecimal(MERIDIAN_SEGMENT)))
                        weeks_width_duo = len(str(to_duodecimal(WEEKS_PER_MONTH-1)))
                        months_width_duo = len(str(to_duodecimal(MONTHS_PER_YEAR-1)))

                        # Apply z_wdith tos econds, minutes, hours, ect, for BASE-16    
                        seconds_width_hex = len(str(to_hexdecimal(SECONDS_PER_MINUTE-1)))
                        minutes_width_hex = len(str(to_hexdecimal(MINUTES_PER_HOUR-1)))
                        hours_military_width_hex = len(str(to_hexdecimal(HOURS_PER_DAY-1)))
                        hours_meridian_width_hex = len(str(to_hexdecimal(MERIDIAN_SEGMENT)))
                        weeks_width_hex = len(str(to_hexdecimal(WEEKS_PER_MONTH-1)))
                        months_width_hex = len(str(to_hexdecimal(MONTHS_PER_YEAR-1)))

                        # Apply z fix before conversion(?)

                        if BASE == 12: 
                            # convert time to duodecimal
                            seconds_disp = str(to_duodecimal(second)).zfill(seconds_width_duo) 
                            minutes_disp = str(to_duodecimal(minute)).zfill(minutes_width_duo)
                            hours_military_disp = str(to_duodecimal(hour_military)).zfill(hours_military_width_duo)
                            hours_meridian_disp = str(to_duodecimal(hour_meridian)).zfill(hours_meridian_width_duo)
                            days_disp = str(to_duodecimal(days)) + day_suffix_assigned
                            weeks_disp = str(to_duodecimal(weeks)).zfill(weeks_width_duo)
                            months_disp = str(to_duodecimal(months)).zfill(months_width_duo)
                            seasons_disp = str(to_duodecimal(seasons))
                        elif BASE == 16:
                            # convert time to hexidecimal
                            seconds_disp = str(to_hexdecimal(second)).zfill(seconds_width_hex)
                            minutes_disp = str(to_hexdecimal(minute)).zfill(minutes_width_hex)
                            hours_military_disp = str(to_hexdecimal(hour_military)).zfill(hours_military_width_hex)
                            hours_meridian_disp = str(to_hexdecimal(hour_meridian)).zfill(hours_meridian_width_hex)
                            days_disp = str(to_hexdecimal(days)) + day_suffix_assigned
                            weeks_disp = str(to_hexdecimal(weeks)).zfill(weeks_width_hex)
                            months_disp = str(to_hexdecimal(months)).zfill(months_width_hex)
                            seasons_disp = str(to_hexdecimal(seasons))
                        else: 
                            # default digital time display for base-10
                            seconds_disp = str(second).zfill(seconds_width)
                            minutes_disp = str(minute).zfill(minutes_width)
                            hours_military_disp = str(hour_military).zfill(hour_military_width)
                            hours_meridian_disp = str(hour_meridian).zfill(hour_meridian_width)
                            days_disp  = str(days) + day_suffix_assigned
                            weeks_disp = str(weeks).zfill(weeks_width)
                            months_disp = str(months).zfill(months_width)
                            seasons_disp = str(seasons) 


                       
                        # Denote Meridan with a for loop
                        # initialize Meridian Display 
                        Meridian_disp = "N/A"
                        for m, interval in MERIDIAN.items():
                            if hour_military in interval:
                                Meridian_disp = m

                        # Logic for displaying current season (using the corrected 0/rollover logic)
                        # The total days elapsed divided by days per season gives us the current season index

                        if SEASONS:
                        # Use the modulo result ex: (0-3) to index the season_names list
                            season = SEASONS[seasons % len(SEASONS)]
                        else:
                            season = "N/A"
                        
                            
                        # 4. RICH DISPLAY UPDATE
                        # we'll omit  | Total Seconds: {total_seconds_elapsed:,}
                        # for now ...
                    
                        output_block = Text.from_markup(f"""
                        [bold yellow]Current Time on {PLANET_NAME}: ({TICK_INTERVAL:.05f}s/tick)[/bold yellow]
                        [bold orange]Military Time[/bold orange]
                        | [grey]H[/grey]: {hours_military_disp} | [grey]M[/grey]: {minutes_disp} | [grey]S[/grey]: {seconds_disp} |
                        [bold purple]{MERIDIAN_SEGMENT} Hour Time[/bold purple]
                        | [green]H[/green]: {hours_meridian_disp} | [green]M[/green]: {minutes_disp} | [green]S[/green]: {seconds_disp} | {Meridian_disp} |
                        [bold red]Date[/bold red]
                        | Day: {days_name_disp}, {days_disp} | Month {months_disp}: {months_name_disp} | Week: {weeks_disp} |
                        [bold blue]SEASON[/bold blue]: [bold magenta]{season}[/bold magenta] | [bold cyan]YEAR[/bold cyan]: [bold white]{canon_year:04d}[/bold white]

                        [bold yellow]-- TOTAL ELAPSED --[/bold yellow]
                        | Total Days: {total_days_elapsed:,}
                        | Total Weeks: {total_weeks_elapsed:,}
                        | Total Months: {total_months_elapsed:,}
                        | Total Seasons: {total_seasons_elapsed:,}
                        | Total Years: {total_years_elapsed:,}
                        """)

                        # 2. Update the live display content
                        # Rich handles the cursor movement and overwriting automatically!
                        live.update(output_block)

        except (KeyboardInterrupt, RecursionError):
                print("\nClock stopped by user interruption.")

                    
    def analog_disp(self):

        """Run an analog display of the alien time system"""

        ##### Set Constants and Dictionaries #####
        """Portion copied from digital_disp() function definition."""

        # Set constants for time based on dictionary
        SECONDS_PER_MINUTE = self.time_constants["Seconds Per Minute"]
        MINUTES_PER_HOUR = self.time_constants["Minutes Per Hour"]
        HOURS_PER_DAY = self.time_constants["Hours Per Day"]

        # Set constants for date based on dictionary
        DAYS_PER_WEEK = self.date_constants["Days Per Week"]
        WEEKS_PER_MONTH = self.date_constants["Weeks Per Month"]
        MONTHS_PER_YEAR = self.date_constants["Months Per Year"]
        DAYS_PER_SEASON = self.date_constants["Days Per Season"]
        DAYS_PER_MONTH = self.date_constants["Days Per Month"]

        # set tick interval
        TICK_INTERVAL = self.tick_interval

        # set canon year
        CANON_YEAR = self.canon_year 

        # set meridian segment 
        MERIDIAN_SEGMENT = self.meridian_segment

        # set day names
        DAY_NAMES = self.day_names

        # Set month names 
        MONTH_NAMES = self.month_names
            
        # Set meridian dictionary
        MERIDIAN = self.meridian 

        # Set Seasons
        SEASONS = self.seasons

        # Set base system (default is 10)  
        BASE = self.base

        # set planet name 
        PLANET_NAME = self.planet_name

        ##### Initialize elapsed time variables 

        # Initialize time elapsed
        total_seconds_elapsed = 0
        total_minutes_elapsed = 0 
        total_hours_elapsed = 0
        total_days_elapsed = 0 
        total_weeks_elapsed = 0
        total_months_elapsed = 0
        total_years_elapsed = 0
        total_seasons_elapsed = 0

        # Initialize canon year
        canon_year = CANON_YEAR 

        # import time.monotonic() and time.time() to run the clock.
        # time.monotonic() is used to measure time intervals

        start_time = time.monotonic()

        # 2. Calculate the exact time this tick should finish

        # The next tick should be at the start_time + (total_seconds_elapsed + 1) * TICK_INTERVAL
        target_time = start_time + (total_seconds_elapsed + 1) * TICK_INTERVAL

        # 3. Calculate how long we still need to sleep
        time_to_sleep = target_time - time.monotonic()
                            
        # 4. Only sleep if the target time hasn't passed (it shouldn't)
        if time_to_sleep > 0:
            time.sleep(time_to_sleep)

            # keep this line of code inside the if block if you want more precision; 
            # keep it the line of code outside the if block if you want the clock to run
            # despite system lag; in other words, if you want the clock to run despite the 
            # the computer being slow (or for game/simulation time) keep the line
            # outside of the if block

            # Seconds advanced ONLY after the sleep completes
            total_seconds_elapsed += 1
                            
            # Minute Logic
            if total_seconds_elapsed > 0 and (total_seconds_elapsed % SECONDS_PER_MINUTE) == 0:
                total_minutes_elapsed += 1
                                
                # Hour Logic
                if total_minutes_elapsed > 0 and (total_minutes_elapsed % MINUTES_PER_HOUR) == 0:
                    total_hours_elapsed += 1
                                    
                    # Days Logic
                    if total_hours_elapsed > 0 and (total_hours_elapsed % HOURS_PER_DAY) == 0:
                        total_days_elapsed += 1

                        # Weeks Logic
                        if total_days_elapsed > 0 and (total_days_elapsed % DAYS_PER_WEEK) == 0:
                            total_weeks_elapsed += 1

                            # Months Logic 
                            if total_weeks_elapsed > 0 and (total_weeks_elapsed % WEEKS_PER_MONTH) == 0:
                                total_months_elapsed += 1

                                # Years Logic 
                                if total_months_elapsed > 0 and (total_months_elapsed % MONTHS_PER_YEAR) == 0:
                                    total_years_elapsed += 1
                                    # Current Year
                                    canon_year += 1

                        # Seasons Logic
                        if total_days_elapsed > 0 and (total_days_elapsed % DAYS_PER_SEASON) == 0:
                            otal_seasons_elapsed += 1

                                                
                            
        # Time Rollovers --> display if no duo/hex conversion is used
        second = total_seconds_elapsed % SECONDS_PER_MINUTE
        hour_military = total_hours_elapsed % HOURS_PER_DAY
        # for hour_meridian rollover, increase the index display from 0
        # to 1: first hour to the specified MERIDIAN SEGMENT
        hour_meridian_raw = total_hours_elapsed % MERIDIAN_SEGMENT
        hour_meridian = hour_meridian_raw + 1
        minute = total_minutes_elapsed % MINUTES_PER_HOUR

        # apply same index increase method to days, weeks, and months.
        days_raw = total_days_elapsed % DAYS_PER_WEEK
        days = days_raw + 1
        weeks_raw = total_weeks_elapsed % WEEKS_PER_MONTH
        weeks = weeks_raw + 1
        months_raw = total_months_elapsed % MONTHS_PER_YEAR
        months = months_raw + 1
        seasons = total_seasons_elapsed % DAYS_PER_SEASON
                    
        # Rollover for the day of the month (previous version)
        day_of_month = total_days_elapsed % DAYS_PER_MONTH
                            
                        
        days_name_disp = DAY_NAMES.get(days-1) # Omit "N/A" to avoid math domain errors
        months_name_disp = MONTH_NAMES.get(months-1)

        # find the correct suffix for the day of the month, 

        def day_suf_len(day_input):
            day_string = str(day_input)
            day_len = len(day_string)

            if day_len == 1 or day_len == 2:
                day_suffix = days % 10
                return day_suffix
            else:
                day_suffix2 = days % 100
            if day_suffix2 !=11 or day_suffix2 !=12 or day_suffix != 13:
                day_suffix = days % 10
                return day_suffix
            else:
                day_suffix = day_suffix2
                return day_suffix

        # define a switch (match) case that handles adding suffix strings to the end of days

        def suffix(day_post_len):
            """function that serves as a match case (switch statement) for assiging a suffix string
            to a number
            """
            match day_post_len: 
                case 0 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13: 
                    suffix = "th"
                    return suffix 
                case 1:
                    suffix = "st"
                    return suffix
                case 2: 
                    suffix = "nd"
                    return suffix
                case 3: 
                    suffix = "rd"
                    return suffix
                            
        # create a variable to insert in custom suffix method that gives the approprite suffix string for the last integer(s) digits
        days_post_suf_len = day_suf_len(days)
        day_suffix_assigned = str(suffix(days_post_suf_len)) 

        """Method to construe an analog watch face using python's turtle"""

        ##### Analog display logic #####

        # --- 1. SETUP ---

        # Initialize the screen
        wndw = turtle.Screen()
        wndw.bgcolor("black")
        wndw.setup(width=600, height=600)
        wndw.title("Analog Clock Base")
        # Turn off screen updates for manual control (necessary for smooth animation)
        wndw.tracer(0) 

        # --- 2. PEN AND HAND CREATION ---

        # Create a common drawing pen for static elements
        def create_pen(color, speed=0):
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.color(color)
            pen.speed(speed)
            return pen
        
        # Create the specific hands (Hour, Minute, Second)
        def create_hand(shape, color, length, size):
            hand = turtle.Turtle()
            hand.shape(shape)
            hand.color(color)
            hand.shapesize(stretch_wid=size[0], stretch_len=size[1]) # stretch_len influences how long the hands are
            hand.penup()
            hand.speed(0) # Max speed
            return hand

        # --- 3. DRAW STATIC FACE ---

        def draw_static_face(pen):
            # Draw clock face circle
            pen.up()
            pen.goto(0, -210)
            pen.pensize(3)
            pen.color("green")
            pen.pendown()
            pen.circle(210)
            pen.penup()

            # Draw hour marks (16 ticks)
            for i in range(MERIDIAN_SEGMENT):
                pen.goto(0, 0)
                # Set heading to the current hour position
                pen.setheading(90 - (i * 30))
                pen.forward(190)
                pen.pendown()
                pen.pensize(2)
                pen.forward(20)
                pen.penup()

        # --- 4. UPDATE DYNAMIC HANDS ---

        def update_hands(hr_hand, mn_hand, sec_hand):
            # Get current system time
            now = datetime.datetime.now()
            hour = now.hour % 12  # Convert to 12-hour format (0-11)
            minute = now.minute
            second = now.second

            # --- ANGLE CALCULATION (Crucial for analog accuracy) ---
                                
            # Second Hand Angle (360 degrees / 60 seconds = 6 degrees/second)
            # The negative sign is because Turtle's 0 is East, 90 is North, and clock rotation is CW (negative heading change)
            sec_angle = -second * 6
            sec_hand.setheading(sec_angle + 90) # Added 90 to start at North
                                
            # Minute Hand Angle (360 / 60 = 6 degrees/minute + correction for seconds)
            mn_angle = -(minute * 6 + (second / 60) * 6)
            mn_hand.setheading(mn_angle + 90)
                                
            # Hour Hand Angle (360 / 12 = 30 degrees/hour + correction for minutes)
            hr_angle = -(hour * 30 + (minute / 60) * 30)
            hr_hand.setheading(hr_angle + 90)
                                
            # Update the screen once all hands are repositioned
            wndw.update()

        # --- 5. MAIN EXECUTION LOOP ---

        # A. Initial Setup (runs once)
        static_pen = create_pen("gray")
        draw_static_face(static_pen)
                                
        # B. Create the Hands
        sec_hand = create_hand("triangle", "red", 110, (0.1, 16)) # Elongate the hands by changing the second tuple numbers
        mn_hand = create_hand("triangle", "blue", 150, (0.2, 14))
        hr_hand = create_hand("triangle", "white", 80, (0.3, 9))

        # C. Main Update Loop (i.e., display watch face)
        try:
            while True:
                # Clear the static pen once (optional, but clean)
                # static_pen.clear() 
                                        
                # The hands must be cleared before being redrawn in the new position
                sec_hand.clear()
                mn_hand.clear()
                hr_hand.clear()
                                        
                # Update the hand positions
                update_hands(hr_hand, mn_hand, sec_hand)
                                        
                # Wait for one second before the next update
                time.sleep(1)

        except (KeyboardInterrupt, RecursionError):
            print("\nClock stopped by user interruption.")
        finally:
            # Crucial: This ensures the graphics window remains open until manually closed
            wndw.mainloop()


    """Print statements for diagnostic/display purposes."""
    # printout constant for entered plnaet name 
    def const_planet_name_print(self):
        """A function that prints out the entered constant for the planet's name for chonology"""

        # print entered planet name
        print("\nEntered planet name:")
        print(f"Planet: {self.planet_name}")

    # print out constants of entered dictionaries for time constants
    def const_time_print(self): 
        """A function that prints out the entered constants for the time and date."""

        # print entered time constants
        print("\nEntered time constants: ")
        for interval, time in self.time_constants.items():
            print(f"{interval}: {time}")

        # print entered date constants
        print("\nEntered date constants: ")
        for interval, date in self.date_constants.items():
            print(f"{interval}: {date}")

        # print entered day segment duration period for meridian times
        print(f"\nEntered day segment (period) constant: {self.meridian_segment}")


    # print out constants of entered dictionary for specific days of the months
    def const_weekdays_print(self):
        """A fucntion rhat prints out the entered specific days of one week."""

        # print out specific weekdays 
        print("\nEntered weekdays for a week: ")
        for i, weekday in self.day_names.items():
            print(f"#{i+1}: {weekday}")

    # print out constants of entered dictionary for specific month names
    def const_months_print(self):
        """A function that prints otu the entered months of one year."""

        # print out specific months
        print("\nEntered months for a year")
        for i, month in self.month_names.items():
            print(f"{i+1}: {month}")

    # print out entered meridian range (indexed lists)
    def const_meridian_print(self):
        """A function that prints out the entered specific index ranges to mark the meridiansn of a full day."""

        # print out the index ranges for the meridians that mark a full day
        print("\nEntered indexes for meridians: ")
        for m, mlist in self.meridian.items():
            print(f"Meridian: {m}; Index Range: {mlist}")

    # print out entered tick interval range constnat
    def const_tick_int_print(self):
        """A function that prints out the entered specific tick interval for the seconds."""

        # print out tick interval
        print(f"\nEntered tick interval (seconds): {self.tick_interval}")
        
    # print out entered canon_year 
    def const_canon_year_print(self): 
        """A function that prints out the entered specific canon year"""

        # print out canonyear
        print(f"\nEntered canon year {self.canon_year}")
    
