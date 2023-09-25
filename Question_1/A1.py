file = open('cheeseburger_corollary_1_validation_input.txt', 'r')
burger_list = []
unsplit_list = []
for _ in file.readlines():
    unsplit_list.append(_.replace('\n',''))
split_list = []
for i in range(1, len(unsplit_list)):
    split_list.append(unsplit_list[i].split())

for _ in split_list:
    burger_list.append(_)

for i in burger_list:
    s = int(i[0])
    d = int(i[1])
    k = int(i[2])
    num_s_buns = int(s) * 2 
    num_s_patties = s 
    num_d_buns = int(d) * 2 
    num_d_patties = d * 2 
    buns_reqd = int(k) + 1 
    patties_reqd = k 
    total_patties = num_s_patties + num_d_patties 
    total_buns = num_s_buns + num_d_buns 
    if total_buns >= buns_reqd and total_patties >= patties_reqd:
       print('Case #' + str(burger_list.index(i) + 1) + ': ' + 'YES')
    else: print('Case #' + str(burger_list.index(i) + 1) + ': ' + 'NO')