import pandas as pd


class Encode_decode:
    def __init__(self, msg):
        self.msg = msg

    def encode_8b6t(self):
        df = pd.read_csv("./table.csv")
        encoded_list = df['encoded']

        encoded_msg = []
        for value in self.msg:
            index = int(value)
            encoded_msg.append(encoded_list[index])
        print(encoded_msg)
        return encoded_msg
    
    def decode_8b6t(self, encoded_msg):
        df = pd.read_csv("./table.csv")
        decoded_msg = []
        msg = ''
        for value in encoded_msg:
            ascii_value = df[df['encoded'] == value].index[0]
            decoded_msg.append(ascii_value)
        msg = ''.join(chr(i) for i in decoded_msg)
        print(msg)
        return msg

msg = [116, 101, 115, 116, 101, 44, 32, 111, 112, 97, 32, 49, 50, 33]
encoded_msg = ['000+0-', '++0-00', '000+00', '000+0-', '++0-00', '0++--0', '-++-00', '++0--+', '000++-', '+0+-00', '-++-00', '0+--+0', '0+-0-+', '+00+--']
a = Encode_decode(msg)
encoded = a.encode_8b6t()
encoded = a.decode_8b6t(encoded_msg)