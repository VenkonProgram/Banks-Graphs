import time
# User class is an object of user which will be call by the main module
# Users are stored in a hash table
class User:
    def __init__(self, idUser, name):
        self.idUser = idUser
        self.name = name
        self.accounts = AccountsMaxHeap()
        # Stores all the accounts of the user in a MaxHeap, the order criteria is how many times an account is used

    def __str__(self):
        return str(self.idUSer)

    def __hash__(self):
        return hash(self.idUser)

    def getId(self):s
        return self.idUser

    # Add an account into the accounts MaxHeap
    def addAccount(self, account):
        self.accounts.insertAccount(account)

    # Remove an account that is in the MaxHeap
    def removeAccount(self, idAccount):
        self.accounts.removeAccount(idAccount)

    # Increase the number of how many times the account is used
    def useAccount(self, idAccount):
        self.accounts.increaseKey(idAccount)

# Account class is an object of user which will be call by the main module
# Accounts are stored in a hash table
class Account:
    def __init__(self, idAccount, user, frequency = 0):
        self.idAccount = idAccount
        self.idUser = user
        self.frequency = frequency
        self.edges = EdgesMinHeap()

    def __str__(self):
        return str(self.idAccount)

    def __hash__(self):
        return hash(self.idAccount)

    def getId(self):
        return self.idAccount

    # Add a transaction between the origin and destination
    def addEdge(self, dest, quantity):
        if self.edges.getTotalEdges() == 15:
            self.edges.removeOldest()
        myEdge = self.edges.getEdge(dest)
        if myEdge is not None:
            myEdge.uses + 1
            myEdge.add(quantity)
        else:
            newEdge = Edge(dest, 1)
            newEdge.add(quantity)
            self.edges.insertEdge(newEdge)

##    def removeEdge():
        #will see

class Edge:

    def __init__(self, dest, uses):
        self.dest = dest
        self.uses = uses
        self.quses = Queue()
        self.money = Queue()
        self.size = 0

    def __str__(self):
         return str(self.dest)

    def getDest(self):
         return self.dest

    # Add money and time into the transaction
    def add(self, quantity):
        self.quses.enqueue(time.time())
        self.money.enqueue(quantity)
        self.size += 1

    # Remove money and time of the oldest transaction
    def removeO(self):
        self.quses.dequeue()
        self.money.dequeue()
        self.size -= 1

    # To know if the size is empty
    def sizeEmpty(self):
        return self.size == 0

class Queue:
    def __init__(self,queue):
        self.queue = []
    def dequeue(self):
        return self.queue.pop(0)
    def enqueue(self,element):
        self.queue.append(element)
