#This programme calculates flight times (block-time, etc) as determined in aviation.
#The calculations are client specific.
import datetime

class flightdutytime():

    def pilottime(self,e,a):
        t = datetime.timedelta
        # convert shut down time
        shtdn = e.split()
        shthr = int(shtdn[0])
        shtmin = int(shtdn[1])
        shut_down = t(hours=shthr, minutes=shtmin)
        #convert start time
        strt = a.split() 
        shr= int(strt[0])
        smin = int(strt[1])
        start = t(hours=shr, minutes=smin)
        pt = shut_down - start
        return pt

    def flighttime(self,d,c):
        t = datetime.timedelta
        #convert landing time
        landing = d.split()
        ldhr = int(landing[0])
        ldmin = int(landing[1])
        lndg = t(hours=ldhr, minutes=ldmin)
        #convert takeoff time
        toff = c.split()
        toffhr = int(toff[0])
        toffmin = int(toff[1])
        t_off = t(hours=toffhr, minutes=toffmin)
        ft = lndg - t_off
        return ft

    def chevron(self,b,e):
        t = datetime.timedelta
        #convert taxi time
        txy = b.split()
        thr = int(txy[0])
        tmin = int(txy[1])
        taxi = t(hours=thr, minutes=tmin)
        # convert shut down time
        shtdn = e.split()
        shthr = int(shtdn[0])
        shtmin = int(shtdn[1])
        shut_down = t(hours=shthr, minutes=shtmin)
        Ft = shut_down - taxi
        return Ft
    
    def chevron2(self,d,e):
        t = datetime.timedelta
        #convert landing time
        landing = d.split()
        ldhr = int(landing[0])
        ldmin = int(landing[1])
        lndg = t(hours=ldhr, minutes=ldmin)
        # convert shut down time
        shtdn = e.split()
        shthr = int(shtdn[0])
        shtmin = int(shtdn[1])
        shut_down = t(hours=shthr, minutes=shtmin)
        #chevron 5min deck time
        uplift = lndg + t(minutes=5)
        time = shut_down - uplift
        return time

def main():
    T = flightdutytime()
    a = input("start time:")
    b = input("taxi time:")
    c = input("takeoff time:")
    d = input("landing time:")
    e = input("shutdown time:")
    client = input("please enter the name of the client:")
    
    if client == "adhoc":
        print("pilot time =", T.pilottime(e,a))
        print("client time =", T.pilottime(e,a))

    elif client == "chevron":
        answer = input("are your rotors running?:")
        if answer == "no":
            print("pilot time =", T.pilottime(e,a))
            print("client time =", T.chevron(b,e))
        elif answer == "yes":
            print("pilot time =", T.pilottime(e,a))
            print("client time =", T.chevron2(d,e))
        else:
            print("run the program again and please enter yes or no to rotors running question")

    else:
        print("pilot time =", T.pilottime(e,a))
        print("client time =", T.flighttime(d,c))

    print("Thank you!")

if __name__=="__main__":
    main()
