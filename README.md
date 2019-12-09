# Opening, reading, writing files and error handling

Topics covered:
- Open()
- Try and except
- With and finally
- Exceptions and error handling

    ``
    (...) All that can go wrong will go wrong (...) - Mr Murphy
    ``
## Error handling
- Means assuming things will break and handling your errors when they do
- Providing adequate feedback while failing with grace
- When you handle your errors your code can continue to run (which is a good thing)

## Definitions

### Try: / Except:
- These blocks of code are used un conjunction to error handling
````
    try:
        block of code
        block of code
    except <exception> as <place_holder>:
        block of code
        block of code
        print(place_holder)
````

### Exceptions
- These occur when an error occurs