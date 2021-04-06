import csv
from collections import Counter

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#remove header from data
file_data.pop(0)

total_weight = 0
total_people = len(file_data)
final_data = []

for i in file_data:
    total_weight += float(i[2])
    final_data.append(float(i[2]))

final_data.sort()

def mean(total_weight, total_people):
    mean = total_weight/total_people
    print(f"The Mean/Avg is -> {mean:.2f}")

def median(total_people, final_data):
    if total_people%2==0:
        median1 = float(final_data[total_people//2])
        median2 = float(final_data[total_people//2-1])
        median = (median1 + median2)/2
    else:
        median = final_data[total_people//2]
    print(f"The Median is -> {median:.2f}")

def mode(final_data):
    data = Counter(final_data)
    mode_data_for_range = {
        '75-85':0,
        '85-95':0,
        '95-105':0,
        '105-115':0,
        '115-125':0,
        '125-135':0,
        '135-145':0,
        '145-155':0,
        '155-165':0,
        '165-175':0,
    }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            mode_data_for_range["75-85"] += occurence
        elif 85 < weight < 95:
            mode_data_for_range["85-95"] += occurence
        elif 95 < weight < 105:
            mode_data_for_range["95-105"] += occurence
        elif 105 < weight < 115:
            mode_data_for_range["105-115"] += occurence
        elif 115 < weight < 125:
            mode_data_for_range["115-125"] += occurence
        elif 125 < weight < 135:
            mode_data_for_range["125-135"] += occurence
        elif 135 < weight < 145:
            mode_data_for_range["135-145"] += occurence
        elif 145 < weight < 155:
            mode_data_for_range["145-155"] += occurence
        elif 155 < weight < 165:
            mode_data_for_range["155-165"] += occurence
        elif 165 < weight < 175:
            mode_data_for_range["165-175"] += occurence

    mode_range, mode_occurrence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurrence:
            mode_range, mode_occurrence = [int(range.split('-')[0]), int(range.split('-')[1])], occurence
    mode = float((mode_range[0]+mode_range[1])/2)
    print(f"The Mode is -> {mode:.2f}")

mean(total_weight, total_people)
median(total_people, final_data)
mode(final_data)

