class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Step 1: copy nums2's elements into the empty tail of nums1
        for (int i = 0; i < n; i++) {
            nums1[m + i] = nums2[i];
        }

        // Step 2: sort the whole array
        Arrays.sort(nums1);
    }
}
