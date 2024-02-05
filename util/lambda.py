import sys,os,time,marshal,zlib,base64; # utility bashpy compile module
from time import ctime as ctt

# create strukture
Wak     =    ctt()
OsUn    =    os.uname()

try:
    opf = sys.argv[1]
    oxf = compile(opf.encode('utf-8'),'<Aleks>','exec')
    oef = repr(base64.b64encode(zlib.compress(marshal.dumps(oxf))))
    print ("Aleks=(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(%s))));exec(Aleks)" % (oef))
    #code = "Aleks=(eval((lambda ____,__,_ : ____.join([_(____) for ___ in __]))({}, chr))(eval((lambda ____,__,_ : ____.join([_(____) for ___ in __]))({}, chr))(eval((lambda ____,__,_ : ____.join([_(____) for ___ in __]))({}, chr))(%s))));exec(Aleks)".format(oef)
except Exception as e:
    print("error{}".format(e))
