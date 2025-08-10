def load_personnel_data():
    """Sample personnel data"""
    return [
        {"id": "P001", "name": "Smith", "rank": "Captain", "unit": "Alpha", "clearance": "Secret"},
        {"id": "P002", "name": "Johnson", "rank": "Lieutenant", "unit": "Bravo", "clearance": "Top Secret"},
        {"id": "P003", "name": "Williams", "rank": "Sergeant", "unit": "Alpha", "clearance": "Confidential"},
        {"id": "P004", "name": "Brown", "rank": "Major", "unit": "Charlie", "clearance": "Top Secret"}
    ]


def filter_by_clearance(personnel, clearance_level):
    """Filter personnel by security clearance"""
    return [p for p in personnel if p["clearance"] == clearance_level]


def group_by_unit(personnel):
    """Group personnel by unit"""
    units = {}
    for person in personnel:
        unit = person["unit"]
        if unit not in units:
            units[unit] = []
        units[unit].append(person["name"])
    return units
