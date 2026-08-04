// Definition for a pair.
// class Pair {
//     public int key;
//     public String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> mergeSort(List<Pair> pairs) {
        return mergeSort(pairs,0,pairs.size()-1);
    }

    private List<Pair> mergeSort(List<Pair> pairs, int startingIdx, int endingIdx){
        if (endingIdx-startingIdx+1 <=1){
            return pairs;
        }

        int midpointIdx = (startingIdx+endingIdx)/2;
        mergeSort(pairs,startingIdx,midpointIdx);
        mergeSort(pairs,midpointIdx+1,startingIdx);

        merge(pairs,startingIdx,midpointIdx,endingIdx);

        return pairs;
    }

    private void merge(List<Pair> pairs, int startingIdx, int midpointIdx, int endingIdx){
        List<Pair> leftSub = new ArrayList<>(pairs.subList(startingIdx,midpointIdx+1));
        for (int i= 0; i<leftSub.size();i++){
            System.out.print(leftSub.get(i).key);
        }
        System.out.println();

        List<Pair> rightSub = new ArrayList<>(pairs.subList(midpointIdx+1,endingIdx+1));
        for (int i= 0; i<rightSub.size();i++){
            System.out.print(rightSub.get(i).key);
        }
        System.out.println();

        int leftIdx = 0;
        int rightIdx = 0;
        int currentIdx = startingIdx;
        while(leftIdx < leftSub.size() || rightIdx < rightSub.size() ){
            if (leftIdx >= leftSub.size()){
                pairs.set(currentIdx,rightSub.get(rightIdx));
                rightIdx++;
            }else if (rightIdx >= rightSub.size()){
                pairs.set(currentIdx, leftSub.get(leftIdx));
                leftIdx++;
            }else if(leftSub.get(leftIdx).key <= rightSub.get(rightIdx).key){
                pairs.set(currentIdx, leftSub.get(leftIdx));
                leftIdx++;
            }else{
                pairs.set(currentIdx,rightSub.get(rightIdx));
                rightIdx++;
            }
            currentIdx++;
        }
    }
}
