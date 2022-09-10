from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("orange")
        self.penup()        
        self.hideturtle()
        self.goto(position)
        self.write_score()


    def write_score(self):
        self.write(f"Score: {self.r_score}", align=ALIGNMENT, font=FONT)
    
    def white_score(self):
        self.write(f"Score: {self.l_score}", align=ALIGNMENT, font=FONT)
    
    def update_score(self):
        self.r_score+=1
        self.l_score+=1
        self.clear()
        self.write_score()
    
    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)