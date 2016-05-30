import os

x = 1

os.system('clear')
print('Welcome to the database record splitter utility') 
print ('Here are the files in the current directory:')
print ('\n')
os.system('ls')
print ('\n')

in_file_name = input('Enter an input file name: ')
out_file_name = input('Enter a file name for saved results: ')

file = open(in_file_name, 'r', errors = 'ignore')
count = 0
for line in file:
	count += 1
file.close()

os.system('clear')
print ('The number of lines or records in ' + in_file_name + ' is: ' + str(count))

start = int(input('Enter a start record: '))
end = int(input('Enter an end record: '))


file = open(in_file_name, 'r', errors = 'ignore')
f = open(out_file_name, 'w', errors = 'ignore')

for line in file:
	if x >= start and x <= end:
		f.write(line)
	x += 1
file.close()
f.close()		

print ('Your selected records have been printed to ' + out_file_name)
choice = input('Enter v to view the new file or just enter to quit: ')
if choice == 'v':
	os.system ('nano ' +  out_file_name)
