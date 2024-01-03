from aocd import data


def get_hash(s: str):
    current_value = 0
    for char in s:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


print(sum(get_hash(s) for s in data.split(",")))


def get_boxes(sequence: str):
    boxes = [[] for _ in range(256)]
    for s in sequence.split(","):
        if "-" in s:
            label = s[:-1]
        else:
            label = s[:-2]
        box_nr = get_hash(label)
        if "-" in s:
            boxes[box_nr] = [lens for lens in boxes[box_nr] if label not in lens]
        else:
            focal_length = int(s[-1])
            for lens in boxes[box_nr]:
                if label in lens:
                    lens[label] = focal_length
                    break
            else:
                boxes[box_nr].append({label: focal_length})
    return boxes


def power(boxes):
    total_power = 0
    for box_nr, box in enumerate(boxes):
        for slot_number, lens in enumerate(box, 1):
            total_power += (box_nr + 1) * slot_number * list(lens.values())[0]
    return total_power


# boxes = get_boxes("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")

boxes = get_boxes(data)

print(power(boxes))
