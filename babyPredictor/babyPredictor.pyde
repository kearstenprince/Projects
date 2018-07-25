from random import *

birthMonth = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
birthDate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
birthYear = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029,2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040]
[1990, 1991, 1992,1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
2015, 2016, 2017, 2018]

febMonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
miniMonth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
shortMonth = ['April', 'June', 'September', 'November']


print 'When will you have a baby?'


chosen = choice(birthMonth)
if chosen == birthMonth[1]:
 print chosen + ' ' + str(choice(febMonth)) + ' ' + str(choice(birthYear))
if chosen in shortMonth:
 print chosen + ' ' + str(choice(miniMonth)) + ' ' + str(choice(birthYear))
else:
 print chosen + ' ' + str(choice(birthDate)) + ' ' + str(choice(birthYear))
