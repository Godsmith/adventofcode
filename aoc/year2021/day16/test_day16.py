from aoc.year2021.day16.day16 import PacketFactory


class TestPacket:
    def test_version(self):
        packet = PacketFactory('D2FE28')

        assert packet.create_packet().version == 6

    def test_type(self):
        packet = PacketFactory('D2FE28')

        assert packet.create_packet().type == 4

    def test_literal(self):
        packet = PacketFactory('D2FE28')

        assert packet.create_packet().literal_value == 2021

    def test_operator_length_type_0(self):
        packet = PacketFactory('38006F45291200')

        assert len(packet.create_packet().subpackets) == 2
