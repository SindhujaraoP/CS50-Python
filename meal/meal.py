def main():
    inp = input("What's the time? ").strip()
    hour = convert(inp)

    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("lunch time")
    elif 18.0 <= hour <= 19.0:
        print("dinner time")
    else:
        return

def convert(x):
    a,b = x.split(":")
    return float(a)+float(b)/60

if __name__ == "__main__":
    main()
