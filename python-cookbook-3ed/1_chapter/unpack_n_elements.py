# You need to unpack N elements from an iterable, but the iterable may be
# longer than N elements, causing a "too many values to unpack" exception.
print()

# Star expressions:
def drop_first_last(grades):
    """
    Drop the first and last homework grades from a semester-long course.
    Return the average of the remaining grades.
    """
    first, *middle, last = grades
    return avg(middle)

# Suppose you have user records with an arbitray number of phone numbers:
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name,'\n', email,'\n', phone_numbers,'\n')

# The starred varibale can also be the first one in the list:
def comparison(sales_record):
    """
    Say you have a sequence of values representing your company's sales figures
    for the last eight quarters.
    You want to see how the most recent quarter compares to the average of the
    first seven quarters.
    """
    *trailing_qtrs, current_qtr = sales_record
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    print('trailing_qtrs:', trailing_qtrs, 'current_qtr:', current_qtr)
    return trailing_avg, current_qtr

print(comparison([10, 8, 7, 1, 9, 5, 10, 3]))
print()
