import utils
import save_data


def main():
    data = utils.add_new_employee()
    print(data)
    save_data.save_new_employee(data)


if __name__ == '__main__':
    main()



