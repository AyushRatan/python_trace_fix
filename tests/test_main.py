import os
import pytest
import pandas as pd
from mymodule.main import app

# Define the path to the test output file
# TEST_OUTPUT_FILE = "C:/Users/ttelkapa/project/NLP_pytest_code/mymodule/output.xlsx"
# store_df = pd.read_excel(TEST_OUTPUT_FILE)

# # Define the columns of the output file
# OUTPUT_COLUMNS = ["name", "age"]

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# @pytest.fixture(scope="session", autouse=True)
# def setup_test_data():
#    """
#    Fixture to setup the test data by creating a new test output file
#    """
#    # Create a new empty test output file with only the name and age columns
#    df = pd.DataFrame(columns=OUTPUT_COLUMNS)
#    df.to_excel(TEST_OUTPUT_FILE, index=False)
#    yield

#     # Clean the output file after testing
#    df = pd.DataFrame(columns=OUTPUT_COLUMNS)
#    df.to_excel(TEST_OUTPUT_FILE, index=False)

def test_form_post_empty(client):
    """
    Test that submitting an empty form returns an error
    """
    response = client.post("/", data=dict(name="", age=""))
    assert b"Please fill in both fields." in response.data

def test_form_post_invalid_age_out_of_bound(client):
    """
    Test that submitting a form with an invalid age returns an error
    """
    response = client.post("/", data=dict(name="John", age="111"))
    assert b"Age must be a valid number between 0 and 110." in response.data

def test_form_post_invalid_age_negative(client):
    """
    Test that submitting a form with an invalid age returns an error
    """
    response = client.post("/", data=dict(name="John", age="-2"))
    assert b"Age must be a valid number between 0 and 110." in response.data

def test_form_post_valid(client):
    """
    Test that submitting a valid form adds the data to the output file
    """
    response = client.post("/", data=dict(name="John", age="30"))
    assert b"Data successfully added!" in response.data
    
    # Check that the data was added to the output file
    # df = pd.read_excel(TEST_OUTPUT_FILE)
    # assert df.shape[0] == 1
    # assert df.iloc[0]['name'] == 'John'
    # assert df.iloc[0]['age'] == 30

    # Clean the output file after testing
    # df = pd.DataFrame(columns=OUTPUT_COLUMNS)
# store_df.to_excel(TEST_OUTPUT_FILE, index=False)
