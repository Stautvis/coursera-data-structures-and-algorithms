class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


class PhoneBook:
    def __init__(self):
        self.contacts = {}
        self.read_queries()

    def find(self, number):
        if number in self.contacts:
            return self.contacts[number]
        return "not found"

    def add(self, name, number):
        self.contacts[number] = name

    def delete(self, number):
        if self.find(number) != "not found":
            self.contacts.pop(number)

    def solve(self):
        log = self.process_queries()
        self.write_responses(log)

    """Queries"""
    def read_queries(self):
        n = int(input())
        self.queries = [Query(input().split()) for i in range(n)]

    def process_queries(self):
        log = []
        for query in self.queries:
            if query.type == "add":
                self.add(query.name, query.number)
            elif query.type == 'del':
                self.delete(query.number)
            else:
                log.append(self.find(query.number))
        return log

    def write_responses(self, log):
        print('\n'.join(log))


if __name__ == '__main__':
    phone_book = PhoneBook()
    phone_book.solve()

