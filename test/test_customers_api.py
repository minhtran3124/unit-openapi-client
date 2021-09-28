"""
    UnitAPI

    Edit the variables with your API Token and API Server.  You can create an API token in Unit Dashboard.   # noqa: E501

    The version of the OpenAPI document: dfec2411-22b5-4a3b-8d43-fcf778bd42a5
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.customers_api import CustomersApi  # noqa: E501


class TestCustomersApi(unittest.TestCase):
    """CustomersApi unit test stubs"""

    def setUp(self):
        self.api = CustomersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_customer_bearer_token(self):
        """Test case for create_customer_bearer_token

        Create Customer Bearer Token  # noqa: E501
        """
        pass

    def test_create_customer_bearer_token_verification(self):
        """Test case for create_customer_bearer_token_verification

        Create Customer Bearer Token Verification  # noqa: E501
        """
        pass

    def test_get1(self):
        """Test case for get1

        Get  # noqa: E501
        """
        pass

    def test_getall0(self):
        """Test case for getall0

        Get all  # noqa: E501
        """
        pass

    def test_patch_customer(self):
        """Test case for patch_customer

        Patch Customer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
