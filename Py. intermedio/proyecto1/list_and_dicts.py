def run():

    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'Genus':'Tectona', 'Species': 'grandis'}

    super_list =[
        {'Genus':'Tectona', 'Species': 'grandis'},
        {'Genus':'Cariniana', 'Species': 'puriformis'},
        {'Genus':'Calophyllum', 'Species': 'mariae'},
        {'Genus':'Anacardium', 'Species': 'excelsum'},
        {'Genus':'Aniba', 'Species': 'perutilis'},
        {'Genus':'Dipteris', 'Species': 'panamensis'}

    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5,6],
        "integer_nums" : [-1, -2, 0, 1, 2],
        "floating" : [1.1, 2.3, 4.6, 6.73]

    }

    for key, value in super_dict.items():
        print(key, ">", value)



if __name__=='__main__':
    run()


