import string # Provides access to string.punctuation



def get_concordance_for_file(file_name: str) -> dict:
    """
    This function generates a concordance for the text found in the given file.
    :param file_name: The name of the file this function processes
    :return: A dictionary representing a concordance for the given file is
    returned.
    """
    f = open(file_name,"r")

    fresh_dic=dict()
    data = []
    while True:
        line = f.readline().lower()
        if line=="":
            break
        words = line.split()
        for word in words:
            data.append(word)
    r = [u.translate({ord(i): None for i in string.punctuation}) for u in data]
    r.sort()
    for index in range(len(r)):
        q = True
        word = r[index]
        for bluh in fresh_dic:
            if(bluh==word):
                fresh_dic[bluh]+=1
                q = False
        if(q): fresh_dic[word]=1

    fresh_dic.pop('')
    f.close()
    # TODO: Implement me correctly.
    return fresh_dic


def save_results_in_file(concordance: dict, filename: str) -> bool:
    """
    This function saves the unique words processed in alphabetical order along
    with their frequencies. For example,

    animal 4
    box 1
    camel 2

    :param concordance: A dictionary of words and their frequencies
    :param filename: The name of the output file where the results are written.
    :return: True if the file had data written to it, False otherwise.
    """
    alpha = []
    f=open(filename,"w")

    for key in concordance:
        alpha.append(key)
        alpha.sort()
    for index in alpha:
        word = index
        value = concordance[index]
        f.write(word + ": " + str(value)+"\n")


    f.close()

    # TODO: Implement me correctly.
    return False
