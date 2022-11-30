def main():
    buff = [1,2,3]
    print(list(zip(buff,map(lambda x:pow(x,2),buff))))
    print(list(map(lambda x:(x,pow(x,2)),buff)))
    print(list(zip(buff,[pow(x,2) for x in buff])))
    print([(x,pow(x,2)) for x in buff])
if __name__ == '__main__':
    main()
