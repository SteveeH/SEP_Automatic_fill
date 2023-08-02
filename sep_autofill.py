import time

import requests

from projects import get_project_id

URL = "https://sep.teamexact.cz/dochazka"

# Need to be changed
# ------------------
# update default project in projects.py


# go to sep https://sep.teamexact.cz/dochazka - F12 - Storage - Cookies - PHPSESSID
COOKIE = {"PHPSESSID": None}

INPUT_FILE = "dochazka_test.csv"
USER_ID = None # string ex. "1234", id can be get by program provider

# for now is used same id_type, id_location and id_stredisko for all records
"""
id_stredisko:
    1 - Office
    2 - Marek Přikryl
    3 - DEVELOPMENT
    4 - KONZULTACE SWE
    5 - Scan2Bim
    6 - NAVIS
    7 - PZT zpusobile
    8 - PZT nezpusobile
    9 - Aplikace (uz se nepouziva)
    11 - 3DTeam 

id_location:
    1 - Kancelar
    2 - Home Office
    3 - Prace v terenu
"""
ID_STREDISKO = "11" 
ID_LOCATION = "1"
ID_TYPE = "10" # bezna cinnost
# ------------------

if USER_ID is None or COOKIE["PHPSESSID"] is None:
    raise ValueError("USER_ID or COOKIE['PHPSESSID'] is not set")


def create_record_payload(
    datum: str,
    from_hour: str,
    to_hour: str,
    project_identifier: str,
    note: str = "",
) -> dict:
    """Create payload for record from CSV file."""

    payload = {
        "data[datum]": datum,
        "data[from]": from_hour,
        "data[to]": to_hour,
        "data[id_stredisko]": ID_STREDISKO,
        "data[id_type]": ID_TYPE,
        "data[id_project]": get_project_id(project_identifier),
        "data[id_location]": ID_LOCATION,
        "data[note]": note,
        "data[id_user]": USER_ID,
        "doDochazka": "",
    }

    return payload


def hour_str2float(hour: str) -> float:
    """Convert hour string to float."""

    hour, minute = hour.split(":")

    return float(hour) + float(minute) / 60


def hour_float2str(hour: float) -> str:
    """Convert hour float to string with leading zeros."""

    _hour = int(hour)
    minute = int((hour - _hour) * 60)

    return f"{_hour:02}:{minute:02}"


def main():
    month_hours = 0

    with open(INPUT_FILE, "r",encoding='utf8') as f:
        records_to_send = []
        for line in f.readlines():
            try:

                # "\ufeff" is BOM (Byte Order Mark) for UTF-8
                record = line.lstrip("\ufeff").strip().split(";")

                datum = record[0]
                from_hour = record[1]
                to_hour = record[2]
                project_identifiers = [("","")]

                if len(record) == 4:
                    p_ids = record[3].split(",")

                    project_identifiers = []

                    for p_id in p_ids:

                        p_id_split = p_id.split("-")
                        if len(p_id_split) == 2:
                            project_identifiers.append((p_id_split[0], p_id_split[1]))
                        else:
                            project_identifiers.append((p_id_split[0], ""))
                        

                # 1. get hours for day
                day_start = hour_str2float(from_hour)
                day_end = hour_str2float(to_hour)
                day_hours = day_end - day_start

                if day_hours > 6:
                    month_hours += day_hours - 0.5
                else:
                    month_hours += day_hours


                # 2. recallculate hours for projects and add lunch break

                hours_per_project = day_hours / len(project_identifiers)
                record_start = day_start



                """ 
                there is 4 options:

                1. record starts before 11:30 and ends after 12:00

                             -->--|11:30|--|12:00|--<-- 

                2. record starts before 11:30 and ends before 12:00

                              -->--|11:30|--<--|12:00|--

                3. record starts after 11:30 and ends after 12:00

                              --|11:30|-->--|12:00|--<--

                4. all other situations:
                       - record starts and end before 11:30
                
                              -->--<--|11:30|--|12:00|--

                       - record starts and end after 12:00
                
                              --|11:30|--|12:00|-->--<-- 
                """

                for project_identifier in project_identifiers:
                    # 1.
                    if record_start < 11.5 and record_start + hours_per_project >= 12:
                        # add lunch break
                        records_to_send.append(
                            create_record_payload(
                                datum=datum,
                                from_hour=hour_float2str(record_start),
                                to_hour="11:30",
                                project_identifier=project_identifier[0],
                                note=project_identifier[1],
                            )
                        )

                        records_to_send.append(
                            create_record_payload(
                                datum=datum,
                                from_hour="12:00",
                                to_hour=hour_float2str(
                                    record_start + hours_per_project
                                ),
                                project_identifier=project_identifier[0],
                                note=project_identifier[1],
                            )
                        )
                    # 2.
                    elif record_start < 11.5 and record_start + hours_per_project <= 12:
                        records_to_send.append(
                            create_record_payload(
                                datum=datum,
                                from_hour=hour_float2str(record_start),
                                to_hour="11:30",
                                project_identifier=project_identifier[0],
                                note=project_identifier[1],
                            )
                        )
                    # 3.
                    elif (
                        11.5 <= record_start <= 12
                        and record_start + hours_per_project > 12
                    ):
                        records_to_send.append(
                            create_record_payload(
                                datum=datum,
                                from_hour="12:00",
                                to_hour=hour_float2str(
                                    record_start + hours_per_project
                                ),
                                project_identifier=project_identifier[0],
                                note=project_identifier[1],
                            )
                        )
                    # 4.
                    else:
                        records_to_send.append(
                            create_record_payload(
                                datum=datum,
                                from_hour=hour_float2str(record_start),
                                to_hour=hour_float2str(
                                    record_start + hours_per_project
                                ),
                                project_identifier=project_identifier[0],
                                note=project_identifier[1],
                            )
                        )

                    record_start = record_start + hours_per_project

            except Exception as e:
                print(f"Invalid record format: {line}")
                print(e)

        # 3. write records to file
        with open("payload.txt", "w") as f:
            for record in records_to_send:
                f.write(str(record))
                f.write(",\n")

        # 4. send records to sep

        for rec_num, record in enumerate(records_to_send):
            print(f"Sending record {rec_num + 1}/{len(records_to_send)}")
            try:
                # send POST request with record
                response = requests.post(URL, data=record, cookies=COOKIE)

                # check response status code
                if response.status_code != 200:
                    print(f"Error while sending record: {record}")

            except Exception as e:
                print(f"Error while sending record: {record}")

            # wait 0.5 second before sending next record
            time.sleep(0.15)

    print("Done")
    print(f"Month hours: {month_hours}")


if __name__ == "__main__":
    main()
