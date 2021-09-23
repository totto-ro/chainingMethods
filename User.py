
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit( self, amount ):
        self.balance += amount
        return self

    def withdraw( self, amount ):
        self.balance -= amount
        return self


    def printInfo( self ):
        print( f"User: {self.name}, Balance: ${self.balance}")
        return self

    def validateFunds ( self, amount ):
        if self.balance > amount:
            return True
        else: 
            return False

    def transfer( self, externalAcc, amountTransfer):
        if self.validateFunds( amountTransfer ):
            self.withdraw( amountTransfer )
            externalAcc.deposit( amountTransfer )
        else:
            print( "You don't have funds" )
        return self
        