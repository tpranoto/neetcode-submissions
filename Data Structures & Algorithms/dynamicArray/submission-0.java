class DynamicArray {
    int[] buffer;
    int cursor;

    public DynamicArray(int capacity) {
        this.buffer = new int[capacity];
        this.cursor = 0;
    }

    public int get(int i) {
        return this.buffer[i];
    }

    public void set(int i, int n) {
        this.buffer[i]=n;
    }

    public void pushback(int n) {
        if(this.cursor == this.buffer.length){
            resize();
        }
        this.buffer[cursor] = n;
        cursor++;
    }

    public int popback() {
        return this.buffer[--cursor];
    }

    private void resize() {
        int[] newBuffer = new int[this.buffer.length*2];
        for(int idx = 0; idx<this.buffer.length;idx++){
            newBuffer[idx] = this.buffer[idx];
        }

        this.buffer = newBuffer;
    }

    public int getSize() {
        return cursor;
    }

    public int getCapacity() {
        return this.buffer.length;
    }
}
