
def create_message(s):
    lis = [s]
    def merger(something = ""):
        if not something:
            return " ".join(lis)
        lis.append(something)
        return merger
    return merger


if __name__ == "__main__":
    print(create_message("Hello")("World!")("how")("are")("you?"))