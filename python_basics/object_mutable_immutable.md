
# Concepts of objects in Python, focusing on mutability and immutability. Here are the key points:
- Data Types: Python categorizes data as numbers or strings, and understanding how to manipulate this data is essential.
- Everything is an Object: In Python, everything is considered an object, which has three main properties: identity, type, and value.
- Mutability: The lecture defines mutable objects (which can be changed) versus immutable objects (which cannot be altered once created).
- Object Identity: It’s emphasized that one should check the identity of an object to determine mutability, rather than making assumptions based on value.
Examples: Numbers in Python are immutable. For instance, changing a variable representing a number results in a new object rather than modifying the original.

- Mutable Objects: Mutable objects, like sets, can be modified without changing their identity, allowing for more flexibility.
- Conclusion: Understanding the distinction between mutable and immutable objects is critical for effective programming in Python.


## 3 features of objects in python
- Identity: Each object in Python has a unique identity, which can be checked using the id() function. This identity distinguishes the object from all other objects in memory. Even if two objects have the same value, their identities can differ.
- Type: Every object has a type, which determines what operations can be performed on it. Python has various built-in types such as integers, strings, lists, and sets. Understanding the type of an object is crucial for effective manipulation in programming.
- Value: This refers to the data contained within the object. For mutable objects, the value can change without altering the identity of the object, while for immutable objects, the value cannot be changed once it is created. For example, modifying a number results in a new object rather than changing the original one.
