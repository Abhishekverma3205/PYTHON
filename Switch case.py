#switch case

def switch_exam(day):
    switcher = {
        "Monday": "Math",
        "Tuesday": "English",
        "Wednesday": "Science",
        "Thursday": "History",
        "Friday": "Art"
    }
    return switcher.get(day, "No exam scheduled")