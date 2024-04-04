import json
import re

def read_data_from_vcf_file(vcf_file):
    with open(vcf_file, 'r') as file:
        vcf_data = file.readlines()

    phone_numbers = []

    for line in vcf_data:
        match = re.search(r'TEL;CELL:(\+\d+)', line)
        if match:
            phone_numbers.append(match.group(1))

    return phone_numbers


def read_data_from_txt_file(txt_file):
    data_list = []

    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                data_list.append(line.strip())
    except FileNotFoundError:
        print("File does not exist or the path is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list


def read_data_from_json_file(json_file):
    name_list = []

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            if 'friends_v2' in json_data:
                name_list = [person['name'].encode('iso-8859-1').decode('utf-8') for person in json_data['friends_v2']]
            else:
                print("Friends list not found in the JSON file.")
    except FileNotFoundError:
        print("JSON file does not exist or the path is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return name_list


def find_friends_json(txt_file, name_list, city_list=None):
    data_list = []

    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                if len(line.strip().split(',')) >= 11:
                    data = line.strip().split(',')
                    name = f"{data[2].strip()} {data[3].strip()}"
                    if city_list is None or any(item.strip() in city_list for item in data):
                        if name in name_list:
                            data_list.append(line.strip())
    except FileNotFoundError:
        print("File does not exist or the path is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list


def find_friends_vcf(txt_file, phone_list):
    data_list = []

    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                phone_number = data[-1].strip()
                if (phone_number or '+48' + phone_number) in phone_list:
                    data_list.append(line.strip())
    except FileNotFoundError:
        print("File does not exist or the path is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list


def find_user_by_name_and_surname(txt_file, full_name):
    data_list = []

    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.split(',')
                name = data[2].strip()
                surname = data[3].strip()
                if full_name.lower() in (name.lower() + ' ' + surname.lower()):
                    data_list.append(line.strip())
    except FileNotFoundError:
        print("File does not exist or the path is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list


def find_user_by_phone_number(txt_file, phone_number):
    data_list = []

    try:
        with open(txt_file, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.split(',')
                phone = data[-1].strip()
                if phone_number.strip() == phone:
                    data_list.append(line.strip())
    except FileNotFoundError:
        print("File does not exist or the path is incorrect.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data_list
