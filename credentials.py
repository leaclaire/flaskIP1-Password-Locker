class Credentials :
  """
  Class that generates new instances for credentials.
  """

  credential_list = []

  def __init__(self,account, username,password):
    self.account = account
    self.username = username
    self.password = password

  def save_credentials(self):
    """
    method saves credentials object into credential_list
    """

    Credentials.credential_list.append(self)

  @classmethod
  def credentials_exist(cls, username):
        '''
        method that checks if a credential exists
        '''
        for credentials in cls.credential_list:
            if credentials.username == username:
                return True

        return False

  def delete_credentials(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credential_list.remove(self)

  @classmethod
  def find_by_username(cls,username):
        for credentials in cls.credential_list:
            if credentials.username == username:
                return credentials  


  @classmethod
  def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

 