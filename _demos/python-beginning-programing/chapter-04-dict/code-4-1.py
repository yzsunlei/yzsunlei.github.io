#!/usr/lib/env python
# coding=utf-8
# a dict for user's phone and address
# output: Beth's address is Bar street 42. or Beth's phone number is 9102.

people = {

    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }

}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = raw_input('Name: ')

# Are we looking for a phone number or an address?
request = raw_input('Phone number (p) or address (a)? ')

# Use the correct key:
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Only try to print information if the name is a valid key in
if name in people: print "%s's %s is %s." % \
    (name, labels[key], people[name][key])

# you also can use get to provide a default value here
# if name in people:
#     print name
#     currPeople = people[name]
#     print currPeople.get('phone')
#     print currPeople.get('addr')
