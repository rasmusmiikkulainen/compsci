def max_char_rep(s):
    if not s:
        out = 0
    else:
        streaks = [1]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                streaks.append(0)
            streaks[-1] += 1
            out = max(streaks)
    return out

testcases = ["abcd", "abbbcdd", "abbbcddddd", ""]
for a in testcases:
    print(f"'{a}'", max_char_rep(a))