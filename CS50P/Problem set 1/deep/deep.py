
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().strip()
answer_box = ["42","forty-two","forty two"]

print("Yes") if answer in answer_box else print("No")