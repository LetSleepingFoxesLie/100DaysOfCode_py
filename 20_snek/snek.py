from turtle import Turtle

MOVE_DISTANCE = 20

ANGLE_UP = 90
ANGLE_LEFT = 180
ANGLE_DOWN = 270
ANGLE_RIGHT = 0

class Snek:
    
    def __init__(self) -> None:
        self.segments_list = self.initialize_body()
        self.head = self.segments_list[0]
    
    # Generates a list and some segments, initializing the snake's body
    def initialize_body(self) -> None:
        s = list()
    
        for p in [(0,0), (-20, 0), (-40, 0)]:
            n = self.generate_body_segment()
            n.penup()
            n.setposition(p)
            s.append(n)
        
        return s
    
    # Generates a body segment... except this toesn't work very well for anything other than generating the starting ones
    def generate_body_segment(self) -> Turtle:
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        return segment
    
    # This actually works for extending the snake!
    def extend_snek(self) -> None:
        new_segment = self.generate_body_segment()
        new_segment.setpos(self.segments_list[-1].position()) # [-1] refers to the last element in an iterable. C should have this
        self.segments_list.append(new_segment)
    
    # Movement controls
    def snek_move_up(self):
        if self.head.heading() != ANGLE_DOWN:
            self.head.seth(ANGLE_UP)
    
    def snek_move_left(self):
        if self.head.heading() != ANGLE_RIGHT:
            self.head.seth(ANGLE_LEFT)
    
    def snek_move_down(self):
        if self.head.heading() != ANGLE_UP:
            self.head.seth(ANGLE_DOWN)
    
    def snek_move_right(self):
        if self.head.heading() != ANGLE_LEFT:
            self.head.seth(ANGLE_RIGHT)
    
    # And this one last function to calculate the position of all segments in the body
    def move_snek_body(self, segments: list[Turtle]) -> None:
        
        # Work from back to to front, setting the position of the last segment to the position of the next segment.
        for i in range(len(segments) - 1, 0, -1):
            nx = segments[i - 1].xcor()
            ny = segments[i - 1].ycor()
            
            segments[i].setpos(nx, ny)
        self.head.forward(MOVE_DISTANCE)