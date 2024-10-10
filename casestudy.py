acc_no=240011223300
db=[]
class BANK:
    def __init__(self):
        print('Welcome to TEZ Bank')
        self.options()
    def options(self):
        self.res=1
        while(self.res==1):
            print('''
\t1.CREATE ACCOUNT
\t2.VIEW ACCOUNT DETAILS
\t3.WITHDRAWAL
\t4.DEPOSIT
\t5.FUND TRANSFER
\t6.PRINT TRANSCATIONS
\t7.EXIT''')
            self.n=int(input("Please Select your option:"))
            
            if self.n==1:
                self.createacc()
            elif self.n==2:
                self.view()
            elif self.n==3:
                self.withdraw()
            elif self.n==4:
                self.deposit()
            elif self.n==5:
                self.fundtransfer()
            elif self.n==6:
                self.print_trans()
            elif self.n==7:
                break
            else:
                print("Please select valid option")
            self.res=int(input("Do you want to further information(enter 1 for yes and 0 for no):"))
                
    def createacc(self):
        global acc_no
        global db
        self.user=input('enter username:')
        self.password=input('enter password:')
        if len(db)!=0:
            for i in db:
                if i[1]==self.user:
                    print('Username already exists\nTry another username')
                    print('Your Account not created')
                    break
            else:
                acc_no+=1
                db.append([acc_no,self.user,self.password,0.0,[]])
                print('Your new account is created\nYour account Number:',acc_no)
        else:
            acc_no+=1
            db.append([acc_no,self.user,self.password,0.0,[]])
            print('Your new account is created\nYour account Number:',acc_no)
    def view(self):
        self.a=int(input('Enter account number:'))
        global db
        for i in db:
            if i[0]==self.a:
                print('Welcome {}\nAvailable Balance:{}'.format(i[1],i[3]))
                break
        else:
            print('Enter correct account number')
    def withdraw(self):
        self.ac=int(input('Enter account number:'))
        global db
        for i in db:
            if i[0]==self.ac:
                self.w=float(input('Enter amount to withdraw:'))
                if self.w<=i[3]:
                    i[3]-=self.w
                    print('Withdrawal amount:',self.w)
                    print('Available Balance:',i[3])
                    i[4].append(-self.w)
                else:
                    print('Insufficient Funds')
                break
        else:
            print('Account Not Found')  
    def deposit(self):
        self.ac=int(input('Enter account number:'))
        global db
        for i in db:
            if i[0]==self.ac:
                self.d=float(input('Enter amount to deposit:'))
                i[3]+=self.d
                print('Available Balance:',i[3])
                i[4].append(self.d)
                break
        else:
            print('Account Not Found')
    def fundtransfer(self):
        self.ur=int(input('Enter your account number:'))
        global db
        for i in db:
            if i[0]==self.ur:
                self.op=int(input('Enter account number to transfer amount:'))
                for j in db:
                    if j[0]==self.op:
                        self.amo=float(input('Enter amount to transfer:'))
                        if self.amo<=i[3]:
                            j[3]+=self.amo
                            i[3]-=self.amo
                            print('Funds transferred successfully\nAvailable Balance:',i[3])
                            i[4].append(-self.amo)
                            j[4].append(self.amo)
                        else:
                            print('Insufficient Funds')
                        break
                else:
                    print('Other person account Not Found')
                break
        else:
            print('Your Account Not Found')
    def print_trans(self):
        self.ac=int(input('Enter Account Number:'))
        global db
        for i in db:
            if i[0]==self.ac:
                print("NOTE:\n\n1.'-' before amount indicates amount debited\n2.No sign before amount indicates amount credited\n\nTransactions(old to new)")
                if len(i[4])==0:
                    print('No Transactions Done Yet')
                else:
                    for j in i[4]:
                        print(j)
                print('Available Balance:',i[3])
                break
        else:
            print('Your Account Not Found')
                
print('****USE THE BELOW ACCOUNT DETAILS FOR REFERENCE*****')
db.append([240011223300,'saiteja','12345678',10000,[10000]])
#db.append([240011223299,'Madhu','12345678',0,[]])
#db.append([240011223288,'chathur','12345678',20000,[20000]])
print(db)
o=BANK()



