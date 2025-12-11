from employee import emp_details

def test_employee():
    expected_output=(
        "Employee name: Queen\n"
        "Employee id: 900\n"
        "Department: MCA\n"
        "Salary: 200000"
    )

    assert emp_details("Queen",900,"MCA",200000) ==expected_op
