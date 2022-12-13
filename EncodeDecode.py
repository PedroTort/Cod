import pandas as pd


class EncodeDecode:
    def __init__(self):
        None

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

    def string_to_ascii(self, msg):
        values = []
        for char in msg:
          values.append(ord(char))
        string = str(values)
        string = string.replace(',', '').replace('[', '').replace(']', '')
        return string


    def ascii_to_binary(self,ascii):
        # print(ascii)
        bin_values = []
        ascii_array = ascii.split(" ")
        for value in ascii_array:
            binzao = format(int(value), '08b')
            bin_values.append(binzao)
            # print(binzao)
        msg = ''.join(value for value in bin_values)
        print(msg)
        return msg

    def encode_8B6T(self,ascii):
        df = pd.read_csv("./table.csv")
        encoded_list = df['encoded']

        ascii_array=ascii.split(' ')

        encoded_msg = []
        for value in ascii_array:
            index = int(value)
            encoded_msg.append(encoded_list[index])
        msg = ''.join(value for value in encoded_msg)
        return msg


    def ascii_to_string(self, ascii):
        if type(ascii) == str:
            ascii = ascii.split(" ")
        values = ""
        for val in ascii:
            values = values + chr(int(val))
        return values

    def decode_8B6T(self,encoded):
        df = pd.read_csv("./table.csv")
        spaced_array = [encoded[i:i+6] for i in range(0, len(encoded),6)]
        decoded_msg = []

        msg = ''
        for value in spaced_array:
            ascii_value = df[df['encoded'] == value].index[0]
            decoded_msg.append(ascii_value)
        # msg = ''.join(chr(i) for i in decoded_msg)
        # print(msg)
        string = str(decoded_msg)
        string = string.replace(',', '').replace('[', '').replace(']', '')
        # return decoded_msg
        return string


    def get_graph(self,encoded_message):
        values = []
        for c in encoded_message:
            if c == '+':
                values.append(1)
            elif c == '0':
                values.append(0)
            elif c == '-':
                values.append(-1)
        from matplotlib import pyplot as plt
        plt.plot(values)
        plt.show()

a = EncodeDecode()

string = 'Opa, aqui ta uma string'
# print(string)
cesinha = a.cesar(string,3,1)
# print(cesinha)
ascii = a.string_to_ascii(cesinha)
# print(ascii)
bin = a.ascii_to_binary(ascii)
# print(bin)
teste = a.encode_8B6T(ascii)
print(teste)
print()
print()
print()
print()
# spaced_array = [teste[i:i+6] for i in range(0, len(teste),6)]
# print(spaced_array)
decode = a.decode_8B6T(teste)
# print(decode)
bi = a.ascii_to_binary(decode)
asci = a.ascii_to_string(decode)
cezin_2 = a.cesar(asci,3,0)
print(cezin_2)