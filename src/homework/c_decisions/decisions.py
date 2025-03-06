
def get_options_ratio (options, total):
    ratio = options / total
    return ratio


def get_faculty_rating(ratio):
    if 0.9 <= ratio <= 1: 
        return "Excellent"
    if 0.8 <= ratio < 0.9:
        return "Very Good"
    if 0.7 <= ratio < 0.8:
        return "Good"
    if 0.6 <= ratio < 0.7:
        return "Needs Improvement"
    elif 0 <= ratio < 0.6: 
        return "Unacceptable"
    