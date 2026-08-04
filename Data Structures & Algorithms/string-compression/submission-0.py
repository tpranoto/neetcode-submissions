class Solution:
    def compress(self, chars: List[str]) -> int:
        left_ptr = 0
        right_ptr = 0

        while right_ptr < len(chars):
            chars[left_ptr] = chars[right_ptr]
            left_ptr += 1
            cons_ptr = right_ptr+1

            while cons_ptr < len(chars) and chars[right_ptr] == chars[cons_ptr]:
                cons_ptr +=1
            
            if cons_ptr - right_ptr > 1:
                for c in str(cons_ptr - right_ptr):
                    chars[left_ptr] = c
                    left_ptr += 1
                
            right_ptr = cons_ptr
        return left_ptr
