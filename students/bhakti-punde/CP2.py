def ask_mark(prompt):
    while True:
        text = input(prompt)
        if not text.isdigit():
            print("Please enter a whole number.")
            continue
        mark = int(text)
        if 0 <= mark <= 100:
            return mark
        else:
            print("Mark must be between 0 and 100.")
