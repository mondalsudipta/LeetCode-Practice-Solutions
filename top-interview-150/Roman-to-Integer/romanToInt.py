class Solution:
    def romanToInt(self, s: str) -> int:
        sum_v = 0
        prev_v = 0
        value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if s[i] == "I":
                sum_v += value["I"]
                prev_v = value["I"]

            elif s[i] == "V":
                if prev_v == value["I"]:
                    sum_v -= value["I"]
                    sum_v += value["V"] - value["I"]
                else:
                    sum_v += value["V"]
                prev_v = value["V"]

            elif s[i] == "X":
                if prev_v == value["I"]:
                    sum_v -= value["I"]
                    sum_v += value["X"] - value["I"]
                else:
                    sum_v += value["X"]
                prev_v = value["X"]

            elif s[i] == "L":
                if prev_v == value["X"]:
                    sum_v -= value["X"]
                    sum_v += value["L"] - value["X"]
                else:
                    sum_v += value["L"]
                prev_v = value["L"]

            elif s[i] == "C":
                if prev_v == value["X"]:
                    sum_v -= value["X"]
                    sum_v += value["C"] - value["X"]
                else:
                    sum_v += value["C"]
                prev_v = value["C"]

            elif s[i] == "D":
                if prev_v == value["C"]:
                    sum_v -= value["C"]
                    sum_v += value["D"] - value["C"]
                else:
                    sum_v += value["D"]
                prev_v = value["D"]

            elif s[i] == "M":
                if prev_v == value["C"]:
                    sum_v -= value["C"]
                    sum_v += value["M"] - value["C"]
                else:
                    sum_v += value["M"]
                prev_v = value["M"]
        return sum_v
