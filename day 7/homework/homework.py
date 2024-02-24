def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("This triangle exists.")
    else:
        print("This triangle does not exist.")

def name_combiner(name1, name2, name3):
    names = [name1, name2, name3]
    print(' '.join(names))

check_triangle(69, 420, 404)
name_combiner('Gela', 'Gogita', 'Levana')
