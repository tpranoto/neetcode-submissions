// Definition for a pair.
// class Pair {
//     int key;
//     String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> quickSort(List<Pair> pairs) {
        return quickSortHelper(pairs,0,pairs.size()-1);
    }

    private List<Pair> quickSortHelper(List<Pair> pairs, int start, int end){
        if (end-start+1<=1){
            return pairs;
        }

        Pair pivot = pairs.get(end);
        int left = start;

        for (int i=start;i<end;i++){
            if (pairs.get(i).key < pivot.key){
                Pair temp = pairs.get(left);
                pairs.set(left,pairs.get(i));
                pairs.set(i, temp);
                left++;
            }
        }
        
        pairs.set(end,pairs.get(left));
        pairs.set(left,pivot);

        quickSortHelper(pairs,start,left-1);
        quickSortHelper(pairs,left+1,end);

        return pairs;
    }
}
