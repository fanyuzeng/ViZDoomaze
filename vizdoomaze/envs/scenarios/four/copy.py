
old_file = open('../one/one_1.cfg', mode='r')
lines = old_file.readlines()
for index in range(1,21):
    new_file = open('four_{}.cfg'.format(index), mode='w')
    for line in lines:
        if 'doom_scenario_path' in line:
            line = "doom_scenario_path = four_{}.wad".format(index)
        new_file.write(line)
    new_file.close()
old_file.close()