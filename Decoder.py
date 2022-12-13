import pandas as pd


class Decoder:
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

    def ascii_to_string(self, msg):
        values = []
        for char in msg:
          values.append(ord(char))
        string = str(values)
        string = string.replace(',', '').replace('[', '').replace(']', '')
        print(string)
        return string



    def binary_to_ascc(self,ascii):
        bin_values = []
        ascii_array = ascii.split(" ")
        for value in ascii_array:
            binzao = format(int(value), '08b')
            bin_values.append(binzao)
            print(binzao)
        msg = ''.join(value for value in bin_values)
        print(msg)
        return msg

    def decode_8B6T(self,ascii):
        df = pd.read_csv("./table.csv")

        decoded_msg = []

        msg = ''
        for value in ascii:
            ascii_value = df[df['encoded'] == value].index[0]
            decoded_msg.append(ascii_value)
        msg = ''.join(chr(i) for i in decoded_msg)
        print(msg)
        return msg


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
