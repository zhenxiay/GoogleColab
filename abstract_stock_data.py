from abc import ABC, abstractmethod

#Abstract class definition
class StockDataStructure(ABC):
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def create_fig(self):
        pass
