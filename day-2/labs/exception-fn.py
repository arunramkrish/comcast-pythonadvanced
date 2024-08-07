class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise ExceptionGroup("g1", [B(), C()])
    except (D,C) as e:
        print("D or C" + str(e))
    except B as e:
        print("B " + str(e))