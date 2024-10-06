# conftest.py
from decimal import Decimal
from faker import Faker
from calculator.plugins.addition.add_plugin import AddCommand
from calculator.plugins.subtraction.subtraction_plugin import SubtractCommand
from calculator.plugins.multiplication.multiplication_plugin import MultiplyCommand
from calculator.plugins.division.division_plugin import DivideCommand

fake = Faker()

def generate_test_data(num_records):
    """Generate test data for various operations.

    Args:
        num_records (int): The number of records to generate.

    Yields:
        Tuple[Decimal, Decimal, str, Callable, Union[Decimal, str]]: Generated test data including operands, operation name, function, and expected result.
    """
    operation_mappings = {
        'add': AddCommand,
        'subtract': SubtractCommand,
        'multiply': MultiplyCommand,
        'divide': DivideCommand
    }
    
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        
        # Ensure b is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == DivideCommand: 
            b = Decimal('1') if b == Decimal('0') else b
        
        # Calculate expected result
        try:
            expected = operation_func(a, b).execute()  # Call the execute method to get the result
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Add command line options for pytest.

    Args:
        parser: The parser object for adding command line options.
    """
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Generate tests dynamically based on the provided fixture names.

    Args:
        metafunc: The metafunc object used to define test parameterization.
    """
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        modified_parameters = [
            (a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected)
            for a, b, op_name, op_func, expected in parameters
        ]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
