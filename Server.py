from http.server import HTTPServer
from HTTPRequestHandler import HTTPRequestHandler
class Server:


	def start(server_class=HTTPServer, handler_class=HTTPRequestHandler):		
		server_address = ('', 8001)
		httpd=server_class(server_address,handler_class)
		print("Server is running.")
		print("Crt+C for close.")
		try:
			httpd.serve_forever()
		except KeyboardInterrupt:
			pass
			print("Server Stops.")
		httpd.server_close()
