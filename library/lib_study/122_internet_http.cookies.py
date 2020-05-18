from http import cookies
C = cookies.SimpleCookie()
C["fig"] = "newton"
C["sugar"] = "wafer"
print(C) # generate HTTP headers
print(C.output()) # same thing
C = cookies.SimpleCookie()
C["rocky"] = "road"
C["rocky"]["path"] = "/cookie"
print(C.output(header="Cookie:"))
print(C.output(attrs=[], header="Cookie:"))
C = cookies.SimpleCookie()
C.load("chips=ahoy; vienna=finger") # load from a string (HTTP header)
print(C)
C = cookies.SimpleCookie()
C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=\\012;";')
print(C)
C = cookies.SimpleCookie()
C["oreo"] = "doublestuff"
C["oreo"]["path"] = "/"
print(C)
C = cookies.SimpleCookie()
C["twix"] = "none for you"
print(C["twix"].value)
C = cookies.SimpleCookie()
C["number"] = 7 # equivalent to C["number"] = str(7)
C["string"] = "seven"
print(C["number"].value)
print(C["string"].value)
print(C)