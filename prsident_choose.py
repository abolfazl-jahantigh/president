def main(n):
    score = 0
    for i in range(2, n + 1):
        score = (score + 2) % i
    return score + 1
def get():
    while True:
        try:
            a = input("enter a number between 2 and 100 ")
            if not a.isdigit():
                print("invalid input ")
                continue
            a = int(a)
            if a < 2 or a > 100:
                print("the number must be between 2 and 100 ")
                continue
            return a
        except ValueError:
            print("invalid input ")
n = get()
print(f"our new president is : {main(n)}")