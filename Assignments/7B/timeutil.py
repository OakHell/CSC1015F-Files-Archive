# timeutil.py
# Module containing time functions
# Stephan Jamieson
import trace

def validate(time):
    time=time.strip()
    colon = time.find(':')
    if colon<1:
        return False
    else:
        hours = time[:colon]
        if len(hours)>2 or len(hours)<1 or not hours.isdigit():
            return False
        
        if len(hours)==2 and int(hours[0])==0:
            return False
        
        suffix = time[-5:]
        if not suffix==' a.m.' and not suffix==' p.m.':
            return False
        
        minutes = time[colon+1:len(time)-5]
        if not len(minutes)==2 or not minutes.isdigit():
            return False

        hours = int(hours)
        minutes = int(minutes)
        return hours>0 and hours<13 and minutes>-1 and minutes<60


    
    