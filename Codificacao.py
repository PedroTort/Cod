

class Codificacao:
    def __init__(self):
        None

    def string_to_ascii(self, msg):
        values = []
        for char in msg:
          values.append(ord(char))
        string = str(values)
        string = string.replace(',', '')
        string = string.replace('[', '').replace(']', '')
        print(string)
        return string

    def cesar(self,data,key,mode):
        alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'
        new_data = ''
        for c in data:
            index = alphabet.find(c)
            if index == -1:
                new_data += c
            else:
                new_index = index + key if mode == 1 else index - key
                new_index = new_index % len(alphabet)
                new_data += alphabet[new_index:new_index+1]
        return new_data

    def ascii_to_binary(self,ascii):
        values = []
        bit_values = []
         

        for i in ascii_number:
            values.append(f'{i:08b}'.format(8))
        
        values = list(''.join(values))

        for bit in values:
            bit_values.append(int(bit))

        return bit_values
