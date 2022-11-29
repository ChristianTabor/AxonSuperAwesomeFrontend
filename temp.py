import json
import objectpath

if __name__ == '__main__':
    f = "C:/Users/Christian Tabor/PycharmProjects/AxonSuperAwesomeFrontend/dist/result.txt"
    tree_obj = objectpath.Tree(json.load(open(f, 'r', encoding="utf8")))
    iterator = tree_obj.execute('$..Text')
    result = ''
    for auto in iterator:
        result += auto
    print(result)
    input("Press Enter To Close")
