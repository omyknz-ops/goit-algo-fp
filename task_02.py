import turtle

#Setup drawing window
def setup_screen():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Pythagoras Tree Fractal")
    screen.setup(width=800, height=600)
    return screen

#Setup turtle object
def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)  # Maximum speed
    t.left(90)  # Turn upward
    t.penup()
    t.goto(0, -250)  # Starting position
    t.pendown()
    t.color("brown")
    t.pensize(1)
    return t

# Recursive function to draw Pythagoras Tree
def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return  # Base case: stop recursion
    
    # Draw current branch
    t.forward(branch_length)
    
    # Save current position and heading
    position = t.position()
    heading = t.heading()
    
    # Draw left branch
    t.left(45)
    draw_pythagoras_tree(t, branch_length * 0.7, level - 1)
    
    # Return to saved position
    t.penup()
    t.goto(position)
    t.setheading(heading)
    t.pendown()
    
    # Draw right branch
    t.right(45)
    draw_pythagoras_tree(t, branch_length * 0.8, level - 1)


# Main program
if __name__ == "__main__":
    screen = setup_screen()
    t = setup_turtle()
    
    # User can specify recursion level
    level = int(input("Введіть рівень рекурсії (5-12): "))
    initial_length = 120
    
    draw_pythagoras_tree(t, initial_length, level)
    
    screen.exitonclick()