class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num = bin(n)[2:].zfill(32)
        binary_num_reversed = binary_num[::-1]
        return int(binary_num_reversed, 2)