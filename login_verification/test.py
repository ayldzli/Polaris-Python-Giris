from login_verification import check_password

def test_func():
    assert(check_password("adj738JS")) == True
    assert(check_password("32432443")) == True
    assert(check_password("DSFHK247")) == True
    assert(check_password("235?3daa")) == True
    assert(check_password("DSFH///?")) == True
    assert(check_password("%&+?*//^")) == True
    assert(check_password("DSFdsada")) == True
    assert(check_password("32478!!2")) == True
    assert(check_password("20007A/s")) == False
    assert(check_password("t81/?!J1")) == False
    assert(check_password("sdUD#f4d")) == False
    assert(check_password("DS83)js2")) == False