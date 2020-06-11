The Java programming language defines the following kinds of variables:<br>
#### Instance Variables (Non-Static Fields)
  >Technically speaking, objects store their individual states in "non-static fields", <br>
   that is, fields declared without the static keyword. <br>
  Non-static fields are also known as instance variables because their values are unique to each instance of a class (to each object, 
  in other words); 
  the currentSpeed of one bicycle is independent from the currentSpeed of another.<br>
#### Class Variables (Static Fields) 
  >A class variable is any field declared with the static modifier; this tells the compiler that there is exactly one copy of this variable <br>
  in existence, regardless of how many times the class has been instantiated. A field defining the number of gears for a particular 
  kind of bicycle could be marked as static since conceptually the same number of gears will apply to all instances. <br>
  The code static int numGears = 6; would create such a static field. Additionally, the keyword final could be added to indicate that 
  the number of gears will never change.<br>
#### Local Variables 
  >Similar to how an object stores its state in fields, a method will often store its temporary state in local variables. <br>
  The syntax for declaring a local variable is similar to declaring a field (for example, int count = 0;). <br>
  There is no special keyword designating a variable as local; that determination comes entirely from the location in which
  the variable is declared — which is between the opening and closing braces of a method. <br>
  As such, local variables are only visible to the methods in which they are declared; they are not accessible from the rest of 
  the class.<br>
#### Parameters 
  >You've already seen examples of parameters, both in the Bicycle class and in the main method of the "Hello World!" application. <br>
  Recall that the signature for the mainmethod is public static void main(String[] args). Here, the args variable is the parameter to 
  this method. The important thing to remember is that parameters are always classified as "variables" not "fields". <br>
  This applies to other parameter-accepting constructs as well (such as constructors and exception handlers) 
  that you'll learn about later in the tutorial.<br>
  <br><br>
  --------
Having said that, the remainder of this tutorial uses the following general guidelines when discussing fields and variables. <br>
If we are talking about "fields in general" (excluding local variables and parameters), we may simply say "fields". <br>
If the discussion applies to "all of the above", we may simply say "variables". <br>
If the context calls for a distinction, we will use specific terms (static field, local variables, etc.) as appropriate. <br>
You may also occasionally see the term "member" used as well. A type's fields, methods, and nested types are collectively called 
its members.<br>

https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html
