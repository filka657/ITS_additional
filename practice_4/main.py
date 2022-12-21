from git import Repo

DEFAULT_FOLDER = "C:\\test"


def MyGenerator():
    start = 0
    while True:
        yield start
        start += 2


def print_even_numbers(n):
    x = MyGenerator()
    for i in range(n):
        print(next(x))


if __name__ == '__main__':
    with open("in", "r") as in_file:
        lines = in_file.readlines()
        in_file.close()

        for line in lines:
            parts = line.split('/')
            try:
                Repo.clone_from(line, DEFAULT_FOLDER + "\\" + parts[-1])
                line = "OK........." + line + "\n"
            except:
                line = "FAIL........." + line + "\n"

        with open("out.txt", "w") as out_file:
            out_file.writelines(lines)
            out_file.close()