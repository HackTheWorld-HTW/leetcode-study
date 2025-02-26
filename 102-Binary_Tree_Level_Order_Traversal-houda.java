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
    public List<List<Integer>> levelOrder(TreeNode root) {
    
        Queue<TreeNode> q = new LinkedList<>();
        List<List<Integer>> out = new ArrayList<>();

        if(root==null) return out;

        q.offer(root);

        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> nodes = new ArrayList<>();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = q.poll();
                nodes.add(node.val);

                if (node.left != null) q.offer(node.left);
                if (node.right != null)q.offer(node.right);
            }
            out.add(nodes);
        }
        return out;
    }
}
