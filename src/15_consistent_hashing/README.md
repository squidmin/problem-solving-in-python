# Consistent Hashing

## Introduction

Consistent Hashing is a distributed hashing scheme that operates independently of the number of servers or objects in a distributed hash table by assigning them a position on an abstract circle, or hash ring.
This document provides a Python implementation of the Consistent Hashing algorithm, widely used in horizontal partitioning and load balancing.

## Implementation

### 1. Import necessary libraries

```python
import hashlib
import bisect
```

### 2. Define the hash function

```python
def hash_function(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16)
```

### 3. Create the `ConsistentHashRing` class

```python
class ConsistentHashRing:

    def __init__(self, num_nodes=1):
        self.num_nodes = num_nodes
        self.nodes = {}
        self.sorted_keys = []

    def add_node(self, node_name):
        # Implementation details...
    
    def remove_node(self, node_name):
        # Implementation details...
    
    def get_node(self, key):
        # Implementation details...
```

### 4. Add and remove nodes

The `add_node` and `remove_node` methods manage the nodes in the hash ring.

### 5. Locate the Node for a given key

The `get_node` method determines the appropriate node for a given key.

#### Example usage

```python
# Create a hash ring
ring = ConsistentHashRing(num_nodes=3)

# Add nodes
ring.add_node("Node1")
ring.add_node("Node2")
ring.add_node("Node3")

# Get the node for a key
node = ring.get_node("my_key")
print(f"Key 'my_key' is mapped to node: {node}")
```

### 6. Complete implementation

```python
import hashlib
import bisect

def hash_function(key):
    """Generate a hash for a given key using MD5."""
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

# Example Usage
ring = ConsistentHashRing(num_nodes=3)
ring.add_node("Node1")
ring.add_node("Node2")
ring.add_node("Node3")

node = ring.get_node("my_key")
print(f"Key 'my_key' is mapped to node: {node}")
```

#### Explanation

- `hash_function`: This function generates a hash for a given key using the MD5 algorithm. The hash is then converted to an integer for use in the hash ring.
- `add_node`: This method adds a new node to the hash ring. It calculates the hash for the node name, then inserts it into the sorted list of keys (`sorted_keys`) to maintain the order. The node's hash and name are also stored in the nodes dictionary.
- `remove_node`: This method removes a node from the hash ring. It finds the node's hash and removes it from both the `sorted_keys` list and the nodes dictionary.
- `get_node`: This method returns the node responsible for a given key. It calculates the hash of the key and uses the bisect algorithm to find the nearest node in the sorted list of keys. If the hash ring is empty (i.e., no nodes), it returns None.

### Conclusion

This Python implementation of Consistent Hashing demonstrates the core principles of the algorithm.
It can be expanded for more complex scenarios and customized for specific requirements.
