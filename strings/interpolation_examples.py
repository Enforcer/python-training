# Altogether
'Hello, %s! %s to meet you for the %d time!' % ('Sebastian', 'Nice', 1)
# 'Hello, Sebastian! Nice to meet you for the 1 time!'

'Hello, {}! {} to meet you for the {} time!'.format('Sebastian', 'Nice', 1)

'Hello, {name}! {how} to meet you for the {time} time!'.format(
    name='Sebastian', how='Nice', time=1
)

template = 'Hello, {name}! {how} to meet you for the {time} time!'
template.format(name='Sebastian', how='Nice', time=1)

name='Sebastian'
how='Nice'
time=1
f"Hello, {name}! {how} to meet you for the {time} time!"

# Alignment
'{:<30}'.format('left aligned')
# 'left aligned                  '

'{:>30}'.format('right aligned')
# '                 right aligned'

'{:^30}'.format('centered')
# '           centered           '

'{:*^30}'.format('centered')
# '***********centered***********'

# Floating numbers
'{:.2}'.format(00.1666)
# '0.17'

'{:%}'.format(00.2137)
# '21.370000%'

'{:.2%}'.format(00.2137)
# '21.37%'
