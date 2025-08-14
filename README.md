🚖 Ride-Sharing Dispatch Simulator

A fun little college project that simulates how a ride-sharing service (like Uber or Ola) assigns drivers to riders.
It matches the nearest driver first, and if two drivers are equally far, the one with the better rating gets the ride.
Also keeps a ride history so you can see who got matched with whom.

✨ Features

Add Drivers with their distance and rating.

Add Riders to a waiting queue (first come, first served).

Ride History: view all completed rides.

Simple & Fast: uses Python’s deque for instant queue operations.

🛠 How It Works

Riders join a queue — whoever requests first waits at the front.

Drivers are stored in a list — sorted by distance (smallest first), then rating (highest first).

When matching happens:

The first rider in queue is assigned to the best driver.

That driver is removed from the available list.

The ride is recorded in history for later review.

>>Example input

Add some drivers
add_driver(1, "aman", 2.5, 4.8)
add_driver(2, "riya", 3.5, 1.8)
add_driver(3, "sahihl", 4.8, 4.2)

# Riders request rides
request_ride("joy")
request_ride("arpit")

# Match riders to drivers
match_driver()
match_driver()

# See who got matched
show_history()

>>Output

Rider 'joy' added to queue.
Rider 'arpit' added to queue.
Matched Rider 'joy' with Driver 'aman'.
Matched Rider 'arpit' with Driver 'riya'.

Ride History:
Rider: joy , Driver: aman
Rider: arpit , Driver: riya
