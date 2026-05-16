class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int n: nums){
                int curr = map.getOrDefault(n,0);
                map.put(n,curr+1);
        }
        List<Integer>[] buckets= new List[nums.length+1]; 
        for(int key: map.keySet()){
           if(buckets[map.get(key)]==null){
            buckets[map.get(key)] = new ArrayList<>();
           }
           buckets[map.get(key)].add(key);
        }
        
        int[] res = new int[k];
        int index = 0;
        for(int i = buckets.length - 1; i >= 0 ; i--){
            if(buckets[i] != null){
                for(int val: buckets[i]){
                    res[index++] = val;
                    if(index == k) return res;
                }
            }
        }
        return res;


    }
}
