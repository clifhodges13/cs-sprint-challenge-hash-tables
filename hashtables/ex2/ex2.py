#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickets_hash = {}

    route = []

    # hash each ticket
    for i in tickets:
        tickets_hash[i.source] = i.destination
    

    # find the first ticket, source == "NONE"
    prev_ticket = tickets_hash["NONE"]
    route.append(prev_ticket)
    
    next_ticket = tickets_hash[prev_ticket]
    i=0
    while i < len(tickets)-1:
        route.append(next_ticket)
        prev_ticket = next_ticket
        next_ticket = tickets_hash[next_ticket]
        i += 1


    return route # route will be an array of strings with entire trip in order
