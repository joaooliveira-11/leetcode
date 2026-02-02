from typing import Deque


def is_valid(s: str) -> bool:
    stack = Deque()

    comp_aux = {
        '(':')',
        '[':']',
        '{':'}'
    }

    for c in s:
        if c in ('(', '[', '{'):
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            top_c = stack.pop()
            if comp_aux[top_c] != c:
                return False
                    
    return len(stack) == 0



