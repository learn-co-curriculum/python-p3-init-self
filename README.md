# Object Initialization

## Learning Goals

- Learn about the `__init__` method.
- Learn about the `self` keyword.
- Initialize unique objects from the same class.

***

## Key Vocab

- **Class**: a bundle of data and functionality. Can be copied and modified to
accomplish a wide variety of programming tasks.
- **Initialize**: create a working copy of a class using its `__init__()`
method.
- **Instance**: one specific working copy of a class. It is created when a
class's `__init__()` method is called.
- **Object**: the more common name for an instance. The two can usually be used
interchangeably.
- **Function**: a series of steps that create, transform, and move data.
- **Method**: a function that is defined inside of a class.
- **Attribute**: variables that belong to an object.

***

## Introduction

We've already seen many new instances of different classes being created:

```py
class Dog:
    pass

fido = Dog()
# <__main__.Dog object at 0x104fc0550>

snoopy = Dog()
# <__main__.Dog object at 0x104fc0562>
```

We know from their IDs that `fido` and `snoopy` live in different locations
in memory, but their _behavior_ is identical. We don't provide them any unique
methods or attributes in the code above.

***

## `__init__`

Every time we initialize a new object, the Python interpreter calls a **magic
method** called `__init__`. **Magic methods** (also called **dunder methods**
due to their **d**ouble **under**scores) are special methods that are not meant
to be called by developers but are invoked by different cues and operators that
act on their objects.

The `__init__` method belongs to every class and is invoked when you
initialize a class. Though you cannot see it in our `Dog` class above, there
is code that is executed behind the scenes.

Though it always executes when we initialize an object, it does not do anything
by default. Instead, we overwrite `__init__` in most classes to change an
object's behavior:

```py
class Dog:
    # Remember that all methods use "self." We'll elaborate on this in a moment.
    def __init__(self):
        print("A dog is born!")

    def bark(self):
        print("Woof!")
    
fido = Dog()
# A dog is born!
```

`__init__` can also be modified to take more arguments. This allows us to
customize the behavior of unique objects:

```py
class Dog:
    def __init__(self, name):
        print(f"{name} is born!")

    def bark(self):
        print("Woof!")

fido = Dog("Fido")
# Fido is born!
fido.bark()
# Woof!

snoopy = Dog("Snoopy")
# Snoopy is born!
snoopy.bark()
# Woof!
```

***

## `self`

Modifying `__init__` has allowed us to provide `fido` and `snoopy` with
different behaviors, but now that they've both been initialized, they're more
or less the same dog. In order to make lasting changes to an object, we need
to modify `self`. Before we do, open up the Python shell and let's take a look
at `self`:

```py
class Dog:
    def __init__(self, name):
        print(f"{name} is born!")

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

fido = Dog("Fido")
# Fido is born!
fido.showing_self()
# <__main__.Dog object at 0x104f8bfa0>
```

You might recognize this output from earlier- `self` is the same type of object
as `fido`! As a matter of fact, it _is_ `fido`!

```py
fido is fido.showing_self()
# <__main__.Dog object at 0x104f8bfa0>
# True
```

How does this work? Inside the `showing_self()` method, we use the `self`
keyword.

The `self` keyword **refers to the instance**, or object, that the
`showing_self()` **method is being called on**.

So, when we call `showing_self()` on `fido`, the method will return the `Dog`
instance that is `fido`.

If you’re familiar with Object Oriented JavaScript from previous experience, the
closest equivalent to `self` in Python is `this` in JavaScript. Again, no
worries if you haven't seen OOJS before. The `this` keyword behaves similarly,
where `this` refers to **the object to the left of the dot** when a method is
called on an object:

```js
class Dog {
  showingThis() {
    return this;
  }
}

const fido = new Dog();
fido.showingThis();
// => Dog {}
```

***

## Operating on `self` in an Instance Method

Let's say that Fido here is getting adopted. Fido's new owner is Sophie. Let's
write an `attr_accessor` on our `Dog` for the owner attribute.

```rb
class Dog
  attr_accessor :name, :owner

  def initialize(name)
    @name = name
  end

end
```

Now we can set Fido's `owner` attribute equal to the string of `"Sophie"`. The
name of his new owner:

```rb
fido.owner = "Sophie"

fido.owner
# => "Sophie"
```

Great, Fido now knows the name of his owner. Let's think about the situation in
which `fido` gets a new owner. This would occur at the moment in which `fido` is
adopted.

To represent this with code, we could write an `#adopted` method like this:

```rb
def adopted(dog, owner_name)
  dog.owner = owner_name
end
```

Here we have a method that takes in two arguments, an instance of the `Dog`
class and an owner's name. We could call our method like this:

```rb
adopted(fido, "Sophie")

# now we can ask Fido who his owner is:

fido.owner
# => "Sophie"
```

However, the beauty of object-oriented programming is that we can encapsulate,
or wrap up, attributes and behaviors into one object. Instead of writing a
method that is not associated to any particular object and that takes in certain
objects as arguments, we can simply teach our `Dog` instances how to get
adopted.

Let's refactor our code above into an instance method on the `Dog` class.

```rb
class Dog
  attr_accessor :name, :owner

  def initialize(name)
    @name = name
  end

  def bark
    "Woof!"
  end

  def get_adopted(owner_name)
    self.owner = owner_name
  end

end
```

Here, we use the `self` keyword inside of the `#get_adopted` instance method to
refer to whichever dog this method is being called on. We set that dog's `owner`
property equal to the new owner's name by calling the `#owner=` method on `self`
inside the method body.

Think about it: if `self` **refers to the object on which the method is being
called**, and if that object is an instance of the `Dog` class, then we can call
any of our other instance methods on `self`.

Here's how we'd use the `#get_adopted` method:

```rb
fido = Dog.new("Fido")
fido.get_adopted("Sophie")
fido.owner
# => "Sophie"
```

## Instructions

Complete the following tasks to get the rest of the tests passing:

1. Add an instance method `sit()` to your `Dog` class that will print "The dog
is sitting."
2. Define a `Person` class in `lib/person.py`
3. Add an instance method `talk()` to your Person class that will print "Hello World!"
4. Add an instance method `walk()` to your Person class that will print "The
person is walking."

## Conclusion

With all tests passing, you have successfully written multiple instance methods
and _two_ different classes!

The ability to define methods and behaviors in our classes for our instances
makes Python classes behave not just as factories, capable of instantiating new
individual instances, but also as a blueprint, defining what those instances
can do.

***

## Resources

- [Python documentation][python docs]
- [Instance method in Python](https://www.geeksforgeeks.org/instance-method-in-python/)
- [Method Objects](https://docs.python.org/3/tutorial/classes.html#method-objects)

[python docs]: https://docs.python.org/3/
