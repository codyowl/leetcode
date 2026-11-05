class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # the idea here is to take each charcter of the two string and fiding the replacement relationship between them 
        # egg -> add (e->a, g->d, g->d)
        s_character_match_with_t = dict()
        t_character_match_with_s = dict()
        # taking the index
        index = 0
        while index < len(s):
            s_character = s[index]
            t_character = t[index]
            if s_character in s_character_match_with_t:
                if s_character_match_with_t[s_character] != t_character:
                    return False
            else:
                s_character_match_with_t[s_character] = t_character
            # now doing the reverse for fiding the replacement relationship
            if t_character in t_character_match_with_s:
                if t_character_match_with_s[t_character] != s_character:
                    return False
            else:
                t_character_match_with_s[t_character] = s_character
            index += 1        
        return True