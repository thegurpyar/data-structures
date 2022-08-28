# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]




def process_queries(queries,contacts):
    if queries.type=="add":
        contacts[queries.number]=queries.name
    
    elif queries.type=="del":
        if contacts.__contains__(queries.number):
            del contacts[queries.number]
    
    else:
        response = 'not found'
        if contacts.__contains__(queries.number):
            response=contacts[query.number]
        return response
if __name__ == '__main__':
    contacts={}
    queries=int(input())
    for _ in range(queries):
        query=Query(input().split())
        result=process_queries(query,contacts)
        if result:
            print(result)
