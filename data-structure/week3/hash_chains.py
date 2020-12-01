# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class Queries:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.queries_list = []
        self.read_queries()
        self.queries = {}

    def __hash(self, string):
        hashed = 0
        for c in reversed(string):
            hashed = (hashed * self._multiplier + ord(c)) % self._prime
        return hashed % self.bucket_count

    def read_query(self):
        return 

    def find(self, string):
        hashed = self.__hash(string)
        if hashed in self.queries:
            if string in self.queries[hashed]:
                return "yes"
        return "no"

    def add(self, string):
        hashed = self.__hash(string)
        if hashed in self.queries:
            self.queries[hashed].add(string)
        else:
            self.queries[hashed] = set()
            self.queries[hashed].add(string)

    def check(self, hash):
        if hash in self.queries:
            return ' '.join([str(item) for item in list(self.queries[hash])[::-1]])
        return ""

    def delete(self, string):
        if self.find(string) == "yes":
            hashed = self.__hash(string)
            self.queries[hashed].remove(string)

    def process_queries(self):
        log = []
        for query in self.queries_list:
            if query.type == "check":
                log.append(self.check(query.ind))
            elif query.type == "add":
                self.add(query.s)
            elif query.type == "find":
                log.append(self.find(query.s))
            elif query.type == "del":
                self.delete(query.s)
        return log

    def print_queries(self):
        log = self.process_queries()
        for item in log:
            print(item)

    def read_queries(self):
        n = int(input())
        for _ in range(n):
            self.queries_list.append(Query(input().split()))

if __name__ == '__main__':
    bucket_count = int(input())
    proc = Queries(bucket_count)
    proc.print_queries()
