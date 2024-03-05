class Reminder:
    def storer(self):
        self.my_dict = {}
        num_events = int(input('How many events do you want to store? '))
        for _ in range(num_events):
            date = input('Enter an important date to remember: ')
            event = input('Enter an important event to remember: ')
            self.my_dict[date] = event
        print("Events stored successfully:", self.my_dict)

    def checker(self):
        date = input('Enter the date to check: ')
        if date in self.my_dict:
            print(f"The event on {date} is: {self.my_dict[date]}")
        else:
            print("No event found for this date.")


rem = Reminder()
ans='y'
while ans=='y':
    print('Welcome to Remind Me!!!')
    print('Enter your choice:')
    print('1.add event\n 2.check event\n')
    choice=int(input('enter the choice: '))
    if choice==1:
        rem.storer()
    elif choice==2:
        rem.checker()
    else:
        print('no such option. Choose again!!!')
    print('do you want to choose again: ')
    ans=input('enter y/n: ').lower()
print('Thanks for using.:) See you again!!')  
