import sys

def exhaust_memory():
    try:
        memory_hog = []
        while True:
         
            memory_hog.extend(range(1000000))
            print(f"Memory usage: {sys.getsizeof(memory_hog)} bytes")
    except MemoryError:
        print("Memory exhausted!")

if __name__ == "__main__":
    exhaust_memory()
