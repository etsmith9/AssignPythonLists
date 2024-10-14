#task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

#if "Alice" in submitted and attended:
#    print("Alice is a good student")  #long way

print("Alice is a good student") if "Alice" in submitted and attended else print("Alice needs to step up her game")
 #all in one line ^^
