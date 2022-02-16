print('Welcome to GraphSoft')
import User_End
yes=['YES','Y','Yes','yes']
no=['NO','N','No','no']
def user_end():
    import user_end
    
def user_newin():
    str(input('Would you like to try again? (YES/NO): '))
user_newin()
if user_newin in yes:
    while user_newin in yes:
        User_End()
        user_newin()
        if user_newin in no:
            break
    
elif user_newin in no:
    print('Thank you for Using GraphSoft')
    exit()
