from collections import defaultdict, Counter
from math import prod

from aocd import data
from aoc.utils import rows
import re


class Tile():
    # sides: top, right, bottom, left
    def __init__(self, id_, rows):
        self.id = id_
        self.rows = rows
        reversed_sides = [''.join(reversed(side)) for side in self.sides]
        self.possible_sides = self.sides + reversed_sides

    def __repr__(self):
        return f"{self.id}\n" + '\n'.join(self.rows)

    @property
    def sides(self):
        return [self.rows[0],
                ''.join(row[-1] for row in self.rows),
                self.rows[-1],
                ''.join(row[0] for row in self.rows)]

    def rotate_so_that_unique_sides_face_top_and_left(self, tiles_from_possible_sides):
        top_is_unique = self._is_unique(self.sides[0], tiles_from_possible_sides)
        left_is_unique = self._is_unique(self.sides[3], tiles_from_possible_sides)
        while not (top_is_unique and left_is_unique):
            self._rotate()
            top_is_unique = self._is_unique(self.sides[0], tiles_from_possible_sides)
            left_is_unique = self._is_unique(self.sides[3], tiles_from_possible_sides)

    def _rotate(self):
        self.rows = list(map(''.join, zip(*reversed(self.rows))))

    def _flip(self):
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
        if self.id == 2423:
            self.id = self.id
        rotate_count = 0
        while rotate_count < 4:
            if self.sides[index] == side:
                return
            self._rotate()
            rotate_count += 1
        self._flip()
        rotate_count = 0
        while rotate_count < 4:
            if self.sides[index] == side:
                return
            self._rotate()
            rotate_count += 1
        assert False, "No match for tile!"


class Image():
    def __init__(self, data, image_height):
        self.image_height = image_height
        self.tiles = self._get_tiles(data)
        self.tiles_from_possible_sides = self._get_tiles_from_possible_sides()
        self.all_sides = list(self._get_all_sides())
        self.corners, self.edges = self._get_corners_and_edges()

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

    def _get_corners_and_edges(self):
        corners = []
        edges = []
        for tile in self.tiles.values():
            outside_edge_count = 0
            for side in tile.sides:
                if self.all_sides.count(side) == 1 and self.all_sides.count(
                        ''.join(reversed(side))) == 0:
                    outside_edge_count += 1
            if outside_edge_count == 1:
                edges.append(tile)
            elif outside_edge_count == 2:
                corners.append(tile)
        return corners, edges

    def _get_tile_with_side(self, side, not_this_tile) -> Tile:
        tiles = [tile for tile in self.tiles_from_possible_sides[side] if
                 tile != not_this_tile]
        if len(tiles) == 0:
            tiles = tiles
        assert len(tiles) == 1
        return tiles[0]

    def get_corner_product(self):

        # Fix first row
        image_matrix = {(0, 0): self.corners[0]}
        self.corners[0].rotate_so_that_unique_sides_face_top_and_left(
            self.tiles_from_possible_sides)
        tile = self.corners[0]
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

        return prod(image_matrix[(x, y)].id
                    for x in (0, self.image_height - 1)
                    for y in (0, self.image_height - 1))

print(Image(rows(data), 12).get_corner_product())
