import turtle
import math

def draw_branch(t, length, level):
    """
    Рекурсивна функція для малювання дерева Піфагора.
    
    :param t: Об'єкт Turtle для малювання
    :param length: Довжина поточної гілки
    :param level: Поточний рівень рекурсії
    """
    if level == 0:
        return
    
    t.forward(length)
    t.left(45)
    draw_branch(t, length / math.sqrt(2), level - 1)
    
    t.right(90)
    draw_branch(t, length / math.sqrt(2), level - 1)
    t.left(45)
    t.backward(length)

def main():
    """
    Основна функція програми. Запитує рівень рекурсії у користувача
    і викликає функцію для побудови дерева Піфагора.
    """
    level = int(input("Введіть рівень рекурсії: "))
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.goto(0, -200)
    t.down()
    
    draw_branch(t, 100, level)
    
    turtle.done()

if __name__ == "__main__":
    main()