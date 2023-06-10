class Word2String:
    
    def __init__(self) -> None:
        pass

    def _word_2_2Dbyte(self, element : int) -> tuple:
        '''
        Returns the tuple of 2 bytes
        print(_word_2_2Dbyte(18498))
        (66, 72)
        '''
        c = (int(element) >> 8) & 0xff
        b = int(element) & 0xff
        return b,c
    
    def word2string(self, word_list : list) -> str:

        '''
        provide the list of 16 bit decimal values (0-65535) equivalent to 2 byte ASCII Codes and it will return a String 

        lst = ['18498','21057','22340','19009']
        w2s = Word2String()
        print(w2s.word2string(lst))
        'BHARDWAJ'
        '''
        
        byte_list_2d = [self._word_2_2Dbyte(i) for i in word_list]
        chr_list = [chr(j) for s in byte_list_2d for j in s]
        return ''.join(chr_list)