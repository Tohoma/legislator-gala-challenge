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
        "preference": "avoid",
        "guests": ["A", "C"]
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
actual_result1 = legislator(num_tables1, guest_list1, planner_preferences1)
print(actual_result1)
expected_result1 = {
    "table_1": ["A", "B"],
    "table_2": ["C"],
    "table_3": ["D"]
}

for table in expected_result1:
    assert set(expected_result1[table]) == set(actual_result1[table])
print("TEST 1 passed")

num_tables2 = 3
guest_list2 = ["A", "B", "C", "D", "E", "F"]
planner_preferences2 = [
    {
        "preference": "pair",
        "guests": ["A", "B"]
    },
    {
        "preference": "avoid",
        "guests": ["B", "C"]
    },
     {
        "preference": "avoid",
        "guests": ["A", "C"]
    },
    {
        "preference":"avoid",
        "guests": ["C", "D"]
    },
    {
        "preference":"avoid",
        "guests": ["B", "D"]
    },
    {
        "preference":"avoid",
        "guests": ["E", "F"]
    }
    ]

actual_result2 = legislator(num_tables2, guest_list2, planner_preferences2)
print("---------------------------------")
print("TEST 2")
print(actual_result2)
expected_result2 = {
    "table_1": ["A", "B", "E"],
    "table_2": ["C", "F"],
    "table_3": ["D"]
}
for table in expected_result2:
    assert set(expected_result2[table]) == set(actual_result2[table])
print("TEST 2 passed")
