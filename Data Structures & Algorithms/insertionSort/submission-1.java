// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> result = new ArrayList<List<Pair>>();
        if (pairs.size() == 0){
            return result;
        }
        
        result.add(new ArrayList<Pair>(pairs));

        for (int idx = 1; idx < pairs.size();idx++){
            int iterator = idx -1;
            while(iterator >=0 && pairs.get(iterator+1).key < pairs.get(iterator).key){
                Pair temp = pairs.get(iterator+1);
                pairs.set(iterator+1, pairs.get(iterator));
                pairs.set(iterator,temp);
                iterator--;
            }

            result.add(new ArrayList<Pair>(pairs));
        }

        return result;
    }
}
