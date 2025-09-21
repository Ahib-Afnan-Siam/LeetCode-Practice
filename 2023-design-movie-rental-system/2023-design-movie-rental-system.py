from sortedcontainers import SortedList
from typing import List

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # Map (shop, movie) -> price
        self.price_map = {}
        
        # Available movies: movie_id -> sorted list of (price, shop)
        self.available = {}
        
        # Rented movies: sorted list of (price, shop, movie)
        self.rented = SortedList()
        
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((price, shop))
    
    def search(self, movie: int) -> List[int]:
        if movie not in self.available:
            return []
        return [shop for price, shop in self.available[movie][:5]]
    
    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))
    
    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))
    
    def report(self) -> List[List[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()