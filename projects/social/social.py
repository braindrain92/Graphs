import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create friendships
        # Generate a list of all possible friendships
        possibleFriendships = []
        #Avoid duplicates by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )

        print(possibleFriendships)
        # Shuffle the list
        random.shuffle(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        for i in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[i]
            self.addFriendship( friendship[0], friendship[1] )

        print(f"Friendships to create: {(avgFriendships * numUsers // 2) * 2}")

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # start a queue and add starting node
        q = []
        q.append(userID)
        # initialize first path
        visited[userID] = [userID]
        # while queue is not empty
        while len(q) > 0:
            # grab first element from queue
            current = q.pop(0)
            # for each friendship of current
            for friend in self.friendships[current]:
                # if friend has not been visited/is not key in visited dictionary
                if friend not in visited:
                    # add key to visited dictionary with existing path from userID plus the friend ID
                    visited[friend] = visited[current] + [friend]
                    # add friend to queue
                    q.append(friend)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
