from aoc.year2021.day16.day16 import Packet


class TestPacket:
    def test_version(self):
        packet = Packet('D2FE28')

        assert packet.version == 6

    def test_type(self):
        packet = Packet('D2FE28')

        assert packet.type == 4

    def test_literal(self):
        packet = Packet('D2FE28')

        assert packet.literal_value == 2021
