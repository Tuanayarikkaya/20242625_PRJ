import os
import sys

KOK_DIZIN = os.path.dirname(os.path.dirname(__file__))
SRC_DIZIN = os.path.join(KOK_DIZIN, "src")
sys.path.insert(0, SRC_DIZIN)
