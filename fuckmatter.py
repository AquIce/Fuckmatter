'''
 > Fuckmatter is a Brainfuck formatter
 > Code by @SinisterIcy
'''

# Get the input file
file = input('BrainFuck file: ')

# System variables (do not edit)
ctnt = ''
indent_level = 0
buffer = ''
final = ''

# Indent char (can be replaced with spaces for example)
indent_char = '\t'

# Get the content of the input file
with open(file, 'r') as f:
	ctnt = f.read().replace(' ', '').replace(indent_char, '').replace('\n', '')
	
# Initialize the char buffer to the first character
chbuffer = ctnt[0]

# Iterate through the content
for i in ctnt:
	if i == '[':
		final += indent_char * indent_level + buffer + '\n' + indent_char * indent_level + '['
		indent_level += 1
		buffer = ''
	elif i == ']':
		final += indent_char * indent_level + buffer + '\n' + indent_char * indent_level + ']'
		indent_level -= 1
		buffer = ''
	elif chbuffer != i:
		buffer += '\n' + indent_char * indent_level + i
	else:
		buffer += i
	chbuffer = i

# Write the result in the file
with open(file, 'w') as f:
	f.write(final)
