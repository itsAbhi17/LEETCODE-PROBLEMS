public class Solution {
    public int lengthOfLastWord(String s) {
        
        String[] words = s.trim().split(" ");

        return words[words.length - 1].length();
    }


    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLastWord("Hello World"));
        System.out.println(sol.lengthOfLastWord("   fly me   to   the moon  ")); 
        System.out.println(sol.lengthOfLastWord("luffy is still joyboy")); 
    }
}
