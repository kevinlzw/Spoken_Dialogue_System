from SemanticFrame import SemanticFrame
from PizzaMenu import *
import re
import os
import pickle
from SentimentAnalyzer import SentimentAnalyzer


change = ["change my order", 'switch']
reorder = ["reorder", "recent", "another order", "my previous", "preferred", "favorite", "my usual"]
delivery = ["take out", "pick up", "pick-up", "takeout", " delivery", "take-out", "pickup"]
confirm = ['sure', 'yes', 'no', 'yeah', 'right', 'nope', 'exactly', 'yep', 'why not']
recommend = ['pizza', 'topping', 'size', 'crust', 'side', 'drink']

class NLUDefault:
    def __init__(self):
        self.sz = SentimentAnalyzer()
        with open(os.path.join(os.getcwd(), 'vectorizer.pk'), 'rb') as fin:
            self.vectorizer = pickle.load(fin)
        with open(os.path.join(os.getcwd(), 'question_detection.sav'), 'rb') as file:
            self.model = pickle.load(file)


    def parse(self, input_str):
        sf = SemanticFrame()
        input_str = input_str.lower()
        sf.Intent = 'user_statement'

        for pizza in PizzaMenu.specialty:
            if pizza.lower() in input_str:
                sf.Slots['pizza'] = pizza
                sf.Intent = "order_pizza"

        for topping in PizzaMenu.Toppings:
            if topping.lower() in input_str:
                if 'topping' not in sf.Slots:
                    sf.Slots['topping'] = []
                sf.Slots['topping'].append(topping)
                sf.Intent = "order_pizza"

        for size in PizzaMenu.sizes:
            if size.lower() in input_str:
                sf.Slots['size'] = size
                sf.Intent = "order_pizza"

        for crust in PizzaMenu.crusts:
            if crust.lower() in input_str:
                sf.Slots['crust'] = crust
                sf.Intent = "order_pizza"

        for side in PizzaMenu.sides:
            if side.lower() in input_str:
                sf.Slots['side'] = side
                sf.Intent = "order_extras"

        for drink in PizzaMenu.drinks:
            if drink.lower() in input_str:
                sf.Slots['drink'] = drink
                sf.Intent = "order_extras"

        phone = re.findall(r"([\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4})", input_str, re.IGNORECASE)
        if phone:
            for num in phone:
                sf.Slots['phone'] = num
                sf.Intent = "provide_contact_information"

        other_contact = re.findall(r"(?:this is|it's) ([\S]+)", input_str, re.IGNORECASE)
        if other_contact:
            for contact in other_contact:
                sf.Slots['contact'] = contact
                sf.Intent = "provide_contact_information"

        for ele in delivery:
            if ele in input_str:
                if ele == ' delivery' or ele == 'delivery':
                    ele = 'delivery'
                else:
                    ele = 'pick-up'
                sf.Slots['delivery_type'] = ele
                sf.Intent = "inform_delivery"

        for ele in change:
            if ele in input_str:
                sf.Intent = "change_order"

        for ele in reorder:
            if ele in input_str:
                sf.Intent = "reorder_favorite"

        ifquestion = self.model.predict(self.vectorizer.transform([input_str]))[0]
        if ifquestion == 'whQuestion' or ifquestion == 'ynQuestion':
            if 'recommend' in input_str:
                sf.Intent = 'ask_for_recommend'
                sf.Slots['recommend'] = []
                for item in recommend:
                    if item in input_str:
                        sf.Slots['recommend'].append(item)
            elif 'order' in input_str:
                sf.Intent = "query_pizza_status"

        for ele in confirm:
            if ele in input_str:
                if ele == 'yes' or ele == 'yeah' or ele == 'right' or ele == 'sure' or ele == 'exactly' or ele == 'yep' or ele == 'why not':
                    sf.Slots['confirm'] = 'yes'
                else:
                    sf.Slots['confirm'] = 'no'
                sf.Intent = "confirm_previous"
        return sf, self.sz.compound_sentiment_score(input_str)
