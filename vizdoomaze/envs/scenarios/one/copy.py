
old_file = open('one_1.cfg', mode='r')
lines = old_file.readlines()
for index in range(2,21):
    new_file = open('one_{}.cfg'.format(index), mode='w')
    for line in lines:
        if 'doom_scenario_path' in line:
            line = "doom_scenario_path = one_{}.wad".format(index)
        new_file.write(line)
    new_file.close()
old_file.close()