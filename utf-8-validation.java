class Solution {
    public boolean validUtf8(int[] data) {
        int index = 0;
        int length = 0;
        boolean head = true;

        int msb = 0b10000000;
        while(index < data.length) {
            int octet = data[index];
            
            if(head) {
                if((octet & msb) == 0) {
                    index++;
                } else {
                    int l = 0;
                    while(((octet << l) & msb) == msb) {
                        l++;
                    }
                    length = l;

                    if(2 <= l && l <= 4) {
                        index++;
                        head = false;
                    }
                    else
                        return false;
                }

            } else {
                if(octet >> 6 == 0b10) {
                    index++;
                    length--;
                    if(length == 1) {
                        length--;
                        head = true;
                    }
                }
                else
                    return false;
            }
        }

        if(length == 0)
            return true;
        else
            return false;
    }
}