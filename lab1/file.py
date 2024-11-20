class FiniteAutomaton:
    def __init__(self, pattern):
        self.pattern = pattern
        self.M = len(pattern)
        self.CHARS = set(pattern)
        self.TF = {state: {char: 0 for char in self.CHARS} for state in range(self.M)}
        self.computeTF()

    def computeTF(self):
        for state in range(self.M):
            for char in self.CHARS:
                nextState = 0
                if self.pattern[state] == char:
                    nextState = state + 1
                else:
                    for ns in range(state, 0, -1):
                        if self.pattern[ns - 1] == char:
                            i = 0
                            for i in range(ns - 1):
                                if self.pattern[i] != self.pattern[state - ns + 1 + i]:
                                    break
                            if i == ns - 1:
                                nextState = ns
                                break
                self.TF[state][char] = nextState

    def searchPattern(self, text):
        state = 0
        occurrences = []
        for i, char in enumerate(text):
            if state in self.TF and char in self.TF[state]:
                state = self.TF[state][char]
            else:
                state = 0
            if state == self.M:
                occurrences.append(i - self.M + 1)
                print(text[:i - self.M + 1] + '\033[{}m'.format(31) + text[i - self.M + 1:i + 1] + '\033[0m' + text[i:] + '\n')
                i -= self.M
                if i - self.M + 2 < len(text):
                    state = self.TF[0].get(text[i - self.M + 2], 0)
        if occurrences:
            print(f"Pattern found at indices: {occurrences}")
        else:
            print("Pattern not found in the text.")


def KMP(pattern, text):
    M = len(pattern)
    N = len(text)

    lps = [0] * M
    j = 0

    occurrences = []

    computeLPSArray(pattern, M, lps)

    i = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == M:
            occurrences.append(i - j)
            print(text[:i - j] + '\033[{}m'.format(31) + text[i - j:i] + '\033[0m' + text[i:] + '\n')
            j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    if occurrences:
        print(f"Pattern found at indices: {occurrences}")
    else:
        print("Pattern not found in the text.")


def computeLPSArray(pattern, M, lps):
    len = 0
    lps[0] = 0
    i = 1

    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


if __name__ == "__main__":
    import sys

    if sys.argv[1] == 'FA':
        automaton = FiniteAutomaton(sys.argv[2])
        with open(sys.argv[3], 'r') as file:
            text = file.read()
            automaton.searchPattern(text)
    elif sys.argv[1] == 'KMP':
        with open(sys.argv[3], 'r') as file:
            text = file.read()
            KMP(sys.argv[2], text)
