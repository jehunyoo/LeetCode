class Solution:
    # simple solution
    def validUtf8(self, data: List[int]) -> bool:
        def validate(size):
            for i in range(index + 1, index + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True
        
        index = 0
        while index < len(data):
            head = data[index]
            if (head >> 5) == 0b110 and validate(1): #2bytes
                index +=2
            elif (head >> 4) == 0b1110 and validate(2): #3bytes
                index += 3
            elif (head >> 3) == 0b11110 and validate(3): #4bytes
                index += 4
            elif (head >> 7) == 0b0:
                index += 1
            else:
                return False
        return True
        
    def validUtf8(self, data: List[int]) -> bool:
        byte = 0
        for datum in data:
            ms1b = bin(datum & 0xFF)[2:].zfill(8)[0] == '1'
            ms2b = bin(datum & 0xFF)[2:].zfill(8)[:2] == '10'
            if not ms1b and not byte:
                continue
            elif ms2b and byte:
                byte -= 1
                continue
            elif ms1b and not ms2b and not byte:
                while bin(datum & 0xFF)[2:].zfill(8)[-8] == '1':
                    byte += 1
                    datum <<= 1
                if not 2 <= byte <= 4:
                    return False
                byte -= 1
            else:
                return False
        
        if byte:
            return False
        else:
            return True