from collections import defaultdict
from math import prod

from aocd import data
from aoc.utils import rows
import regex as re


class Tile():
    def __init__(self, id_, rows):
        self.id = id_
        self.rows = rows
        reversed_sides = [''.join(reversed(side)) for side in self.sides]
        self.possible_sides = self.sides + reversed_sides

    def __repr__(self):
        return f"{self.id}\n" + '\n'.join(self.rows)

    @property
    def sides(self):
        # sides: top, right, bottom, left
        return [self.rows[0], ''.join(row[-1] for row in self.rows),
                self.rows[-1], ''.join(row[0] for row in self.rows)]

    def rotate_so_that_unique_sides_face_top_and_left(self, tiles_from_possible_sides):
        top_is_unique = self._is_unique(self.sides[0], tiles_from_possible_sides)
        left_is_unique = self._is_unique(self.sides[3], tiles_from_possible_sides)
        while not (top_is_unique and left_is_unique):
            self.rotate()
            top_is_unique = self._is_unique(self.sides[0], tiles_from_possible_sides)
            left_is_unique = self._is_unique(self.sides[3], tiles_from_possible_sides)

    def rotate(self):
        self.rows = list(map(''.join, zip(*reversed(self.rows))))

    def flip(self):
        self.rows = [''.join(reversed(row)) for row in self.rows]

    def _is_unique(self, side, tiles_from_possible_sides):
        return len(tiles_from_possible_sides[side]) == 1

    @property
    def right_side(self):
        return self.sides[1]

    @property
    def bottom_side(self):
        return self.sides[2]

    def flip_and_rotate_so_that_side_faces_left(self, side):
        self._flip_and_rotate_so_that_side_faces_index(side, 3)

    def flip_and_rotate_so_that_side_faces_top(self, side):
        self._flip_and_rotate_so_that_side_faces_index(side, 0)

    def _flip_and_rotate_so_that_side_faces_index(self, side, index):
        if self._rotate_so_that_side_faces_index(side, index):
            return
        self.flip()
        self._rotate_so_that_side_faces_index(side, index)

    def _rotate_so_that_side_faces_index(self, side, index):
        for _ in range(4):
            if self.sides[index] == side:
                return True
            self.rotate()

    @property
    def image_without_borders(self):
        for row in self.rows[1:-1]:
            yield row[1:-1]


class Image():
    def __init__(self, data, image_height):
        self.image_height = image_height
        self.tiles = self._get_tiles(data)
        self.tiles_from_possible_sides = self._get_tiles_from_possible_sides()
        self.all_sides = list(self._get_all_sides())
        self.image_matrix = self._create_image_matrix()

    def _get_tiles(self, rows):
        tiles = {}
        current_rows = []
        for row in rows:
            if "Tile" in row:
                id_ = re.findall(r"\d+", row)[0]
            elif row == "":
                tiles[int(id_)] = Tile(int(id_), current_rows)
                current_rows = []
            else:
                current_rows += [row]
        tiles[int(id_)] = Tile(int(id_), current_rows)
        return tiles

    def _get_tiles_from_possible_sides(self):
        tiles_from_possible_sides = defaultdict(list)
        for id_, tile in self.tiles.items():
            for side in tile.possible_sides:
                tiles_from_possible_sides[side].append(tile)
        return tiles_from_possible_sides

    def _get_all_sides(self):
        for tile in self.tiles.values():
            yield from tile.sides

    @property
    def _first_corner(self):
        for tile in self.tiles.values():
            outside_edge_count = 0
            for side in tile.sides:
                if self.all_sides.count(side) == 1 and self.all_sides.count(
                        ''.join(reversed(side))) == 0:
                    outside_edge_count += 1
            if outside_edge_count == 2:
                return tile

    def _get_tile_with_side(self, side, not_this_tile) -> Tile:
        return [tile for tile in self.tiles_from_possible_sides[side] if
                 tile != not_this_tile][0]

    def _create_image_matrix(self):
        # Fix first row
        tile = self._first_corner
        image_matrix = {(0, 0): tile}
        tile.rotate_so_that_unique_sides_face_top_and_left(
            self.tiles_from_possible_sides)
        for column in range(1, self.image_height):
            side = tile.right_side
            tile = self._get_tile_with_side(side, tile)
            tile.flip_and_rotate_so_that_side_faces_left(side)
            image_matrix[(0, column)] = tile

        # Fix following rows
        for row in range(1, self.image_height):
            for column in range(self.image_height):
                tile_above = image_matrix[(row - 1, column)]
                side = tile_above.bottom_side
                new_tile = self._get_tile_with_side(side, tile_above)
                new_tile.flip_and_rotate_so_that_side_faces_top(side)
                image_matrix[(row, column)] = new_tile

        return image_matrix

    @property
    def corner_product(self):
        return prod(self.image_matrix[(x, y)].id
                    for x in (0, self.image_height - 1)
                    for y in (0, self.image_height - 1))

    @property
    def image_without_borders(self):
        image_rows = []
        for row in range(self.image_height):
            for image_row in range(8):
                image_row_parts = []
                for column in range(self.image_height):
                    image_row_parts.append(
                        list(self.image_matrix[(row, column)].image_without_borders)[
                            image_row])
                image_rows.append(''.join(image_row_parts))
        return '\n'.join(image_rows)

    @property
    def count_sea_monsters(self):
        padding_length = str(self.image_height * 8 - 20 + 1)
        pattern_string = r"..................#..{" + padding_length + \
                         r"}#....##....##....###.{" + padding_length + \
                         r"}.#..#..#..#..#..#..."
        pattern = re.compile(pattern_string, re.MULTILINE + re.DOTALL)
        if sea_monster_count := self._count_matches_for_all_rotations(pattern) > 0:
            return sea_monster_count
        self._flip_image_matrix()
        return self._count_matches_for_all_rotations(pattern)

    def _count_matches_for_all_rotations(self, pattern):
        for _ in range(4):
            count = len(
                re.findall(pattern, self.image_without_borders, overlapped=True))
            if count > 0:
                return count
            self._rotate_image_matrix()
        return 0

    def _rotate_image_matrix(self):
        new_image_matrix = {}
        for x in range(self.image_height):
            for y in range(self.image_height):
                new_image_matrix[(x, y)] = self.image_matrix[
                    (self.image_height - y - 1, x)]
        self.image_matrix = new_image_matrix
        for tile in self.image_matrix.values():
            tile.rotate()

    def _flip_image_matrix(self):
        new_image_matrix = {}
        for x in range(self.image_height):
            for y in range(self.image_height):
                new_image_matrix[(x, y)] = self.image_matrix[
                    (x, self.image_height - y - 1)]
        self.image_matrix = new_image_matrix
        for tile in self.image_matrix.values():
            tile.flip()

    @property
    def water_roughness(self):
        sea_monster_count = self.count_sea_monsters
        sea_monster_characters = 15 * sea_monster_count
        total_hash_symbols = self.image_without_borders.count("#")
        return total_hash_symbols - sea_monster_characters


print(Image(rows(data), 12).corner_product)
print(Image(rows(data), 12).water_roughness)
