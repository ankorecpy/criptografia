import sys, file_mang
from classes_lorenz import CoderMachine, CypherMachine, Gear

WHEELS_NUMBER = 12

def _create_gears(configs):
	gears = []
	for line in configs:
		aux = line.split(";")
		if len(line) > 0 and len(aux) == 2:
			num_pins = int(aux[0])
			aux[1].replace('\n','')
			init = int(aux[1])
			gears.append(Gear(num_pins, init))
	return gears

def encrypt(lines, path_config):
	configs = file_mang.getLinesFile(path_config)
	gears = _create_gears(configs)
	ciphered_lines = []
	if len(gears) == WHEELS_NUMBER:
		cypherMachine = CypherMachine(gears[0], gears[1], gears[2:7], gears[7:12])
		for line in lines:
			ciphered_text = cypherMachine.encrypt(line)
			ciphered_lines.append(ciphered_text)
	return ciphered_lines
			
def decrypt(lines, path_config):
	configs = file_mang.getLinesFile(path_config)
	gears = _create_gears(configs)
	deciphered_lines = []
	if len(gears) == WHEELS_NUMBER:
		cypherMachine = CypherMachine(gears[0], gears[1], gears[2:7], gears[7:12])
		for line in lines:
			deciphered_text = cypherMachine.decrypt(line)
			deciphered_lines.append(deciphered_text)
	return deciphered_lines
