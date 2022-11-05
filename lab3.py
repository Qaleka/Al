from lab_python_fp import field,gen_random,unique,sort,print_result,cm_timer,process_data

def main():
    while True:
        print('Введите номер задания(От 1  до 7). Если хотите завершить программу,введите 0: ')
        buff = input()
        match int(buff):
            case 0:
                break
            case 1:
                field.main()
            case 2:
                gen_random.main()
            case 3:
                unique.main()
            case 4:
                sort.main()
            case 5:
                print_result.main()
            case 6:
                cm_timer.main()
            case 7:
                process_data.main()


if __name__ == '__main__':
    main()
