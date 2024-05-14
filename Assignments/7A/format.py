def time_str(hours, minutes):

    if minutes==0:
        return '{:} o\'clock'.format(hours)
    elif minutes==30:
        return 'half past {:}'.format(hours)
    elif minutes < 30:
        preposition = 'past'
    else:
        preposition = 'to'
        hours = hours+1
        if hours > 12:
            hours = 1
        minutes = 60-minutes
    if minutes == 1:
        unit_string = 'minute'
    else:
        unit_string = 'minutes'
    return '{:} {:} {:} {:}'.format(minutes, unit_string, preposition, hours)