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

    def test_length(self):
        packet = PacketFactory('D2FE28')

        assert packet.create_packet().length == 21

    def test_subpackets_type_0(self):
        packet = PacketFactory('38006F45291200')

        assert len(packet.create_packet().subpackets) == 2

    def test_subpackets_type_1(self):
        packet = PacketFactory('EE00D40C823060')

        assert len(packet.create_packet().subpackets) == 3

class TestPacketFactory:
    def test_version_sum(self):
        assert PacketFactory("8A004A801A8002F478").version_sum() == 16
        assert PacketFactory("620080001611562C8802118E34").version_sum() == 12
        assert PacketFactory("C0015000016115A2E0802F182340").version_sum() == 23
        assert PacketFactory("A0016C880162017C3686B18A3D4780").version_sum() == 31
