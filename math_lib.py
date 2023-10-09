from dataclasses import dataclass

@dataclass
class vec2:
    x: int
    y: int

@dataclass
class triangle:
    p1: vec2
    p2: vec2
    p3: vec2