# items()

```python
car = {"name" : "BMW", "price" : "7000"} 
car.items() 
dict_items([('name', 'BMW'), ('price', '7000')]) 
```

```python
car = {"name" : "BMW", "price" : "7000"} 
for key, val in car.items():
    print("key : {} value : {}".format(key,val)) 

# key : name value : BMW 
# key : price value : 7000 
```

