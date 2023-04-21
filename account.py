class Account:
    def __init__(self, name:str) -> None:
        '''
        Sets up Account
        :param name: the Account Name
        '''
        self.__account_name = name
        self.__account_balance = 0


    def deposit(self,amount:float) -> bool:
        '''
        Puts Money into Account
        :param amount: amount of money being added to account
        :return: Whether Money was added or not
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False


    def withdraw(self,amount:float) -> bool:
        '''
        Takes Money from Account
        :param amount: Amount of money being taken from account
        :return: Whether Money was taken or not
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False


    def get_balance(self) -> float:
        '''
        :return: gives account balance
        '''
        return self.__account_balance


    def get_name(self) -> str:
        '''
        :return: gives account name
        '''
        return self.__account_name
