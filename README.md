# LING575-Homework2

This is an FST implementation for Homework 2, Questions 1 and 2.
To run, the configuration must pass in the parameter "-s FrameSimple"

**hw2_q4.py** is the entry point for the program.

Requirements: each response must include a keyword for the intent
- Pizza: "I want a vegan pizza"
- Topping: "I want a mushroom topping"
  -Note: only one topping is currently supported per pizza. 
  That is, only one topping pizzas are available to order.
- Size: "I want a small size"

Ordered items must be spelled the same as in the menu.

## Example dialog

##1. Specialty pizza

```markdown
Welcome to the pizza ordering system. How can we help you?
> I want a hawaiian pizza
To confirm, you want a hawaiian specialty pizza
> yes
Okay. Do you want a delivery or pick-up?
> pick-up
To confirm, you want a pick-up service
> yes
Okay. What is your phone number?
> 123-456-7891
To confirm, your phone number is 315-228-8286
> yes
Thank you, your order for a medium hawaiian with regular crust and pineapple topping pizza is on the way
```


##2. Reorder pizza
```markdown
> reorder
Please type in your phone number.
> 123-456-7891
Thank you, your order for a medium hawaiian with regular crust and pineapple topping pizza is on the way
```

##3. Check order
```markdown
> check order
Please type in your phone number.
> 123-456-7891
Great, thank you. I see there is an order for a medium hawaiian with regular crust and pineapple topping pizza currently on its way
```

##4. Revise order
```markdown
Welcome to the pizza ordering system. How can we help you?
> hawaiian pizza
To confirm, you want a hawaiian specialty pizza
> I want to revise pizza
Okay, what is your new pizza?
> vegan pizza
To confirm, you want a vegan specialty pizza
> yes
Okay. Do you want a delivery or pick-up?
> pick-up
To confirm, you want a pick-up service
> yes
Okay. What is your phone number?
> 123-456-7891
To confirm, your phone number is 123-456-7891
> yes
Thank you, your order for a large vegan with gluten-free crust and mushrooms topping pizza is on the way
```

##5. Reject previously provided information
```markdown
Welcome to the pizza ordering system. How can we help you?
> a hawaiian pizza
To confirm, you want a hawaiian specialty pizza
> no
What pizza would you like?
> 4 cheese pizza
To confirm, you want a 4 cheese pizza
> yes
Okay. What topping do you want to add to your pizza?
> swiss topping
To confirm, your topping for your pizza is swiss
> no
What topping do you want to add to your pizza?
> ham topping
To confirm, your topping for your pizza is ham
> yes
Okay. What crust for your pizza?
> thin crust
To confirm, your crust selection is thin crust
> yes
Okay. Which size do you want? We have small, medium and large.
> small size
To confirm, your pizza size is small size
> yes
Okay. Do you want a delivery or pick-up?
> delivery
To confirm, you want a delivery service
> yes
Okay. Can you give me an address for your delivery?
> 123 main st address
To confirm, your address is 123 main st 
> yes
Okay. What is your phone number?
> 123-456-7891
To confirm, your phone number is 123-456-7891
> no
What is your phone number?
> 123-456-7899
To confirm, your phone number is 123-456-7899
> yes
Thank you, your order for a small 4 cheese with thin crust and ham topping pizza is on the way
```

##6 Provide information out-of-turn or out-of-order

```markdown
Welcome to the pizza ordering system. How can we help you?
> I want a thin crust
To confirm, your crust selection is thin crust
> yes
Okay. What pizza would you like?
> I want a swiss topping
To confirm, your topping for your pizza is swiss
> yes
Okay. What pizza would you like?
> I want delivery service
To confirm, you want a delivery service
> yes
Okay. What pizza would you like?
> 13 main street address
To confirm, your address is 13 main street 
> yes
Okay. What pizza would you like?
> 123-456-7899
To confirm, your phone number is 123-456-7899
> yes
Okay. What pizza would you like?
> 4 cheese pizza
To confirm, you want a 4 cheese pizza
> yes
Okay. Which size do you want? We have small, medium and large.
> large size
To confirm, your pizza size is large size
> yes
Thank you, your order for a large 4 cheese with thin crust and swiss topping pizza is on the way
```