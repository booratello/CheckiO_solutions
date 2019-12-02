"""
We have an array of straight connections between drones. Each connection is represented as a string with two names of
friends separated by hyphen. Your should write a function that allow determine more complex connection between drones.
You are given two names also. Try to determine if they are related through common bonds by any depth.
For example: if two drones have a common friends or friends who have common friends and so on.

Input:Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.
"""


def check_connection(network, first, second):
    friends = [first]
    network = list(network)
    while len(friends) != 0:
        for pair in network:
            if pair.find(friends[0]) != -1:
                friends.append(pair.replace(friends[0], "").replace("-", ""))
                network.remove(pair)
        friends.pop(0)
        if second in friends:
            return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
