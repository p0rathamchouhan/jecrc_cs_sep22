    today=(input())
    condition=input()
    if today=='Saturday':
        print('Half Day Work')
    elif today=='Sunday':
        if condition=='Sick':
            print('Take Rest')
        else:
            print('party')

