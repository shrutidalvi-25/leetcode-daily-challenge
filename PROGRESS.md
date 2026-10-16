# Progress Log

Starting this challenge from zero — no LeetCode problems solved before Day 1.
The goal is 1 problem/day, in Java, from true beginner fundamentals up through
advanced interview-level topics. Every row below is a real problem solved
myself.

Rows are appended automatically by `tools/complete_day.py` — don't hand-edit the
table below unless you're fixing a mistake.

| Day | Date | Problem | Difficulty | Approach/Rationale | Time/Space Complexity | Solution Link |
|---|---|---|---|---|---|---|
| 1 | 2026-08-16 | Two Sum | Easy | Brute-force nested loop checking every pair for target sum. | O(n^2) / O(1) | [day-001-two-sum.java](solutions/day-001-two-sum.java) |
| 2 | 2026-08-16 | Valid Anagram | Easy | Sorted both char arrays and compared for equality after an early length check. | O(n log n) / O(n) | [day-002-valid-anagram.java](solutions/day-002-valid-anagram.java) |
| 3 | 2026-08-17 | Contains Duplicate | Easy | Used a HashSet, adding each number and checking membership before insert; return true on first repeat, false if loop completes. | O(n) / O(n) | [day-003-contains-duplicate.java](solutions/day-003-contains-duplicate.java) |
| 4 | 2026-08-17 | Valid Palindrome | Easy | Lowercased and stripped non-alphanumeric characters via regex, then compared the string to its reversed StringBuilder form. | O(n) / O(n) | [day-004-valid-palindrome.java](solutions/day-004-valid-palindrome.java) |
| 5 | 2026-08-18 | Reverse String | Easy | Two-pointer in-place swap from both ends toward the middle. | O(n) / O(1) | [day-005-reverse-string.java](solutions/day-005-reverse-string.java) |
| 6 | 2026-08-20 | Best Time to Buy and Sell Stock | Easy | one-pass min-price tracking, update max profit as we scan | O(n) / O(1) | [day-006-best-time-to-buy-and-sell-stock.java](solutions/day-006-best-time-to-buy-and-sell-stock.java) |
| 7 | 2026-08-20 | Majority Element | Easy | Boyer-Moore Voting Algorithm - track a candidate and a running count; reset candidate when count hits 0, increment/decrement based on match | O(n) / O(1) | [day-007-majority-element.java](solutions/day-007-majority-element.java) |
| 8 | 2026-08-21 | Move Zeroes | Easy | Two-pointer/index technique: scan and shift non-zero elements to the front, then fill the remaining tail with zeroes. | O(n) / O(1) | [day-008-move-zeroes.java](solutions/day-008-move-zeroes.java) |
| 9 | 2026-08-22 | Plus One | Easy | Two-pointer digit increment from the end with carry propagation; if all digits are 9, allocate new array of length+1 with leading 1 | O(n) / O(1) average, O(n) only for all-9s overflow case | [day-009-plus-one.java](solutions/day-009-plus-one.java) |
| 10 | 2026-08-23 | Remove Duplicates from Sorted Array | Easy | Two-pointer: 'unique' marks the write position for the next unseen value; scan array and copy any element that differs from the last unique one, since the array is sorted duplicates are always adjacent. | O(n) / O(1) | [day-010-remove-duplicates-from-sorted-array.java](solutions/day-010-remove-duplicates-from-sorted-array.java) |
| 11 | 2026-08-24 | Remove Element | Easy | two-pointer: k tracks write position for next kept element, overwrite in place when nums[i] != val | O(n) / O(1) | [day-011-remove-element.java](solutions/day-011-remove-element.java) |
| 12 | 2026-08-25 | Merge Sorted Array | Easy | copy nums2's elements into the empty tail of nums1, then sort the whole array with Arrays.sort() | O((m+n) log(m+n)) / O(1) extra | [day-012-merge-sorted-array.java](solutions/day-012-merge-sorted-array.java) |
| 13 | 2026-08-26 | Squares of a Sorted Array | Easy | square each element then sort (built-in sort, not two-pointer) | O(n log n) / O(n) | [day-013-squares-of-a-sorted-array.java](solutions/day-013-squares-of-a-sorted-array.java) |
| 14 | 2026-08-27 | Single Number | Easy | Brute-force double loop counting occurrences of each element. | O(n^2) / O(1) | [day-014-single-number.java](solutions/day-014-single-number.java) |
| 15 | 2026-08-29 | Intersection of Two Arrays II | Easy | HashMap counts occurrences in nums1, then scan nums2 decrementing counts to collect matches | O(n + m) / O(min(n, m)) | [day-015-intersection-of-two-arrays-ii.java](solutions/day-015-intersection-of-two-arrays-ii.java) |
| 16 | 2026-08-30 | Pascal's Triangle | Easy | Row-by-row build: each row starts as all 1s, then interior values are the sum of the two values above (a[i-1][j-1] + a[i-1][j]). | O(numRows^2) / O(numRows^2) | [day-016-pascals-triangle.py](solutions/day-016-pascals-triangle.py) |
| 17 | 2026-08-31 | Roman to Integer | Easy | if/else chain to map symbol to value, subtract when current symbol < next symbol (handles subtractive cases IV/IX/XL/XC/CD/CM naturally) | O(n) / O(1) | [day-017-roman-to-integer.java](solutions/day-017-roman-to-integer.java) |
| 18 | 2026-09-08 | Longest Common Prefix | Easy | shrink candidate prefix from strs[0] char-by-char until every string starts with it | O(n*m) worst case / O(1) extra | [day-018-longest-common-prefix.java](solutions/day-018-longest-common-prefix.java) |
| 19 | 2026-09-11 | Find the Index of the First Occurrence in a String | Easy | used Java's built-in String.indexOf(needle) to find the first occurrence directly | O(n*m) worst case / O(1) extra | [day-019-find-the-index-of-the-first-occurrence-in-a-string.java](solutions/day-019-find-the-index-of-the-first-occurrence-in-a-string.java) |
| 20 | 2026-09-12 | Length of Last Word | Easy | Walk backwards from the end: skip trailing spaces, then count characters until the next space or start of string | O(n) / O(1) | [day-020-length-of-last-word.java](solutions/day-020-length-of-last-word.java) |
| 21 | 2026-09-12 | Isomorphic Strings | Easy | Two int arrays (size 256) storing last-seen index+1 per char position in s and t; mismatch if timestamps differ, ensures consistent 1-1 mapping | O(n) / O(1) | [day-021-isomorphic-strings.java](solutions/day-021-isomorphic-strings.java) |
| 22 | 2026-09-13 | Ransom Note | Easy | HashMap-style int[26] frequency count of magazine chars, then decrement while scanning ransomNote (return false on zero count) | O(n+m) / O(1) | [day-022-ransom-note.java](solutions/day-022-ransom-note.java) |
| 23 | 2026-09-13 | First Unique Character in a String | Easy | int[26] frequency count of chars, then scan again returning first index with count 1 | O(n) / O(1) | [day-023-first-unique-character-in-a-string.java](solutions/day-023-first-unique-character-in-a-string.java) |
| 24 | 2026-10-16 | Add Binary | Easy | Two pointers from the end of both strings, adding digits plus carry; append sum%2 to a StringBuilder, carry=sum/2, reverse at the end. | O(max(m, n)) / O(max(m, n)) | [day-024-add-binary.java](solutions/day-024-add-binary.java) |
<!-- COMPLETE_DAY_INSERT_MARKER -->

## Redo log

Every ~6 months, redo one early problem (Day 1-20 range) from scratch and log it
here side-by-side with the original. This is the single most convincing "growth"
proof for interviews — visible before/after on your own timeline.

| Redo Date | Original Day | Problem | Original Solution | Redo Solution | What changed / why |
|---|---|---|---|---|---|
| | | | | | |

## Feedback log

Roughly every 2-3 weeks, review recurring mistakes or patterns you keep missing
and note what you changed as a result. Self-practice alone plateaus — this is
what prevents that.

| Date | Topic / Pattern | What went wrong | What I changed |
|---|---|---|---|
