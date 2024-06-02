# Comparison of List, Tuple, Set, and Map in Python

| Property       | List             | Tuple            | Set              | Map (Dictionary)  |
| -------------- | ---------------- | ---------------- | ---------------- | ----------------- |
| **Mutable**    | Yes              | No               | Yes              | Yes               |
| **Ordered**    | Yes              | Yes              | No               | Yes (Python 3.7+) |
| **Indexed**    | Yes              | Yes              | No               | No                |
| **Duplicate Values** | Yes        | Yes              | No               | Yes (Values) No (Keys)      |

### Explanation of Properties

- **Mutable**: Indicates whether the data structure can be modified after creation.
  - **List**: Elements can be changed, added, or removed.
  - **Tuple**: Immutable; elements cannot be changed after creation.
  - **Set**: Elements can be added or removed, but they must be unique.
  - **Map (Dictionary)**: Key-value pairs can be changed, added, or removed.

- **Ordered**: Indicates whether the elements maintain a specific order.
  - **List**: Maintains order of elements.
  - **Tuple**: Maintains order of elements.
  - **Set**: Does not maintain any order.
  - **Map (Dictionary)**: Maintains insertion order from Python 3.7 onwards.

- **Indexed**: Indicates whether elements can be accessed by a numerical index.
  - **List**: Elements are accessible by numerical index.
  - **Tuple**: Elements are accessible by numerical index.
  - **Set**: Elements are not accessible by index; can only iterate over elements.
  - **Map (Dictionary)**: Elements are accessed by keys, not numerical index.

- **Duplicate Values**: Indicates whether the data structure allows duplicate elements.
  - **List**: Allows duplicate values.
  - **Tuple**: Allows duplicate values.
  - **Set**: Does not allow duplicate values.
  - **Map (Dictionary)**: Allows duplicate values but not duplicate keys.
