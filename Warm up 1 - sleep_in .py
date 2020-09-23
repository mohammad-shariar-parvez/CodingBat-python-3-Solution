from calendar import weekday

#you can avoid the above line (1)
#if you follow check next comment line

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
main =(sleep_in(weekday==False,vacation=True))

# or main =(sleep_in(weekday=0,vacation=1))
#because we know that (0/None) value represent False
#and (non-zero 1/2/3 & not None value represent True

print(main)
