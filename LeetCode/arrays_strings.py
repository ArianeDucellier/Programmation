from math import floor, log10

def firstUniqChar(s):
    """
    """
    letters = []
    unique = []
    for letter in s:
        if letter in letters:
            if letter in unique:
                unique.remove(letter)
        else:
            unique.append(letter)
            letters.append(letter)
    if (len(unique) == 0):
        return -1
    else:
        return s.find(unique[0])

def number2words(number):
    """
    """
    units = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    dozen = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    size = int(floor(log10(number)))
    result = ''
    for i in range(0, size + 1):
        n = str(number)[i]
        if n != '0':
            if ((i - size) % 3 == 0):
                if (i == 0) or (str(number)[i - 1] != '1'):
                    result = result + ' ' + units[int(n) - 1]
            elif ((i - size) % 3 == 2):
                if (n == '1'):
                    nn = str(number)[i + 1]
                    result = result + ' ' + teens[int(nn) - 1]
                else:
                    result = result + ' ' + dozen[int(n) - 1]
            else:
                result = result + ' ' + units[int(n) - 1]
        if ((i - size) % 3 == 1):
            result = result + ' Hundred'
        if (i == size - 3):
            result = result + ' Thousand'
        if (i == size - 6):
            result = result + ' Million'
        if (i == size - 9):
            result = result + ' Billion'
    return result[1:]
