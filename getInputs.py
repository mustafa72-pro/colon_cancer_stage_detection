def get_inputs(_age,_sex,_topo,_t,_n,_m,_surge):
    if (_sex == 'M'):
        _sex = 1
    elif (_sex == 'F'):
        _sex = 2


    if (_topo == 'colon_sigm'):
        _topo = 1
    elif (_topo == 'ungh_splen'):
        _topo = 2
    elif (_topo == 'colon_desc'):
        _topo = 3
    elif (_topo == 'cec'):
        _topo = 4
    elif (_topo == 'jonc_rect_sigm'):
        _topo = 5
    elif (_topo == 'rect'):
        _topo = 6
    elif (_topo == 'colon_trans'):
        _topo = 7
    elif (_topo == 'colon_asc'):
        _topo = 8
    elif (_topo == 'ungh_hep'):
        _topo = 9


    if(_t =='T1'):
        _t = 1
    elif(_t =='T2'):
        _t = 2
    elif(_t =='T3'):
        _t = 3
    elif(_t =='T4'):
        _t = 4
    elif(_t =='Tx'):
        _t = 4


    if(_n =='N0'):
        _n = 0
    elif(_n =='N1'):
        _n = 1
    elif(_n =='N2'):
        _n = 2
    elif(_n =='Nx'):
        _n = 3


    if(_m =='M0'):
        _m = 0
    elif(_m =='M1'):
        _m = 1
    elif(_m =='Mx'):
        _m = 2
    elif(_m =='M1_hep'):
        _m = 3

    if (_surge == 'one'):
        _surge = 1
    elif (_surge == 'two'):
        _surge = 2
    elif (_topo == 'three'):
        _surge = 3
    elif (_surge == 'four'):
        _surge = 4
    elif (_surge == 'five'):
        _surge = 5
    elif (_surge == 'six'):
        _surge = 6
    elif (_surge == 'seven'):
        _surge = 7
    elif (_surge == 'eight'):
        _surge = 8
    elif (_surge == 'nine'):
        _surge = 9
    elif (_surge == 'ten'):
        _surge = 10

    return (_age,_sex,_topo,_t,_n,_m,_surge)