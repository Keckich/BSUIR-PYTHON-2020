import script
import tempfile


def file_size(file):
    size = sum(1 for line in file)
    return size


def sort(filename):
    flag = False
    file1_block = []
    file2_block = []
    length = 0
    with open(filename) as file:
        size = file_size(file)
        file1 = tempfile.TemporaryFile(mode='w+')
        file2 = tempfile.TemporaryFile(mode='w+')
        for i in range(size - 1):
            file.seek(0)
            line1 = int(file.readlines()[i])
            file.seek(0)
            line2 = int(file.readlines()[i + 1])
            if line1 <= line2:
                file.seek(0)
                line = (file.readlines()[i])
                if flag:
                    file2.write(line)
                else:
                    file1.write(line)
                length += 1
            else:
                length += 1
                file.seek(0)
                line = (file.readlines()[i])
                if flag:

                    file2.write(line)
                    file2_block.append(length)
                else:

                    file1.write(line)
                    file1_block.append(length)
                flag = not flag
                length = 0

        file.seek(0)
        length += 1
        if flag:
            file2.write((file.readlines()[-1]))
            file2_block.append(length)
        else:
            file1.write((file.readlines()[-1]))
            file1_block.append(length)

        if not file2_block:
            file1.close()
            file2.close()
            return True
        else:
            block = []
            j = 0
            i = 0
            k = 0
            script.new_file(filename, '', 'w')
            while size > 0:
                tmp1 = i
                tmp2 = k
                if j < len(file1_block):
                    while i < file1_block[j] + tmp1:
                        file1.seek(0)
                        block.append(int(file1.readlines()[i]))
                        i += 1
                if j < len(file2_block):
                    while k < file2_block[j] + tmp2:
                        file2.seek(0)
                        block.append(int(file2.readlines()[k]))
                        k += 1

                j += 1
                block = sorted(block)
                script.new_file(filename, block)
                size -= len(block)
                block = []
            file1.close()
            file2.close()
            return False


def external_sort(filename):
    script.sort_file(filename)
    ex_sort = sort(filename)
    while ex_sort is not True:
        ex_sort = sort(filename)


if __name__ == '__main__':
    external_sort('numbers')
