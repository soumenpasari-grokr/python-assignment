from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_gender(self): pass