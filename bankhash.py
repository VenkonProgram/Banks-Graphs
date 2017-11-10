# TODO - FIX HASHTABLE

class BankHash:
    def __init__(self):
        self.size = 25
        self.buckets = [None] * self.size

    def __str__(self):
        toPrint = ""
        for bucket in self.buckets:
            toPrint += str(bucket) + "\n"
        return toPrint
            

    def put(self,value):
        hashedkey = hash(value) % self.size

        if self.buckets[hashedkey] == None:
            self.buckets[hashedkey] = value

        ##elif self.buckets[hashedkey] == value:
        ##    self.values[hashedkey] = value

        else:
            ##while(self.buckets[hashedkey] != None and self.buckets != value):

            hashedkey = (hashedkey + 1) % self.size
            i = 0
            while self.buckets[hashedkey] != None and i < self.size:
                hashedkey = (hashedkey + 1) % self.size
                i+=1
            if self.buckets[hashedkey] == None:
                self.buckets[hashedkey] = value



    def get(self, value):
        start= hashedkey = hash(value) % self.size
        val = None
        done = False

        while not done:
            if self.buckets[hashedkey].getId() == value:
                val = self.buckets[hashedkey]
                done = True

            else:
                hashedkey = (hashedkey + 1)%self.size
                if hashedkey ==  start:
                    done = True

                elif self.buckets[hashedkey] == None:
                    done = True

        return val

    def delete(self,key):
        hashedkey = hash(key)% self.size
        i = hashedkey
        prev = self.buckets[hashedkey]
        while prev.getId() != key:
            if prev != None:
                i = (hashedkey + 1) % self.size
                prev = self.buckets[i]
                
            else:
                return None

        self.buckets[i] = None

        while self.buckets[(i + 1) % self.size] != None and hash(self.buckets[(i + 1) % self.size].getId())%self.size == hashedkey:
            self.buckets[i] = self.buckets [(i+1) % self.size]
            i = (i + 1) % self.size
            self.buckets[i] = None

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,val):
        self.put(key,val)
