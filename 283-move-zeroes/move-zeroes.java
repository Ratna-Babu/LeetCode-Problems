class Solution {
    public void moveZeroes(int[] nums) {
     int leftPointer=0;
     int i;
     for(i=0;i<nums.length;i++){
        if (nums[i]!=0){
            nums[leftPointer]=nums[i];
            leftPointer++;
        }
     }
     for(i=leftPointer;i<nums.length;i++){
        nums[i] = 0;
     }   
     
    }
}