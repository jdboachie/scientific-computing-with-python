def parse(time, is_24hr=False):
    pieces = time.split(":")

    if is_24hr:
        pieces = [piece.split(" ") for piece in pieces]
        pieces = pieces[0] + pieces[1]
        return [pieces[0], pieces[1], pieces[2]]
    else:
        return [pieces[0], pieces[1]]


def add(start_time, duration):
    hours = int(start_time["hours"]) + int(duration["hours"])
    minutes = int(start_time["minutes"]) + int(duration["minutes"])

    if minutes >= 60:
        hours += (minutes // 60)
        minutes = minutes % 60

    return {"hours": hours, "minutes": minutes, "GMT": start_time["GMT"]}


def to_12hr(time):
    old_time = time["hours"]

    if time["hours"] >= 12:
        if time["GMT"] == "PM":
            days = (time["hours"] + 12) // 24
        else:
            days = time["hours"] // 24
        time["days"] = days

        if time["hours"] % 12 != 0:
            time["hours"] %= 12
        else:
            time["hours"] = 12

        if time["GMT"] == "AM":
            if old_time >= 12:
                time["GMT"] = "PM"
        else:
            if old_time >= 12:
                time["GMT"] = "AM"

        if days > 1:
            time["days_later"] = f" ({days} days later)"
        elif days == 1:
            time["days_later"] = " (next day)"
    return time


def construct_return_string(time, day = None):
    # Two-digit decoration: adding a zero in front of single-digit numbers
    if len(str(time["minutes"])) == 1:
        minutes = "0" + str(time["minutes"])
    else:
        minutes = str(time["minutes"])

    if time["day"] and not time["days_later"]:
        print("here")
        return str(time["hours"]) + ":" + minutes + " " + str(time["GMT"]) + ", " + time["day"]
    elif time["day"] and time["days_later"]:
        print("there")
        return str(time["hours"]) + ":" + minutes + " " + str(time["GMT"]) + ", " + time["day"] + time["days_later"]
    else:
        print("where")
        return str(time["hours"]) + ":" + minutes + " " + str(time["GMT"])


def do_day(time, day):
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    time["day"] = days_of_the_week[days_of_the_week.index(day) + time["days"]]
    return time


def add_time(start, duration, day = None):
    
    # Step 1
    start = parse(start, is_24hr=True)
    start_time = {"hours": start[0], "minutes": start[1], "GMT": start[2]}

    # Step 2
    duration = parse(duration, is_24hr=False)
    duration = {"hours": duration[0], "minutes": duration[1]}

    # Step 3
    added_time = add(start_time, duration)
    added_time["day"] = None

    # Step 4
    added_time = to_12hr(added_time)
    
    # Step 5
    if day:
        added_time = do_day(added_time, day.lower().capitalize())
        return construct_return_string(added_time)
    else:
        return construct_return_string(added_time)

print(add_time("11:59 Pm", "24:05"))