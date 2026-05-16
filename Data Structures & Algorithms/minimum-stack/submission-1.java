class MinStack {

    List<Integer> list;
    public MinStack() {
        this.list = new ArrayList();
    }
    
    public void push(int val) {
        list.add(val);
    }
    
    public void pop() {
        if(!list.isEmpty()) list.remove(list.size() - 1);
    }
    
    public int top() {  
        return list.get(list.size() - 1);
    }
    
    public int getMin() {
        int min = Integer.MAX_VALUE;
        for(int i : list){
            if(i < min) min = i;
        }
        return min;
    }
}
