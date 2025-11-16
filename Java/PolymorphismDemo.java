
// Interface definition
interface Drawable {
    void draw();
    void erase();
}

// Abstract class demonstrating polymorphism
abstract class Shape implements Drawable {
    protected String color;
    
    public Shape(String color) {
        this.color = color;
    }
    
    public abstract double calculateArea();
    
    public void displayColor() {
        System.out.println("Color: " + color);
    }
}

// Circle class
class Circle extends Shape {
    private double radius;
    
    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " circle with radius " + radius);
    }
    
    @Override
    public void erase() {
        System.out.println("Erasing the circle");
    }
}

// Rectangle class
class Rectangle extends Shape {
    private double length;
    private double width;
    
    public Rectangle(String color, double length, double width) {
        super(color);
        this.length = length;
        this.width = width;
    }
    
    @Override
    public double calculateArea() {
        return length * width;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " rectangle with dimensions " + length + "x" + width);
    }
    
    @Override
    public void erase() {
        System.out.println("Erasing the rectangle");
    }
}

// Triangle class
class Triangle extends Shape {
    private double base;
    private double height;
    
    public Triangle(String color, double base, double height) {
        super(color);
        this.base = base;
        this.height = height;
    }
    
    @Override
    public double calculateArea() {
        return 0.5 * base * height;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing a " + color + " triangle with base " + base + " and height " + height);
    }
    
    @Override
    public void erase() {
        System.out.println("Erasing the triangle");
    }
}

// Main class demonstrating dynamic polymorphism
public class PolymorphismDemo {
    public static void main(String[] args) {
        // Array of Shape references - demonstrating polymorphism
        Shape[] shapes = new Shape[3];
        shapes[0] = new Circle("Red", 5.0);
        shapes[1] = new Rectangle("Blue", 4.0, 6.0);
        shapes[2] = new Triangle("Green", 3.0, 4.0);
        
        System.out.println("=== Demonstrating Dynamic Polymorphism ===\n");
        
        // Dynamic method dispatch
        for (Shape shape : shapes) {
            shape.draw();
            shape.displayColor();
            System.out.printf("Area: %.2f\n", shape.calculateArea());
            shape.erase();
            System.out.println();
        }
        
        // Interface reference demonstration
        System.out.println("=== Interface Reference ===\n");
        Drawable drawable = new Circle("Yellow", 3.0);
        drawable.draw();
        drawable.erase();
    }
}