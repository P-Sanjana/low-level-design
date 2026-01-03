class SearchQuery:
    def __init__(self, builder):
        self.search = builder.search
        self.filters = builder.filters
        self.sort = builder.sort
        self.size = builder.size


    def __str__(self):
        return f'SearchQuery(search={self.search}, filters={self.filters}, sort={self.sort}, size={self.size}'

    class SearchQueryBuilder:
        def __init__(self, search):
            self.search = search
            self.filters = {}
            self.sort = {}
            self.size = 50

        def add_filter(self, key, value):
            self.filters[key] = value
            return self

        def add_sort(self, sort_by, order):
            self.sort[sort_by] = order
            return self

        def add_size(self, size):
            self.size = size
            return self

        def build(self):
            return SearchQuery(self)

if __name__=="__main__":
    search_query1 = SearchQuery.SearchQueryBuilder('Bitcoin').build()
    print(search_query1)
    search_query2 = SearchQuery.SearchQueryBuilder('Ethereum').add_filter('price', 60000).build()
    print(search_query2)
    search_query3 = SearchQuery.SearchQueryBuilder('Bitcoin').add_filter('price', 80000).add_sort('timestamp', 'desc').add_size(100).build()
    print(search_query3)


