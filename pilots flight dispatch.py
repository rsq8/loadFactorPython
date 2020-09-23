#This programme cacolates the payload(weight) an s92 helicopter can carry for a 
#given mission. results displayed in a terminal window/

class dispatch():
    def payloadavailable(self,aps,crew,fuel):        # calculate disposable weight
        return 26500-aps-crew-fuel


    def zerofuelweight(self,aps,crew):      # calculate Zero fuel weight
        return aps + crew


    def mslsload(self,paxw,bag,freight,zfw,fuel):            #calculate MSLS Loaad (paxw=pax weight)
        return paxw + bag + freight + zfw + fuel

def main():
    d = dispatch()
    #collect all required data
    
    aps = int(input("enter APS weight as seen on MSLS:"))
    pilot = int(input("enter Pilot weight:"))
    copilot = int(input("enter copilot weight:"))
    crew = pilot + copilot
    fuel = int(input("enter fuel loaded:"))
    paxw = int(input("enter pax weight:"))
    bag = int(input("enter baggage weight:"))
    freight = int(input("enter freight weight:"))
    luggage = bag + freight
    question = input("What would you like to calculate?:")

    if question == "payload":
        p = str(d.payloadavailable(aps,crew,fuel))
        print(p +"lbs")       
       
    elif question == "take-off weight":
        l = str(luggage)
        if luggage > 1000:
            print(l + "lbs","exceeds the maximum allowable (1000lbs) in the baggage compartment!")
            print("please reduce luggage!!")
                
        zfw = d.zerofuelweight(aps,crew)
        TO_weight = d.mslsload(paxw,bag,freight,zfw,fuel)
        t = str(TO_weight)
        if TO_weight > 26500:
            print(t + "lbs","exceeds the maximum alloawable(26500lbs) take-off weight")
            print("It is illegal to fly!")
        else:
            print(t + "lbs")    
            print("Enjoy your flight!")
    else:
        print("invalid entry, restart program and enter 'payload' or 'take-off weight'")

if __name__ == "__main__":
    main()
