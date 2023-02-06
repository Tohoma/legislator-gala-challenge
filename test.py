from legislator import *

num_tables1 = 3
guest_list1 = ["A", "B", "C", "D"]
planner_preferences1 = [
    {
        "preference": "pair",
        "guests": ["A", "B"]
    },
    {
        "preference": "avoid",
        "guests": ["B", "C"]
    },
    {
        "preference":"avoid",
        "guests": ["C", "D"]
    },
    {
        "preference":"avoid",
        "guests": ["B", "D"]
    }
    ]
actual_result = legislator(num_tables1, guest_list1, planner_preferences1)
expected_result = {
    "table_1": ["A", "B"],
    "table_2": ["C"],
    "table_3": ["D"]
}
assert actual_result == expected_result