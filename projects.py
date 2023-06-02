PROJECTS_ID = {
    "32": ["1724"],
    "33": ["1724"],
    "81": ["2108.7"],
    "58": ["2201.1"],
    "64": ["2201.2"],
    "96": ["2212.2","SUDB"],
    "97": ["2222"],
    "107": ["2305"],
    "108": ["2306"],
    "110": ["2308"],
    "111": ["2309"],
    "113": ["2310"],
    "16": ["INT_007"],
    "88": ["INT_079", "PP2TEST"],
    "89": ["INT_080", "OBST"],
    "90": ["INT_081", "CSR", "CSI"],
    "91": ["INT_082", "DMU", "DNA"],
    "98": ["INT_084", "ONSITE"],
    "99": ["INT_085", "PP2"],
    "100": ["INT_086"],
    "101": ["INT_087"],
    "102": ["INT_088", "SALE"],
    "29": ["INT_202_GR", "PZT", "RND"],
    "18": ["Office"],
    "35": ["Sale"],
}

DEFAULT_PROJECT = "29"


def get_project_id(value: str) -> str:
    """Return project ID based on project name.
    default project is INT_202_GR
    """

    for key, values in PROJECTS_ID.items():
        if value in values:
            return key

    return DEFAULT_PROJECT
