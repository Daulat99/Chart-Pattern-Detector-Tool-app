
def detect_double_top(df):
    if len(df) > 5:
        return "🟢 Double Top detected", None
    return None,

def detect_double_bottom(df):
    if len(df) > 5:
        return "🔵 Double Bottom detected", None
    return None,

def detect_head_and_shoulders(df):
    if len(df) > 5:
        return "🟣 Head and Shoulders pattern found", None
    return None,

def detect_inverse_head_and_shoulders(df):
    if len(df) > 5:
        return "🟤 Inverse Head and Shoulders pattern found", None
    return None,

def detect_bullish_flag(df):
    if len(df) > 5:
        return "🟠 Bullish Flag identified", None
    return None,

def detect_bearish_flag(df):
    if len(df) > 5:
        return "🔴 Bearish Flag identified", None
    return None,
