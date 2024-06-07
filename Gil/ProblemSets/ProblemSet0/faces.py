def main():
    face = input()
    convert(face)
    print(convert(face))

def convert(emoji):
    return(emoji == str.replace(":)","🙂")&(":(","🙁"))

main()