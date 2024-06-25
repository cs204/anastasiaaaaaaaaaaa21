def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    q=input()
    f=convert(q)
    print(f)

if __name__ == "__main__":
    main()

