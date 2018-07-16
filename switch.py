def case1_include(A,B):
    if (A in B):
        print "B include A"
    else:
        print "NO"
    
def case2_equal(A,B):
    print "A equal B"


switch={"include" :case1_include,
"equal" :case2_equal}


AA= "include jpg"
BB= "sfsdfdsdaf.jpg"
CC= AA.split(' ',1)


switch["include"](CC[1],BB)
