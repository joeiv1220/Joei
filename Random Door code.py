while True:
    print 'pick a door \n Door One \n Door Two \n Door Three'
    answer = raw_input()
    if answer in ['Door One', 'Door Two', 'Door Three']:
            print 'Okay.'
            break
    elif answer in ['1','2','3']:
        print 'Invalid option. Input a valid option.'
        