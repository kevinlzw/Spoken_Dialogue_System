from Order import Order


class DialogFrameSimple:

    def __init__(self):
        self.FrameName = "DialogFrameSimple"
        self.customer_preferred_order = {}
        self.cur_order = Order()
        self.ongoing_order = {}

    def ifPhoneHasArchived(self):
        return self.cur_order.phone in self.customer_preferred_order

    def ifCurOrderStarted(self):
        return self.cur_order.ifOrderStarted()

    def curUnfilledItem(self):
        return self.cur_order.NotFilledAttribute()

    def ifCurOrderOnlyPhone(self):
        return self.cur_order.ifOnlyPhone()

    def addCurOrderToArchive(self):
        self.customer_preferred_order[self.cur_order.phone] = self.cur_order
        self.ongoing_order[self.cur_order.phone] = self.cur_order
        self.cur_order = Order()

    def resetCurOrder(self):
        self.cur_order = Order()