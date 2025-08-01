from http.server import BaseHTTPRequestHandler, HTTPServer

# Patterns to detect Spring4Shell-style attacks
malicious_keywords = [
    "class.module.classLoader.resources.context.parent.pipeline.first",
    "pattern=",
    "suffix=",
    "prefix=",
    "directory=",
    "suffix=%>//",
    "c1=Runtime",
    "c2=<%",
]

class FirewallHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode()

        # Combine headers and body into one string for scanning
        scan_content = post_data + str(self.headers)

        if any(keyword in scan_content for keyword in malicious_keywords):
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Request Blocked by Firewall (Spring4Shell detected)")
            print("🔥 Blocked malicious request.")
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Request Accepted")
            print("✅ Clean request allowed.")

    def log_message(self, format, *args):
        return  # Disable default logging

def run(server_class=HTTPServer, handler_class=FirewallHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🚦 Firewall server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
