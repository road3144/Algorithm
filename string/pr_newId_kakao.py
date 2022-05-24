import re


def solution(new_id):
    new_id = new_id.lower()
    symbols = "-_.~!@#$%^&*()=+[{]}:?,<>/".replace(".", "").replace("-", "").replace("_", "")
    for symbol in symbols:
        new_id = new_id.replace(symbol, "")
    # new_id = re.sub("[^a-z0-9\-_.]", "", new_id)
    new_id = re.sub("\.+", ".", new_id)
    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_id = new_id[:len(new_id)-1]
    if len(new_id) == 0:
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id.endswith("."):
        new_id = new_id[:len(new_id)-1]
    while len(new_id) < 3:
        new_id = new_id + new_id[len(new_id)-1]
    return new_id


print(solution("...!@Bw23--_aT#*..y.abcdfg..h..ijklm"))
