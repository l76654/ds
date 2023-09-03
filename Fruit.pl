fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).
fruit_color(kiwi, green).
fruit_color(lemon, yellow).
fruit_color(pineapple, yellow).
fruit_color(cherry, red).
find_color(Fruit, Color) :-
    fruit_color(Fruit, Color).
find_fruit(Color, Fruit) :-
    fruit_color(Fruit, Color).
