from collections import deque

riders = deque()
drivers = []
history = []


def add_drivers(driver_id,name,distance,rating):
    drivers.append({
        "id" : driver_id,
        "name" : name,
        "distance" : distance,
        "rating": rating
    })

def request_riders(rider_name):
    riders.append(rider_name)
    print(f"Rider '{rider_name}'added to queue.")

def match_drivers():
    if not riders:
        print("no riders in queue.")
        return
    if not drivers:
        print("no drivers available.")        
        return
    
    drivers.sort(key=lambda d : (d["distance"], -d['rating']))

    rider = riders.popleft()
    driver = drivers.pop(0)
    history.append({"rider":rider, "driver": driver["name"]})
    print(f"Matched Rider '{rider}' with Driver '{driver['name']}'.")

def show_history():
    print("Ride history")
    for ride in history:
        print (f"rider : {ride['rider']} , Driver : {ride['driver']} ")
    if not history :
        print ("no rides booked")

add_drivers(1,"aman",2.5,4.8)
add_drivers(2,"riya",3.5,1.8)
add_drivers(3,"sahil",4.8,4.2)

request_riders("joy")
request_riders("arpit")

match_drivers()
match_drivers()
show_history()