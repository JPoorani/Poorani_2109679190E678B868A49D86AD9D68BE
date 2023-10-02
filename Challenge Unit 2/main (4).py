class bankAccount:
  def_innit_(self,account_number,account_holder_name,initial_balance=0.0):
  self.__account_number=account_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_balance
  def deposit(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposited {}.New balance:{}".format(amount,self.__acccount_balance))
    else:
      print("Invalid deposit amount.Please deposit a postive amount.")
      def withdraw(self,amount):
        if amount>0 and amount<=self.__account_balance:
          self.__account_balance-=amount
          print("Withdrew {}.New balance:{}".format(amount,self.__account_balance)
                else:
          print("Invalid withdrawal amount or insufficient balance.")
          def display_balance(self):
            print("Account balance for {}(account#{}):".format(self._account_holder_name,self.__account_balance))
            account=BankAccount(account_number="123456789",account_holder_name="pooja",
            initial_balance=10000.0)
            account.display()
            account.deposit(500.0)
            account.withdraw(200.0)
            account.display_balance()