class LinkedList {
    class Node{
        int value;
        Node next;

        public Node(int val, Node next){
            this.value = val;
            this.next = next;
        }
    }
    Node head;
    Node tail;

    public LinkedList() {
        this.head = null;
        this.tail = null;
    }

    public int get(int index) {
        if (this.head ==null){
            return -1;
        }
        Node nodeAtIdx = this.head;
        int idx = 0;
        for (;idx <index && nodeAtIdx.next !=null;idx++){
            nodeAtIdx = nodeAtIdx.next;
        }

        if (nodeAtIdx.next == null && idx<index){
            return -1;
        }

        return nodeAtIdx.value;
    }

    public void insertHead(int val) {
        Node newHead = new Node(val,this.head);
        this.head = newHead;
        if (this.tail == null){
            this.tail = this.head;
        }
    }

    public void insertTail(int val) {
        Node newTail = new Node(val,null);
        if (this.tail == null){
            this.tail = newTail;
            this.head = this.tail;
        }else{
            this.tail.next = newTail;
            this.tail = newTail;
        }
    }

    public boolean remove(int index) {
        if (this.head == null){
            return false;
        }

        if (index == 0 && this.head == this.tail){
            this.head =null;
            this.tail =null;
            return true;
        }

        if (index == 0){
            this.head = this.head.next;
            return true;
        }

        int idx = 0;
        Node it = this.head;
        while(idx<index-1&&it!=null){
            idx++;
            it =it.next;
        }

        if (it!=null && it.next !=null){
            if (it.next == this.tail){
                this.tail = it;
            }
                it.next = it.next.next;
            return true;
        }

        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> result = new ArrayList<>();
        if (this.head==null) {
        	return result;
        }
        for(Node it=this.head;it!=null;it=it.next){
            result.add(it.value);
        }
        return result;
    }
}
