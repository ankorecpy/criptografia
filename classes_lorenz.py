class Gear:
	step = 3
	pin = 0
	next_pin = 0
	location = 0
	last_location = "0"
	
	def __init__(self, num_pins, init):
		self.pin = 360 / num_pins
		self.next_pin = self.pin
		self.location = (init % int(self.pin))
		self.last_location = "0"
				
	def rotate(self):
		self.location += 3
		if self.location >= self.next_pin:
			self.next_pin = (self.pin + self.next_pin) % 360
			self.last_location = "1"
			self.location = self.location % 360			
		else:			
			self.last_location = "0"

	def getpin(self):		
		return self.last_location

class CypherMachine:	
	engine_wheel_1 = None
	engine_wheel_2 = None
	chi_wheels = []
	psi_wheels = []
	
	def __init__(self, wheel_1, wheel_2, psi_wheels, chi_wheels):
		self.engine_wheel_1 = wheel_1
		self.engine_wheel_2 = wheel_2
		self.psi_wheels = psi_wheels
		self.chi_wheels = chi_wheels
		
	def _rotate_wheels(self):
		self.engine_wheel_1.rotate()
		if self.engine_wheel_1.getpin() == "1":
			self.engine_wheel_2.rotate()
		self._rotate(self.chi_wheels)
		if self.engine_wheel_2.getpin() == "1":
			self._rotate(self.psi_wheels)
		
	def _rotate(self, wheels):
		for wheel in wheels:
			wheel.rotate()
	
	def _get_first_bit(self, gears):
		bits = []
		for gear in gears:
			bits.append(gear.getpin())
		return bits		
	
	def _xor(self, bits_1, bits_2, bits_3):
		result = []
		for index in range(0, len(bits_1)):
			xor_1 = "0" if bits_1[index] == bits_2[index] else "1"
			xor_2 = "0" if xor_1 == bits_3[index] else "1"
			result.append(xor_2)
			self._rotate_wheels()
		return result
	
	def _change_bits(self, bits):
		segment = 5
		new_bits = ""
		for index in range(0, len(bits), segment):			
			psi_bits = self._get_first_bit(self.psi_wheels)
			chi_bits = self._get_first_bit(self.chi_wheels)
			code = bits[index : index + segment]
			new_code = self._xor(code, chi_bits, psi_bits)
			new_bits += (''.join(new_code))
		return new_bits
	
	def encrypt(self, text):
		coder_machine = CoderMachine()
		code = coder_machine.code(text)
		new_text = ""
		if code != -1:
			new_code = self._change_bits(code)
			new_text = coder_machine.decode(new_code)						
		return new_text
	
	def decrypt(self, text):
		coder_machine = CoderMachine()
		code = coder_machine.code(text)
		new_text = ""	
		if code != -1:
			new_code = self._change_bits(code)			
			new_text = coder_machine.decode(new_code)								
		return new_text

class CoderMachine:
	
	baudot_symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ']', '\n', ' ', "%", "[", '_']
	
	baudot_codes = ["11000", "10011", "01110", "10010", "10000", "10110", "01011", "00101", "01100", "11010", "11110", "01001", "00111", "00110", "00011", "01101", "11101", "01010", "10100", "00001", "11100", "01111", "11001", "10111", "10101", "10001", "00010", "01000", "00100", "11011", "11111", "00000"]
	
	def __init__(self):
		pass
			
	def _search_for_code(self, symbol):
		code = -1
		if symbol in self.baudot_symbols:
			index = self.baudot_symbols.index(symbol)
			code = self.baudot_codes[index]
		return code	
	
	def code(self, text):
		coded_text = ""
		for symbol in text:
			code = self._search_for_code(symbol)
			if code == -1:
				coded_text = -1
				print("ERROR: '{0}' no es permitido" .format(symbol))
				break
			coded_text += code
		return coded_text
		
	def _search_for_symbol(self, code):
		symbol = -1
		if code in self.baudot_codes:
			index = self.baudot_codes.index(code)
			symbol = self.baudot_symbols[index]
		return symbol
	
	def decode(self, code_text):
		text = ""
		code_list, segment = [], 5
		code_list.extend(code_text)
		for index in range(0, len(code_list), segment):
			code = ''.join(code_list[index : (index + segment)])
			symbol = self._search_for_symbol(code)
			if symbol == -1:
				text = symbol
				print("ERROR: '{0}' no es permitido" .format(code))
				break
			text += symbol
		return text
