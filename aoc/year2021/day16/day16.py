from collections import deque

class Packet:
    def __init__(self, hexadecimal_string: str):
        integer = int(hexadecimal_string, 16)
        self.binary_string = format(integer, "b")

        self.version = int(self.take_as_int(3))
        self.type = int(self.take_as_int(3))

        self.literal_value = None  # type: Optional[int]

        while self.binary_string != "0" * len(self.binary_string):
            if self.type == 4:
                last_group = False
                literal_value_binary_string = ""
                while not last_group:
                    if self.take_as_string(1) == "0":
                        last_group = True
                    literal_value_binary_string += self.take_as_string(4)
                self.literal_value = int(literal_value_binary_string, 2)

    def take_as_string(self, n: int) -> str:
        string = self.binary_string[:n]
        self.binary_string = self.binary_string[n:]
        return string

    def take_as_int(self, n: int) -> int:
        return int(self.take_as_string(n), 2)






print(Packet("8").binary_string)