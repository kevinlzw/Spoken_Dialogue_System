from DialogActTypes import DialogActTypes
import random

confirm_phrase = {
    'pizza': 'you want a {} pizza',
    'topping': 'your topping for your pizza is {}',
    'crust': 'your crust selection is {} crust',
    'size': 'your pizza size is {} size',
    'delivery_type': 'you want a {} service',
    'phone': 'your phone number is {}',
    'address': 'your address is {}',
    'ifcontinue': 'Do you want to continue the order?'
}

request_phrase = {
    'pizza': 'What pizza would you like?',
    'topping': 'What topping do you want to add to your pizza?',
    'crust': 'What crust for your pizza?',
    'size': 'Which size do you want? We have small, medium and large.',
    'delivery_type': 'Do you want a delivery or pick-up?',
    'phone': 'What is your phone number?',
    'address': 'Can you give me an address for your delivery?'
}

recommend_phrase = {
    'pizza': 'Our most popular specialty pizza would be the typical pepperoni. Of course, if you are vegetarian I '
             'would recommend veggie supreme and vegan. If you are cheese lover, go with 4 cheese. ',
    'topping': 'We have mozzarella, cheddar and swiss cheese. In terms of other toppings, we have provolone, '
               'pineapple, green peppers, red onions, mushrooms, black olives, pepperoni, ham, bacon and sausage. ',
    'crust': 'I would recommend regular crust since most customers take it. If you need gluten free we also have it. ',
    'size': 'Small is for 2-3 people, medium is for 4-5 people and large is party size mainly for more than 6 people.',
    'side': 'We have two sticks and two salads. I would recommend bread sticks and caesar salad. ',
    'drink': 'If you want soft drinks, we have cola, root beer, orange soda and lemon soda. We also have mineral '
             'water and ginger ale. '
}

confirm_phrase_pre = ['To confirm', 'Just want to be sure', 'Let me repeat you', 'Just to make sure I understand']

class NLGDefault:

    def __init__(self):
        self.Name = "NLGDefault"

    def generate(self, dialogAct):
        if dialogAct.DialogActType == DialogActTypes.CONFIRM:
            confirm_idx = random.randint(0, len(confirm_phrase_pre)-1)
            s = confirm_phrase_pre[confirm_idx]
            if isinstance(dialogAct.info, str):
                s = 'I am so sorry for what happened. {}'.format(confirm_phrase[dialogAct.info])
            else:
                for key in dialogAct.info:
                    if isinstance(dialogAct.info[key], list):
                        s += ', ' + confirm_phrase[key].format(','.join(dialogAct.info[key]))
                    else:
                        s += ', ' + confirm_phrase[key].format(dialogAct.info[key])
            return s
        if dialogAct.DialogActType == DialogActTypes.REQUEST:
            if dialogAct.info[1]:
                s = dialogAct.info[1] + request_phrase[dialogAct.info[0]]
                return s
            s = request_phrase[dialogAct.info[0]]
            return s
        elif dialogAct.DialogActType == DialogActTypes.REVISE:
            s = "Okay, what is your new {}?".format(dialogAct.info)
            return s
        elif dialogAct.DialogActType == DialogActTypes.UNDEFINED:
            s = "I don't understand, can you say it again?"
            return s
        elif dialogAct.DialogActType == DialogActTypes.GOODBYE:
            s = "Thank you, your order for a {} pizza is on the way".format(dialogAct.info)
            return s
        elif dialogAct.DialogActType == DialogActTypes.REORDER:
            s = "Please type in your phone number."
            return s
        elif dialogAct.DialogActType == DialogActTypes.RETURN_CHECK:
            s = "Great, thank you. I see there is an order for a {} pizza currently on its way".format(dialogAct.info)
            return s
        elif dialogAct.DialogActType == DialogActTypes.RECOMMEND:
            s = ''
            for item in dialogAct.info:
                s += recommend_phrase[item]
            return s
