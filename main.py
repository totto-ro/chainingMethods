from User import User

adrienUser = User( "Adrien")
adrienUser.deposit( 101 ).deposit( 101 ).deposit( 201 ).withdraw( 101 ).printInfo()

mrNibblesUser = User( "Mr. Nibbles")
mrNibblesUser.deposit( 1200 ).deposit( 2200 ).withdraw( 1200 ).withdraw( 1000 ).printInfo()

bennyUser = User( "Benny Bob")
bennyUser.deposit( 1500 ).withdraw( 1000 ).withdraw( 5000 ).withdraw( 3000 ).printInfo()

adrienUser.transfer( bennyUser, 250 ).printInfo()
bennyUser.printInfo()
