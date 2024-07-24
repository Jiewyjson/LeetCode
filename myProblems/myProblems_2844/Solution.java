package myProblems.myProblems_2844;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumOperations(String num) {
        int ans = num.contains("0") ? num.length() - 1 : num.length();
        var ends = new String[]{"00", "25", "50", "75"};
        for (var end : ends) {
            ans = Math.min(ans, help(num, end));
        }
        return ans;
    }
    int help(String num,String end){
        var i = end.charAt(1);
        var j = end.charAt(0);
        int idx_i = num.lastIndexOf(i);
        if (idx_i <= 0)return num.length();
        int idx_j = num.lastIndexOf(j, idx_i - 1);
        if (idx_j < 0)return num.length();
        else return num.length() - idx_j - 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String num = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minimumOperations(num));
    }
}
