import argparse
from bigtree import Node, find_path, print_tree, findall, find_attr


def parse(filename):
    """Parse input."""

    root = Node("/", file_type="dir")
    current_node = root
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip()
            if line.startswith("$"):
                _, cmd, *cmd_args = line.split()
                if cmd == "cd":
                    new_dir = cmd_args[0]
                    if new_dir == "..":
                        current_node = current_node.parent
                    elif new_dir == "/":
                        current_node = root
                    else:
                        current_node = find_path(root, f"{current_node.path_name}/{new_dir}")
            else:
                attr, name = line.split()
                if attr == "dir":
                    Node(name, file_type=attr, parent=current_node)
                else:
                    Node(name, file_type="file", file_size=attr, parent=current_node)
    return root


def part1(puzzle_data):
    """Solve part 1."""
    total_size_to_delete = 0
    for d in findall(puzzle_data, lambda node: node.file_type=="dir"):
        directory_size = get_directory_size(d)
        if directory_size <= 100000:
            total_size_to_delete += directory_size

    return total_size_to_delete


def part2(puzzle_data):
    """Solve part 2."""
    disk_available_space = 70000000
    space_needed_for_update = 30000000
    remaining_space = disk_available_space - get_directory_size(puzzle_data)
    dir_size_to_delete = space_needed_for_update - remaining_space

    dir_sizes = []
    for d in findall(puzzle_data, lambda node: node.file_type=="dir"):
        directory_size = get_directory_size(d)
        if directory_size >= dir_size_to_delete:
            dir_sizes.append(directory_size)

    return min(dir_sizes)


def get_directory_size(directory):
    directory_size = sum(int(node.file_size) for node in directory.children if node.file_type == "file")
    directory_size += sum(get_directory_size(node) for node in directory.children if node.file_type == "dir")

    return directory_size


def solve(filename):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tuning Trouble")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
