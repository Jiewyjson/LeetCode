package myProblems.myProblems_2740;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findValueOfPartition(int[] nums) {
        Arrays.sort(nums);
        int ans = 0x3f3f3f3f;
        for(int i = 0; i < nums.length - 1; i++)
            ans = Math.min(ans,nums[i + 1] - nums[i]);
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(findValueOfPartition(nums));
    }
}
