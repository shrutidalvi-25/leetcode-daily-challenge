class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> list = new ArrayList<>();

        for (int i = 1; i <= nums.length; i++) {
            boolean found = false;
            for (int n : nums)
                if (n == i) found = true;
            if (!found) list.add(i);
        }

        return list;
    }
}
