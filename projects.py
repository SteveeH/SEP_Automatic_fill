PROJECTS_ID = {
    "32": ["1724"],
    "33": ["1724"],
    "81": ["2108.7"],
    "58": ["2201.1"],
    "64": ["2201.2"],
    "96": ["2212.2", "SUDB"],
    "97": ["2222"],
    "107": ["2305"],
    "108": ["2306"],
    "110": ["2308"],
    "111": ["2309"],
    "113": ["2310"],
    "114": ["2311"],
    "121": ["2316", "HW401"],
    "122": ["2317", "Opava", "Tesinska"],
    "124": ["2320", "Trebic"],
    "127": ["2321", "Oresud", "SWE_most"],
    "129": ["2316.2", "HW401_2"],
    "146": ["2323", "E6", "E6_Stenungsund"],
    "16": ["INT_007"],
    "88": ["INT_079", "PP2TEST"],
    "89": ["INT_080", "OBST"],
    "90": ["INT_081", "CSR", "CSI"],
    "91": ["INT_082", "DMU", "DNA"],
    "98": ["INT_084", "ONSITE"],
    "99": ["INT_085", "PP2"],
    "100": ["INT_086"],
    "101": ["INT_087", "DMU_portal", "dmu_portal"],
    "102": ["INT_088", "fika", "Fika", "FIKA", "INT_Schuzky"],
    "29": ["INT_202_GR", "PZT", "RND"],
    "18": ["Office"],
    "35": ["Sale", "Sales"],
    "128": ["ESA_A", "esa_a"],
    "133": ["ESA_B", "esa_b"],
    "134": ["ESA_C", "esa_c"],
    "136": ["ESA_E", "esa_e"],
    "135": ["ESA_D", "esa_d", "ESA_AdjustMT", "AdjustMT"],
    "137": ["ESA_F", "esa_f", "ESA_Remote_PP2", "Remote_PP2", "esa_remote_pp2"],
    "139": ["ESA_G", "esa_g"],
    "140": ["ESA_H", "esa_h"],
    "141": ["ESA_I", "esa_i"],
    "142": ["ESA_J", "esa_j"],
    "143": ["ESA_K", "esa_k"],
    "144": ["ESA_L", "esa_l"],
    "145": ["ESA_M", "esa_m"],
    "147": ["ESA_N", "esa_n"],
    "148": ["ESA_O", "esa_o", "esa_meeting", "ESA_meeting"],
    "149": ["DMU_TS", "dmu_ts", "patent_ts"],
    "150": ["Virtual_ski_marketing", "DMU_Marketing"],
    "162": ["INT_97", "Test_virtual_ski"],
    "164": ["INT_98", "scan_inclination"],
    "152": ["INT_92", "vyuzitelnost_ski"],
    "172": ["E18", "SWE_E18"],
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
