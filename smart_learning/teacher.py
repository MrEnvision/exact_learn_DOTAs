from common.equivalence import equivalence
from copy import deepcopy
from common.system import build_canonicalOTA


# LRTWs + value
def TQs(LTWs, system):
    LRTWs, value = system.test_LTWs(LTWs)
    return LRTWs, value


# equivalence query
def EQs(hypothesis, system):
    new_system = build_canonicalOTA(deepcopy(system))
    equivalent, ctx = equivalence(hypothesis, new_system)
    system.eq_num += 1
    return equivalent, ctx
