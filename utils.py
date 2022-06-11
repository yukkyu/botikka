from time import strftime


def printt(text):
    print(strftime("[%H:%M:%S]"), text)


def list_element_exists(elements_list, element):
    index = 1
    for ind in elements_list:
        if ind != element:
            index += 1
    return index == len(elements_list)
