def main():
    Ftype = input("File name: ")
    Ftype = Ftype.casefold().strip()
    atype = cutoff(Ftype,".")
    match atype:
        case ".gif":
            print("image/gif")
        case ".jpeg" | ".jpg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


def cutoff(string,dot):
    index=string.rfind(dot)
    return string[index:]


main()
