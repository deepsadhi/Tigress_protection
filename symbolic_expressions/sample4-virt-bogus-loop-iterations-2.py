#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_250 = SymVar_0
ref_261 = ref_250 # MOV operation
ref_273 = ref_261 # MOV operation
ref_275 = ref_273 # MOV operation
ref_309 = ((ref_275 >> 56) & 0xFF) # Byte reference - MOV operation
ref_310 = ((ref_275 >> 48) & 0xFF) # Byte reference - MOV operation
ref_311 = ((ref_275 >> 40) & 0xFF) # Byte reference - MOV operation
ref_312 = ((ref_275 >> 32) & 0xFF) # Byte reference - MOV operation
ref_313 = ((ref_275 >> 24) & 0xFF) # Byte reference - MOV operation
ref_314 = ((ref_275 >> 16) & 0xFF) # Byte reference - MOV operation
ref_315 = ((ref_275 >> 8) & 0xFF) # Byte reference - MOV operation
ref_316 = (ref_275 & 0xFF) # Byte reference - MOV operation
ref_1542787 = ref_316 # MOVZX operation
ref_1585475 = (ref_1542787 & 0xFF) # MOVZX operation
ref_1585477 = (ref_1585475 & 0xFF) # MOVZX operation
ref_1713627 = (ref_1585477 & 0xFFFFFFFF) # MOV operation
ref_1713629 = (((ref_1713627 & 0xFFFFFFFF) + 0x1) & 0xFFFFFFFF) # ADD operation
ref_1884492 = (ref_1713629 & 0xFFFFFFFF) # MOV operation
ref_1884501 = ((((0x0) << 32 | (ref_1884492 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_1884503 = (ref_1884501 & 0xFFFFFFFF) # MOV operation
ref_1927225 = (ref_1884503 & 0xFFFFFFFF) # MOV operation
ref_2055439 = (ref_1927225 & 0xFFFFFFFF) # MOV operation
ref_2183589 = (ref_2055439 & 0xFFFFFFFF) # MOV operation
ref_2183591 = (((ref_2183589 & 0xFFFFFFFF) + 0x0) & 0xFFFFFFFF) # ADD operation
ref_2354454 = (ref_2183591 & 0xFFFFFFFF) # MOV operation
ref_2354463 = ((((0x0) << 32 | (ref_2354454 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_2354465 = (ref_2354463 & 0xFFFFFFFF) # MOV operation
ref_2397187 = (ref_2354465 & 0xFFFFFFFF) # MOV operation
ref_3379932 = ref_315 # MOVZX operation
ref_3422620 = (ref_3379932 & 0xFF) # MOVZX operation
ref_3422622 = (ref_3422620 & 0xFF) # MOVZX operation
ref_3508066 = (ref_1927225 & 0xFFFFFFFF) # MOV operation
ref_3550760 = (ref_3508066 & 0xFFFFFFFF) # MOV operation
ref_3550772 = (ref_3422622 & 0xFFFFFFFF) # MOV operation
ref_3550774 = (((ref_3550772 & 0xFFFFFFFF) + (ref_3550760 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_3721637 = (ref_3550774 & 0xFFFFFFFF) # MOV operation
ref_3721646 = ((((0x0) << 32 | (ref_3721637 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_3721648 = (ref_3721646 & 0xFFFFFFFF) # MOV operation
ref_3764370 = (ref_3721648 & 0xFFFFFFFF) # MOV operation
ref_3892584 = (ref_3764370 & 0xFFFFFFFF) # MOV operation
ref_3978028 = (ref_2397187 & 0xFFFFFFFF) # MOV operation
ref_4020722 = (ref_3978028 & 0xFFFFFFFF) # MOV operation
ref_4020734 = (ref_3892584 & 0xFFFFFFFF) # MOV operation
ref_4020736 = (((ref_4020734 & 0xFFFFFFFF) + (ref_4020722 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_4191599 = (ref_4020736 & 0xFFFFFFFF) # MOV operation
ref_4191608 = ((((0x0) << 32 | (ref_4191599 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_4191610 = (ref_4191608 & 0xFFFFFFFF) # MOV operation
ref_4234332 = (ref_4191610 & 0xFFFFFFFF) # MOV operation
ref_5217077 = ref_314 # MOVZX operation
ref_5259765 = (ref_5217077 & 0xFF) # MOVZX operation
ref_5259767 = (ref_5259765 & 0xFF) # MOVZX operation
ref_5345211 = (ref_3764370 & 0xFFFFFFFF) # MOV operation
ref_5387905 = (ref_5345211 & 0xFFFFFFFF) # MOV operation
ref_5387917 = (ref_5259767 & 0xFFFFFFFF) # MOV operation
ref_5387919 = (((ref_5387917 & 0xFFFFFFFF) + (ref_5387905 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_5558782 = (ref_5387919 & 0xFFFFFFFF) # MOV operation
ref_5558791 = ((((0x0) << 32 | (ref_5558782 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_5558793 = (ref_5558791 & 0xFFFFFFFF) # MOV operation
ref_5601515 = (ref_5558793 & 0xFFFFFFFF) # MOV operation
ref_5729729 = (ref_5601515 & 0xFFFFFFFF) # MOV operation
ref_5815173 = (ref_4234332 & 0xFFFFFFFF) # MOV operation
ref_5857867 = (ref_5815173 & 0xFFFFFFFF) # MOV operation
ref_5857879 = (ref_5729729 & 0xFFFFFFFF) # MOV operation
ref_5857881 = (((ref_5857879 & 0xFFFFFFFF) + (ref_5857867 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_6028744 = (ref_5857881 & 0xFFFFFFFF) # MOV operation
ref_6028753 = ((((0x0) << 32 | (ref_6028744 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_6028755 = (ref_6028753 & 0xFFFFFFFF) # MOV operation
ref_6071477 = (ref_6028755 & 0xFFFFFFFF) # MOV operation
ref_7054222 = ref_313 # MOVZX operation
ref_7096910 = (ref_7054222 & 0xFF) # MOVZX operation
ref_7096912 = (ref_7096910 & 0xFF) # MOVZX operation
ref_7182356 = (ref_5601515 & 0xFFFFFFFF) # MOV operation
ref_7225050 = (ref_7182356 & 0xFFFFFFFF) # MOV operation
ref_7225062 = (ref_7096912 & 0xFFFFFFFF) # MOV operation
ref_7225064 = (((ref_7225062 & 0xFFFFFFFF) + (ref_7225050 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7395927 = (ref_7225064 & 0xFFFFFFFF) # MOV operation
ref_7395936 = ((((0x0) << 32 | (ref_7395927 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_7395938 = (ref_7395936 & 0xFFFFFFFF) # MOV operation
ref_7438660 = (ref_7395938 & 0xFFFFFFFF) # MOV operation
ref_7566874 = (ref_7438660 & 0xFFFFFFFF) # MOV operation
ref_7652318 = (ref_6071477 & 0xFFFFFFFF) # MOV operation
ref_7695012 = (ref_7652318 & 0xFFFFFFFF) # MOV operation
ref_7695024 = (ref_7566874 & 0xFFFFFFFF) # MOV operation
ref_7695026 = (((ref_7695024 & 0xFFFFFFFF) + (ref_7695012 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_7865889 = (ref_7695026 & 0xFFFFFFFF) # MOV operation
ref_7865898 = ((((0x0) << 32 | (ref_7865889 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_7865900 = (ref_7865898 & 0xFFFFFFFF) # MOV operation
ref_7908622 = (ref_7865900 & 0xFFFFFFFF) # MOV operation
ref_8891367 = ref_312 # MOVZX operation
ref_8934055 = (ref_8891367 & 0xFF) # MOVZX operation
ref_8934057 = (ref_8934055 & 0xFF) # MOVZX operation
ref_9019501 = (ref_7438660 & 0xFFFFFFFF) # MOV operation
ref_9062195 = (ref_9019501 & 0xFFFFFFFF) # MOV operation
ref_9062207 = (ref_8934057 & 0xFFFFFFFF) # MOV operation
ref_9062209 = (((ref_9062207 & 0xFFFFFFFF) + (ref_9062195 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9233072 = (ref_9062209 & 0xFFFFFFFF) # MOV operation
ref_9233081 = ((((0x0) << 32 | (ref_9233072 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_9233083 = (ref_9233081 & 0xFFFFFFFF) # MOV operation
ref_9275805 = (ref_9233083 & 0xFFFFFFFF) # MOV operation
ref_9404019 = (ref_9275805 & 0xFFFFFFFF) # MOV operation
ref_9489463 = (ref_7908622 & 0xFFFFFFFF) # MOV operation
ref_9532157 = (ref_9489463 & 0xFFFFFFFF) # MOV operation
ref_9532169 = (ref_9404019 & 0xFFFFFFFF) # MOV operation
ref_9532171 = (((ref_9532169 & 0xFFFFFFFF) + (ref_9532157 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_9703034 = (ref_9532171 & 0xFFFFFFFF) # MOV operation
ref_9703043 = ((((0x0) << 32 | (ref_9703034 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_9703045 = (ref_9703043 & 0xFFFFFFFF) # MOV operation
ref_9745767 = (ref_9703045 & 0xFFFFFFFF) # MOV operation
ref_10728512 = ref_311 # MOVZX operation
ref_10771200 = (ref_10728512 & 0xFF) # MOVZX operation
ref_10771202 = (ref_10771200 & 0xFF) # MOVZX operation
ref_10856646 = (ref_9275805 & 0xFFFFFFFF) # MOV operation
ref_10899340 = (ref_10856646 & 0xFFFFFFFF) # MOV operation
ref_10899352 = (ref_10771202 & 0xFFFFFFFF) # MOV operation
ref_10899354 = (((ref_10899352 & 0xFFFFFFFF) + (ref_10899340 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_11070217 = (ref_10899354 & 0xFFFFFFFF) # MOV operation
ref_11070226 = ((((0x0) << 32 | (ref_11070217 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_11070228 = (ref_11070226 & 0xFFFFFFFF) # MOV operation
ref_11112950 = (ref_11070228 & 0xFFFFFFFF) # MOV operation
ref_11241164 = (ref_11112950 & 0xFFFFFFFF) # MOV operation
ref_11326608 = (ref_9745767 & 0xFFFFFFFF) # MOV operation
ref_11369302 = (ref_11326608 & 0xFFFFFFFF) # MOV operation
ref_11369314 = (ref_11241164 & 0xFFFFFFFF) # MOV operation
ref_11369316 = (((ref_11369314 & 0xFFFFFFFF) + (ref_11369302 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_11540179 = (ref_11369316 & 0xFFFFFFFF) # MOV operation
ref_11540188 = ((((0x0) << 32 | (ref_11540179 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_11540190 = (ref_11540188 & 0xFFFFFFFF) # MOV operation
ref_11582912 = (ref_11540190 & 0xFFFFFFFF) # MOV operation
ref_12565657 = ref_310 # MOVZX operation
ref_12608345 = (ref_12565657 & 0xFF) # MOVZX operation
ref_12608347 = (ref_12608345 & 0xFF) # MOVZX operation
ref_12693791 = (ref_11112950 & 0xFFFFFFFF) # MOV operation
ref_12736485 = (ref_12693791 & 0xFFFFFFFF) # MOV operation
ref_12736497 = (ref_12608347 & 0xFFFFFFFF) # MOV operation
ref_12736499 = (((ref_12736497 & 0xFFFFFFFF) + (ref_12736485 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_12907362 = (ref_12736499 & 0xFFFFFFFF) # MOV operation
ref_12907371 = ((((0x0) << 32 | (ref_12907362 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_12907373 = (ref_12907371 & 0xFFFFFFFF) # MOV operation
ref_12950095 = (ref_12907373 & 0xFFFFFFFF) # MOV operation
ref_13078309 = (ref_12950095 & 0xFFFFFFFF) # MOV operation
ref_13163753 = (ref_11582912 & 0xFFFFFFFF) # MOV operation
ref_13206447 = (ref_13163753 & 0xFFFFFFFF) # MOV operation
ref_13206459 = (ref_13078309 & 0xFFFFFFFF) # MOV operation
ref_13206461 = (((ref_13206459 & 0xFFFFFFFF) + (ref_13206447 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_13377324 = (ref_13206461 & 0xFFFFFFFF) # MOV operation
ref_13377333 = ((((0x0) << 32 | (ref_13377324 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_13377335 = (ref_13377333 & 0xFFFFFFFF) # MOV operation
ref_13420057 = (ref_13377335 & 0xFFFFFFFF) # MOV operation
ref_14402802 = ref_309 # MOVZX operation
ref_14445490 = (ref_14402802 & 0xFF) # MOVZX operation
ref_14445492 = (ref_14445490 & 0xFF) # MOVZX operation
ref_14530936 = (ref_12950095 & 0xFFFFFFFF) # MOV operation
ref_14573630 = (ref_14530936 & 0xFFFFFFFF) # MOV operation
ref_14573642 = (ref_14445492 & 0xFFFFFFFF) # MOV operation
ref_14573644 = (((ref_14573642 & 0xFFFFFFFF) + (ref_14573630 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_14744507 = (ref_14573644 & 0xFFFFFFFF) # MOV operation
ref_14744516 = ((((0x0) << 32 | (ref_14744507 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_14744518 = (ref_14744516 & 0xFFFFFFFF) # MOV operation
ref_14787240 = (ref_14744518 & 0xFFFFFFFF) # MOV operation
ref_14915454 = (ref_14787240 & 0xFFFFFFFF) # MOV operation
ref_15000898 = (ref_13420057 & 0xFFFFFFFF) # MOV operation
ref_15043592 = (ref_15000898 & 0xFFFFFFFF) # MOV operation
ref_15043604 = (ref_14915454 & 0xFFFFFFFF) # MOV operation
ref_15043606 = (((ref_15043604 & 0xFFFFFFFF) + (ref_15043592 & 0xFFFFFFFF)) & 0xFFFFFFFF) # ADD operation
ref_15214469 = (ref_15043606 & 0xFFFFFFFF) # MOV operation
ref_15214478 = ((((0x0) << 32 | (ref_15214469 & 0xFFFFFFFF)) % 0xFFF1) & 0xFFFFFFFF) # DIV operation
ref_15214480 = (ref_15214478 & 0xFFFFFFFF) # MOV operation
ref_15257202 = (ref_15214480 & 0xFFFFFFFF) # MOV operation
ref_16026300 = (ref_15257202 & 0xFFFFFFFF) # MOV operation
ref_16111736 = (ref_16026300 & 0xFFFFFFFF) # MOV operation
ref_16111744 = (((ref_16111736 & 0xFFFFFFFF) << (0x10 & 0x1F)) & 0xFFFFFFFF) # SHL operation
ref_16111751 = (ref_16111744 & 0xFFFFFFFF) # MOV operation
ref_16197215 = (ref_14787240 & 0xFFFFFFFF) # MOV operation
ref_16239917 = (ref_16111751 & 0xFFFFFFFF) # MOV operation
ref_16239921 = (ref_16197215 & 0xFFFFFFFF) # MOV operation
ref_16239923 = ((ref_16239921 & 0xFFFFFFFF) | (ref_16239917 & 0xFFFFFFFF)) # OR operation
ref_16282650 = (ref_16239923 & 0xFFFFFFFF) # MOV operation
ref_16410820 = (ref_16282650 & 0xFFFFFFFF) # MOV operation
ref_16453510 = (ref_16410820 & 0xFFFFFFFF) # MOV operation
ref_16453534 = (ref_16453510 & 0xFFFFFFFF) # MOV operation
ref_16453542 = (ref_16453534 & 0xFFFFFFFF) # MOV operation
ref_16453544 = (ref_16453542 & 0xFFFFFFFF) # MOV operation

print ref_16453544 & 0xffffffffffffffff