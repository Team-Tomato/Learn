import csv
with open('C:\\Users\\praji\\Desktop\\senior\\haha.txt') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')

    for line in csv_reader:
        print(line)

    with open('C:\\Users\\praji\\Desktop\\senior\\haha_new.txt',mode='a') as new_csv_file:
        csv_writer = csv.writer(new_csv_file,delimiter="," ,quotechar='"' ,quoting=csv.QUOTE_MINIMAL)

        for line in csv_reader:
            csv_writer.writerow(line)
