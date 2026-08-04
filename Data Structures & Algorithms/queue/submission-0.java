class Deque {
    class Node{
        int val;
        Node next;
        Node prev;

        public Node(int val,Node next,Node prev){
            this.val = val;
            this.next = next;
            this.prev = prev;
        }
    }
    Node head;
    Node tail;

    public Deque() {
        this.head = null;
        this.tail = null;
    }

    public boolean isEmpty() {
        return this.head ==null && this.tail == null;
    }

    public void append(int value) {
        if (this.tail ==null){
            this.tail = new Node(value,null,null);
            this.head = this.tail;
            return;
        }
        Node newNode = new Node(value,null,this.tail);
        this.tail.next = newNode;
        this.tail = this.tail.next;
    }

    public void appendleft(int value) {
        if (this.head == null){
            this.head = new Node(value, null,null);
            this.tail = this.head;
            return;
        }

        Node newNode = new Node(value,this.head,null);
        this.head.prev = newNode;
        this.head = this.head.prev;
    }

    public int pop() {
        if (this.tail ==null){
            return -1;
        }
        Node popped = this.tail;
        this.tail = this.tail.prev;
        if (this.tail !=null){
            this.tail.next = null;
        }else{
            this.head = this.tail;
        }
        return popped.val;
    }

    public int popleft() {
        if(this.head == null){
            return -1;
        }
        Node popped = this.head;
        this.head = this.head.next;
        if(this.head !=null){
            this.head.prev = null;
        }else{
            this.tail = this.head;
        }
        return popped.val;
    }
}
