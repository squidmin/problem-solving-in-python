import hashlib
import bisect


def hash_function(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16)


class ConsistentHashRing:
    def __init__(self, num_nodes=1):
        self.num_nodes = num_nodes
        self.nodes = {}
        self.sorted_keys = []

    def add_node(self, node_name):
        """Add a new node to the hash ring."""
        node_hash = hash_function(node_name)
        if node_hash not in self.nodes:
            self.nodes[node_hash] = node_name
            bisect.insort(self.sorted_keys, node_hash)

    def remove_node(self, node_name):
        """Remove a node from the hash ring."""
        node_hash = hash_function(node_name)
        if node_hash in self.nodes:
            self.nodes.pop(node_hash)
            self.sorted_keys.remove(node_hash)

    def get_node(self, key):
        """Get the node responsible for the given key."""
        if not self.sorted_keys:
            return None
        key_hash = hash_function(key)
        index = bisect.bisect(self.sorted_keys, key_hash) % len(self.sorted_keys)
        return self.nodes[self.sorted_keys[index]]


# Create a hash ring
ring = ConsistentHashRing(num_nodes=3)

# Add nodes
ring.add_node("Node1")
ring.add_node("Node2")
ring.add_node("Node3")

# Get the node for a key
node = ring.get_node("my_key")
print(f"Key 'my_key' is mapped to node: {node}")
