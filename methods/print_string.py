def print_string_from_file(file_path, number):
    if not isinstance(file_path, str):
        raise TypeError('Not valid type for file path.')
    elif not isinstance(number, int):
        raise TypeError('Not valid type for param. Expected to be integer.')
    elif number <= 0:
        raise ArithmeticError('Number suppose to be more than zero')

    with open(file_path) as f:
        lines = [line.strip() for line in f]

    file_lengths = len(lines)
    if file_lengths == 0:
        raise Exception('File is empty')
    elif file_lengths < number:
        raise Exception(f'The number lines in file les that given number. Lines in file: {file_lengths}, '
                        f'given number: {number}')
    last_lines = lines[-number:]
    print(last_lines)


def return_files_lines(file_path, number):
    """
    Method only for test purposes returns N last lines from file in string format
    :param file_path: path to file
    :param number: number of lines which are needed to return
    :return: N last lines from file
    """
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    last_lines = lines[-number:]
    return str(last_lines)
