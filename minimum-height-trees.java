class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if(n == 1)
            return Arrays.asList(0);
        
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for(int[] edge: edges) {
            List<Integer> list0;
            List<Integer> list1;

            if(graph.containsKey(edge[0])) {
                list0 = graph.get(edge[0]);
            } else {
                list0 = new ArrayList<>();
            }
            if(graph.containsKey(edge[1])) {
                list1 = graph.get(edge[1]);
            } else {
                list1 = new ArrayList<>();
            }
            
            list0.add(edge[1]);
            list1.add(edge[0]);
            graph.put(edge[0], list0);
            graph.put(edge[1], list1);
        }
        
        List<Integer> leaves = new ArrayList<>();
        for(int i=0; i<n; i++) {
            if(graph.get(i).size() == 1)
                leaves.add(i);
        }

        while(n > 2) {
            n -= leaves.size();
            List<Integer> new_leaves = new ArrayList<>();
            for(int leaf: leaves) {
                int neighbor = graph.get(leaf).get(0);
                graph.get(leaf).remove(0);
                graph.get(neighbor).remove(Integer.valueOf(leaf));

                if(graph.get(neighbor).size() == 1)
                    new_leaves.add(neighbor);
            }

            leaves = new_leaves;
        }

        return leaves;
    }
}