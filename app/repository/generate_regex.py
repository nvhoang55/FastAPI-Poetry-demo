import pyperclip
from unidecode import unidecode

# Vietnamese characters with diacritical marks.
special_characters = {
    "A": r"[aAàẢÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬ]",
    **dict.fromkeys(['D', 'B', 'P'], r"[dDđĐBP]"),
    "E": r"[eEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆ]",
    "I": r"[iIìÌỉỈĩĨíÍịỊ]",
    "O": r"[oOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢ]",
    "U": r"[UùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰ]",
    "Y": r"[YỳỲỷỶỹỸýÝỵỴ]",
}


def text_to_regex(text: str) -> str:
    regex = ""

    # Convert mark chars to no-mark chars
    text = unidecode(text.upper())

    char_list = list(text)

    # Replace space with "\s?"
    char_list = list(map(lambda x: x.replace(" ", r"\s+?"), char_list))

    # Replace special characters with regex
    for char in char_list:
        if char in special_characters.keys():
            regex += special_characters[char]
        else:
            regex += char

    return regex


regex = text_to_regex("cong hoa xa hoi chu nghia viet nam")
pyperclip.copy(regex)
print(regex)
