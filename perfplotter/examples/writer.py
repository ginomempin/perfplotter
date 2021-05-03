import csv


def create_csv(filepath, data):
    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in data:
            csvwriter.writerow(row)
