
def main(name=None):
	if name is None:
		return "Hello, World!"
	else:
		return f"Hello, {name}!"

def say_hello():
	return "Hola Mundo!"
	
if __name__ == '__main__':
	say_hello()