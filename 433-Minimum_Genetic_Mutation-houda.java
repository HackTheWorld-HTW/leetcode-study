import java.util.*;

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {

        Set<String> set = new HashSet<>(Arrays.asList(bank));
        if (!set.contains(endGene)) return -1; 
        
        Queue<String> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        
        q.offer(startGene);
        visited.add(startGene);

        int mutations = 0;
        char[] choices = {'A', 'C', 'G', 'T'}; 

        while (!q.isEmpty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; i++) {
                String gene = q.poll();
                if (gene.equals(endGene)) return mutations; 

                char[] geneArr = gene.toCharArray();
                for (int j = 0; j < geneArr.length; j++) {
                    char original = geneArr[j];
                    for (char c : choices) {
                        if (c == original) continue;

                        geneArr[j] = c;
                        String newGene = new String(geneArr);

                        if (set.contains(newGene) && !visited.contains(newGene)) {
                            q.offer(newGene);
                            visited.add(newGene);
                        }
                    }
                    geneArr[j] = original;
                }
            }
            mutations++; 
        }
        return -1;
    }
}
