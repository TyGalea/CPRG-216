ITS = {'CMPH-209', 'COMM-238', 'CPNT-219', 'CPRG-216', 'MATH-237', 'CPNT-224', 'CPRG-217', 'CPSY-204', 'CPSY-206', 'PHIL-241'}
SD = {'CPRG-213', 'COMM-238', 'CPNT-217', 'CPRG-216', 'MATH-237', 'CPRG-211', 'CPRG-250', 'CPSY-200', 'CPSY-202', 'PHIL-241'}
print("Common 1st Year Courses:")
for course in ITS & SD:
    print("    ", course)
print("\nITS-only 1st Year Courses:")
for course in ITS - SD:
    print("    ", course)

print("\nSD-only 1st Year Courses:")
for course in SD - ITS:
    print("    ", course)