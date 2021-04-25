from enum import Enum
import random
from typing import Sequence

from pydantic import BaseModel


class Card(BaseModel):
    word: str


class Board(BaseModel):
    cards: Sequence[Card]
    
    @classmethod
    def generate_random(cls, n: int, vocab: Sequence[str], seed: int=0):
        random.seed(seed)
        
        return cls(cards=[Card(word=x) for x in random.sample(vocab, n)])


class CardAssignment(Enum):
    NEUTRAL = 0
    RED = 1
    BLUE = 2
    SPY = 3


class Assignments(BaseModel):
    assignments: Sequence[CardAssignment]
        
    @classmethod
    def generate_random(cls, n: int, each: int, seed: int=0):
        random.seed(seed)
        
        if (each * 2 + 1) > n:
            raise ValueError
            
        assignments = (
            [CardAssignment.RED] * (each + 1)
            + [CardAssignment.BLUE] * each
            + [CardAssignment.SPY]
            + [CardAssignment.NEUTRAL] * (n - 2 * each - 2)
        )
        
        random.shuffle(assignments)
        
        return cls(assignments=assignments)


class Team(Enum):
    RED = 1
    BLUE = 2


class GameState(BaseModel):
    selected: Sequence[bool]
    turn: Team
