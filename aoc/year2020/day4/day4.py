from aocd import data
import re

REQUIRED_FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def passports():
    passport_strings = data.split("\n\n")
    for passport_string in passport_strings:
        passport = {}
        key_value_strings = passport_string.split()
        for key_value_string in key_value_strings:
            key, value = key_value_string.split(":")
            passport[key] = value
        yield passport


def is_valid(passport):
    for field in REQUIRED_FIELDS:
        if not field in passport:
            return False
    return True


def is_valid2(passport):
    regexes = (('byr', '^\d{4}$'),
               ('iyr', '^\d{4}$'),
               ('eyr', '^\d{4}$'),
               ('hgt', '^\d*(cm|in)$'),
               ('hcl', '^#[0-9a-f]{6}$'),
               ('ecl', '^(amb|blu|brn|gry|grn|hzl|oth)$'),
               ('pid', '^\d{9}$'))
    try:
        results = [re.match(pattern, passport[field]) is not None for field, pattern in
                   regexes]
        results.append(1920 <= int(passport['byr']) <= 2002)
        results.append(2010 <= int(passport['iyr']) <= 2020)
        results.append(2020 <= int(passport['eyr']) <= 2030)
        if 'cm' in passport['hgt']:
            min_hgt = 150
            max_hgt = 193
        else:
            min_hgt = 59
            max_hgt = 76
        results.append(min_hgt <= int(passport['hgt'][:-2]) <= max_hgt)
    except (KeyError, ValueError):
        return False
    return all(results)

print(sum(map(is_valid, passports())))
print(sum(map(is_valid2, passports())))
