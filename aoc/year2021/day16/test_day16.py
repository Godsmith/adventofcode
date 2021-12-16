from aoc.year2021.day16.day16 import PacketFactory


class TestPacket:
    def test_version(self):
        factory = PacketFactory('D2FE28')

        assert factory.create_packet().version == 6

    def test_type(self):
        factory = PacketFactory('D2FE28')

        assert factory.create_packet().type == 4

    def test_literal(self):
        factory = PacketFactory('D2FE28')

        assert factory.create_packet().literal_value == 2021

    def test_length(self):
        factory = PacketFactory('D2FE28')

        assert factory.create_packet().length == 21

    def test_subpackets_type_0(self):
        factory = PacketFactory('38006F45291200')

        assert len(factory.create_packet().subpackets) == 2

    def test_subpackets_type_1(self):
        factory = PacketFactory('EE00D40C823060')

        assert len(factory.create_packet().subpackets) == 3

    def test_value(self):
        assert PacketFactory('C200B40A82').create_packet().value == 3
        assert PacketFactory('04005AC33890').create_packet().value == 54
        assert PacketFactory('880086C3E88112').create_packet().value == 7
        assert PacketFactory('CE00C43D881120').create_packet().value == 9
        assert PacketFactory('D8005AC2A8F0').create_packet().value == 1
        assert PacketFactory('F600BC2D8F').create_packet().value == 0
        assert PacketFactory('9C005AC2F8F0').create_packet().value == 0
        assert PacketFactory('9C0141080250320F1802104A08').create_packet().value == 1

    def test_version_sum(self):
        assert PacketFactory("8A004A801A8002F478").create_packet().version_sum() == 16
        assert PacketFactory("620080001611562C8802118E34").create_packet().version_sum() == 12
        assert PacketFactory("C0015000016115A2E0802F182340").create_packet().version_sum() == 23
        assert PacketFactory("A0016C880162017C3686B18A3D4780").create_packet().version_sum() == 31

