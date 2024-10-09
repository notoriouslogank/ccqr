import csv


def get_data():
    machine = input("Machine: ")
    location = input("Location: ")
    return machine, location


def write_csv(csv_data):
    with open("location_list.csv", "a", newline="") as csvfile:
        writer = csv.writer(
            csvfile, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(csv_data)


write_csv(get_data())
