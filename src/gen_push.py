import sys

USAGE = sys.argv[0] + " <items> - number of parameters required"

def main():
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)

    items = sys.argv[1]
    values = "0123456789"

    result = "("
    for i in range(0,int(items)):
        data_item = i%len(values)
        result +=  values[data_item:data_item+1] + ","

    if len(result) > 1:
        result = result[:-1]
    result += ")"

    print(result)

if __name__ == '__main__':
    main()
