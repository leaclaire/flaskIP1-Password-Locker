# import unittest
# from account import Account


# class TestAccount(unittest.TestCase):

#       """
#       Test class that defines test cases for the account class behaviours.

#         Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#       """

#       def setUp(self):
#         """
#         setUp method to run before each test case.
#         """
#         self.new_account = Account ("leah", "jepkorir", "leaclaire003")

#       def test_init(self):
#         """
#         test_init test cases to test if the object is initialized properly.
#         """

        self.assertEqual(self.new_account.account_name,"leah")
        self.assertEqual(self.new_account.user_name,"jepkorir")
        self.assertEqual(self.new_account.password,"leaclaire003")

      def test_save_account(self):
        """
        test_save_account test cases to test if the account object is saved into the account list.
        """

        self.new_account.save_accounts()
        self.assertEqual(len(Account.account_list),1)

      def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_account.save_account()
        test_account = Account ("leah", "jepkorir", "leaclaire003") 
        test_account.save_account()

        account_exists = Account.account_exists("jepkorir", "leaclaire003")
        self.assertTrue(account_exists)
      

if __name__ == '__main__':
    unittest.main()   
