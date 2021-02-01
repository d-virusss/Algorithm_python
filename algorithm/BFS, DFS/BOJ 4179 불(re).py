# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import sys
from collections import deque
row, col = map(int, sys.stdin.readline().split())
field = [ list(sys.stdin.readline().strip()) for _ in range(row)]
q, fq = deque([]), deque([])