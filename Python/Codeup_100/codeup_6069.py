grade = input()
comment = {
    'A' : 'best!!!',
    'B' : 'good!!',
    'C' : 'run!',
    'D' : 'slowly~'
           }
print(comment.get(grade, 'what?'))
