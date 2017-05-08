import BaseHTTPServer

server_port = 9000


def run(server_class=BaseHTTPServer.HTTPServer,
		handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
	server_address = ('', server_port)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()


class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

	# for GET requests...
	def do_GET(self):
		self.send_response(200)

#		self.send_header("Content-type", type)
#		self.end_headers()
#		self.wfile.write("Helloooo!!!")
#		self.wfile.close()



                self.send_header('Content-type', 'image/jpeg')
		self.end_headers()
                fileObj = open("WhimLogo.png","rb")
                image = fileObj.read()
                self.wfile.write(image)
		self.wfile.close()




		pass
		

	# for POST requests...
	def do_POST(self):
		# do whatever...
		pass


def main():
	run(handler_class=MyHTTPRequestHandler)


if __name__ == '__main__':
	main()
