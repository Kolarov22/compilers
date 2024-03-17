import re
def Search(searchFor, searchInto):
    positions = []
    
    for keyword in searchFor:
        pattern = r'\b' + re.escape(keyword) + r'\b'
        matches = re.finditer(pattern, searchInto)
        for match in matches:
            positions.append((keyword, match.start(), match.end()))

    return positions