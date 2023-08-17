/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int maxDiff = 0;

    public boolean isBalanced(TreeNode root) {
        getHeight(root);
        return maxDiff <= 1? true: false;
    }
    public int getHeight(TreeNode node) {
        if(node == null)
            return 0;
        
        int left = getHeight(node.left) + 1;
        int right = getHeight(node.right) + 1;
        maxDiff = Math.max(maxDiff, Math.abs(left - right));
        return Math.max(left, right);
    }
}