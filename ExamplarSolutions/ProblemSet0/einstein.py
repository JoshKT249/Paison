def main():
    # assuming only valid input will be given
    mass = int(input("m: "))
    c = 300000000
    # could use math module here for pow()
    energy = mass * c * c
    print(f"E: {energy}")

if __name__ == "__main__":
    main()