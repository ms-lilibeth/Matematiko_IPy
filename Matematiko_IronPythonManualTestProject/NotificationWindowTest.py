from System import Array
from NotificationWindow import NotificationWindow

def TestRandomResults():
    field1D = [randint(1,13) for i in range(field_lght*field_lght)]
    arr = Array.CreateInstance(int, field_lght*field_lght)
    pass

def TestFixedResultSet():
    res1 = {"Sum":440,
           "INLINE_2EqNums":6,"INLINE_3EqNums":1,"INLINE_4EqNums":0,
           "INLINE_2PairsOfEqNums":1,"INLINE_3EqNums_plus_2EqNums":2,
           "INLINE_5ConsecutiveNums":0,"INLINE_Three_1_Two_13":0,
           "INLINE_1_10_11_12_13":0,"INLINE_4Ones":0,"BIAS_2EqNums":8,
           "BIAS_3EqNums":0,"BIAS_4EqNums":0,"BIAS_2PairsOfEqNums":0,
           "BIAS_3EqNums_plus_2EqNums":0,"BIAS_5ConsecutiveNums":0,
           "BIAS_Three_1_Two_13":0,"BIAS_1_10_11_12_13":0,"BIAS_4Ones":0}

    res2 = {"Sum":350,"INLINE_2EqNums":6,"INLINE_3EqNums":0,"INLINE_4EqNums":0,
            "INLINE_2PairsOfEqNums":2,"INLINE_3EqNums_plus_2EqNums":0,
            "INLINE_5ConsecutiveNums":2,"INLINE_Three_1_Two_13":0,
            "INLINE_1_10_11_12_13":0,"INLINE_4Ones":0,"BIAS_2EqNums":5,
            "BIAS_3EqNums":1,"BIAS_4EqNums":0,"BIAS_2PairsOfEqNums":0,
            "BIAS_3EqNums_plus_2EqNums":0,"BIAS_5ConsecutiveNums":0,
            "BIAS_Three_1_Two_13":0,"BIAS_1_10_11_12_13":0,"BIAS_4Ones":0}

    w = NotificationWindow(res1, res2)
    w.Show()

