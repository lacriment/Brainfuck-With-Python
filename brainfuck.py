code = input("write or paste your code here:\n")
commands = [x for x in code if x in "<>+-,.[]"]
pointer = step = stepback = 0
tape = [0] * 30
while step < len(commands):
	command = commands[step]
	if command == "<":
		pointer -= 1
	elif command == ">":
		pointer += 1
	elif command == "+":
		tape[pointer] += 1
	elif command == "-":
		if tape[pointer] > 0:
			tape[pointer] -= 1
	elif command == ",":
		tape[pointer] = ord(input("Input : "))
	elif command == ".":
		print(chr(tape[pointer]))
	elif command == "[":
		stepback = step
	elif command == "]":
		if tape[pointer] > 0:
			step = stepback - 1
	step += 1
print(tape)
