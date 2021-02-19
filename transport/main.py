import argparse
from magic_functions import main, save_to_server

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('url', action='store', type=str, help='Url which save cards')
	args = parser.parse_args()

	key="lose something?"
	while True:
		req=main(key)
		if req != False:
			save_to_server(args.url, req)
