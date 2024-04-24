from src.util import TreeNode


def count_paths(root, target_sum):
    return count_paths_prefix_sum(root, target_sum, {}, 0)


def count_paths_prefix_sum(current_node: TreeNode, target_sum, path_map, current_path_sum):
    if current_node is None:
        return 0

    path_count = 0
    current_path_sum += current_node.val

    # Check if current path sum equals target sum
    if current_path_sum == target_sum:
        path_count += 1

    # Add the number of paths that end at this node and sum to the target
    path_count += path_map.get(current_path_sum - target_sum, 0)

    # Update the path_map with the current path sum
    path_map[current_path_sum] = path_map.get(current_path_sum, 0) + 1

    # Recurse down to the left and right children
    path_count += count_paths_prefix_sum(current_node.left, target_sum, path_map, current_path_sum)
    path_count += count_paths_prefix_sum(current_node.right, target_sum, path_map, current_path_sum)

    # After returning from recursion, decrement the count of the current path sum in the map
    path_map[current_path_sum] = path_map.get(current_path_sum, 1) - 1

    return path_count
