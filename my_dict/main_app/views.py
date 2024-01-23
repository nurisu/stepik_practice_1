from django.shortcuts import render

# Create your views here.

def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()

    words1 = []
    words2 = []
    for line in file:
        if len(line) == 0:
            return [], []
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    print(words1, words2)
    return words1, words2


def words_list(request):
    t = read_from_file()
    l = []
    for i in range(len(t[0])):
        l.append([t[0][i], t[1][i]])
    context = {"dictionary": l}
    return render(request, "words_list.html", context)


def add_word(request):
    if request.method == "GET":
        return render(request, "add_word.html")
    else:
        data = request.POST
        add_to_file(data['word1'], data['word2'])
        return render(request, "add_word.html")

def home(request):
    return render(request, "home.html")

