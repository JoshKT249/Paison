def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    ans = ans.casefold().strip()
    if iscorrect(ans)== True:
        print("Yes")
    else:
        print("No")

def iscorrect(x):
    match x:
        case "42" | "forty-two" | "forty two":
            return(True)

main()
