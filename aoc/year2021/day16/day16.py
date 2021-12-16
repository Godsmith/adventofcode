from collections import deque


class Packet:
    def __init__(self, version, type_):
        self.version = version
        self.type = type_
        self.literal_value = None  # type: Optional[int]
        self.subpackets = []


class PacketFactory:
    def __init__(self, hexadecimal_string: str):
        integer = int(hexadecimal_string, 16)
        number_of_bits = len(hexadecimal_string) * 4
        self.binary_string = format(integer, f"0{number_of_bits}b")

    def create_packets_until_end(self):
        packets = []
        while self.binary_string != "0" * len(self.binary_string):
            packets.append(self.create_packet())
        return packets

    def create_packets_with_total_length(self, length: int):
        packets = []
        while sum(packet.length for packet in packets) < length:
            packets.append(self.create_packet())
        return packets

    def create_packet(self):
        packet = Packet(version=self.take_as_int(3), type_=self.take_as_int(3))

        if packet.type == 4:
            last_group = False
            literal_value_binary_string = ""
            while not last_group:
                if self.take_as_binary_string(1) == "0":
                    last_group = True
                literal_value_binary_string += self.take_as_binary_string(4)
            packet.literal_value = int(literal_value_binary_string, 2)
        else:
            if self.take_as_binary_string(1) == "0":
                total_length_of_subpackets = self.take_as_int(15)
                packet.subpackets = self.create_packets_with_total_length(total_length_of_subpackets)
        return packet

    def take_as_binary_string(self, n: int) -> str:
        string = self.binary_string[:n]
        self.binary_string = self.binary_string[n:]
        return string

    def take_as_int(self, n: int) -> int:
        return int(self.take_as_binary_string(n), 2)

    def take_as_hexadecimal_string(self, n: int) -> str:
        return format(self.take_as_int(n), "X")
