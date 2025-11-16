import java.util.LinkedList;
import java.util.Queue;

// Shared buffer class
class SharedBuffer {
    private Queue<Integer> buffer;
    private int capacity;
    
    public SharedBuffer(int capacity) {
        this.buffer = new LinkedList<>();
        this.capacity = capacity;
    }
    
    // Synchronized produce method
    public synchronized void produce(int value) throws InterruptedException {
        // Wait if buffer is full
        while (buffer.size() == capacity) {
            System.out.println("Buffer is full. Producer is waiting...");
            wait();
        }
        
        buffer.add(value);
        System.out.println("Produced: " + value + " | Buffer size: " + buffer.size());
        
        // Notify consumer that item is available
        notifyAll();
    }
    
    // Synchronized consume method
    public synchronized int consume() throws InterruptedException {
        // Wait if buffer is empty
        while (buffer.isEmpty()) {
            System.out.println("Buffer is empty. Consumer is waiting...");
            wait();
        }
        
        int value = buffer.poll();
        System.out.println("Consumed: " + value + " | Buffer size: " + buffer.size());
        
        // Notify producer that space is available
        notifyAll();
        return value;
    }
}

// Producer thread
class Producer extends Thread {
    private SharedBuffer buffer;
    private int itemsToProduce;
    
    public Producer(SharedBuffer buffer, int itemsToProduce) {
        this.buffer = buffer;
        this.itemsToProduce = itemsToProduce;
    }
    
    @Override
    public void run() {
        try {
            for (int i = 1; i <= itemsToProduce; i++) {
                buffer.produce(i);
                Thread.sleep(500); // Simulate production time
            }
            System.out.println("Producer finished producing.");
        } catch (InterruptedException e) {
            System.out.println("Producer interrupted: " + e.getMessage());
        }
    }
}

// Consumer thread
class Consumer extends Thread {
    private SharedBuffer buffer;
    private int itemsToConsume;
    
    public Consumer(SharedBuffer buffer, int itemsToConsume) {
        this.buffer = buffer;
        this.itemsToConsume = itemsToConsume;
    }
    
    @Override
    public void run() {
        try {
            for (int i = 0; i < itemsToConsume; i++) {
                buffer.consume();
                Thread.sleep(1000); // Simulate consumption time
            }
            System.out.println("Consumer finished consuming.");
        } catch (InterruptedException e) {
            System.out.println("Consumer interrupted: " + e.getMessage());
        }
    }
}

// Main class
public class ProducerConsumerDemo {
    public static void main(String[] args) {
        System.out.println("=== Producer-Consumer Problem ===\n");
        
        // Create shared buffer with capacity of 5
        SharedBuffer buffer = new SharedBuffer(5);
        
        // Create producer and consumer threads
        Producer producer = new Producer(buffer, 10);
        Consumer consumer = new Consumer(buffer, 10);
        
        // Start threads
        producer.start();
        consumer.start();
        
        try {
            // Wait for both threads to complete
            producer.join();
            consumer.join();
        } catch (InterruptedException e) {
            System.out.println("Main thread interrupted: " + e.getMessage());
        }
        
        System.out.println("\nAll operations completed successfully!");
    }
}