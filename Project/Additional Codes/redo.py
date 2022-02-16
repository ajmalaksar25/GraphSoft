yes=['YES','Y','Yes','yes']
no=['NO','N','No','no']

userin=input('Start?:')
if userin in yes:
    while True:
        import User_End
        del(User_End)
        re1=input('again? ')
        while re1 in yes:
            import User_End
        print('Thank you for using GraphSoft')
        exit()
