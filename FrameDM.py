from DialogFrameSimple import DialogFrameSimple
from DialogAct import DialogAct
from DialogActTypes import DialogActTypes



class FrameDMSimple:

    def __init__(self, NLU, NLG):
        self.NLU = NLU
        self.NLG = NLG
        # define frame below, for example:
        self.DialogFrame = DialogFrameSimple()
        self.status = None
        self.info = None
        self.confirm_saved_info = None
        self.NLG_output = None

    def execute(self, inputStr):
        # apply the NLU component
        currentSemanticFrame, compound_score = self.NLU.parse(inputStr)

        # update the dialog frame with the new information
        self.trackState(currentSemanticFrame, compound_score)

        # and decide what to do next
        newDialogAct = self.selectDialogAct()

        # then generate some meaningful response
        response = self.NLG.generate(newDialogAct)
        return response

    def trackState(self, newSemanticFrame, sentiment_score):
        # update self.DialogFrame based on the contents of newSemanticFrame
        if self.status == 'GIVE_RECOMMEND':
            if sentiment_score > 0.3:
                self.NLG_output = 'I am glad you found it useful! '
            elif sentiment_score < 0.3:
                self.NLG_output = 'I am sorry my recommendation did not help. '
        if newSemanticFrame.Intent == 'reorder_favorite':
            self.status = 'REQUEST_phone_reorder'
            self.info = None
            self.confirm_saved_info = None
        elif newSemanticFrame.Intent == 'order_pizza':
            self.status = 'CONFIRM'
            self.confirm_saved_info = newSemanticFrame.Slots
        elif newSemanticFrame.Intent == 'provide_contact_information':
            if self.status == 'REQUEST_phone_reorder':
                if newSemanticFrame.Slots['phone'] in self.DialogFrame.customer_preferred_order:
                    preferred_order = self.DialogFrame.customer_preferred_order[newSemanticFrame.Slots['phone']]
                    self.DialogFrame.cur_order = preferred_order
                    self.status = 'NEXT_THING_TO_ASK'
                else:
                    self.status = 'NEXT_THING_TO_ASK'
                    self.info = 'no_reorder'
                    self.confirm_saved_info = None
            elif self.status == 'REQUEST_phone_check':
                if newSemanticFrame.Slots['phone'] in self.DialogFrame.ongoing_order:
                    check_order = self.DialogFrame.ongoing_order[newSemanticFrame.Slots['phone']]
                    self.status = 'RETURN_check'
                    self.info = check_order
                else:
                    self.status = 'NEXT_THING_TO_ASK'
                    self.info = 'no_check'
                    self.confirm_saved_info = None
            elif not self.DialogFrame.cur_order.phone:
                self.status = 'CONFIRM'
                self.info = 'phone'
                self.confirm_saved_info = newSemanticFrame.Slots
        elif newSemanticFrame.Intent == 'inform_delivery':
            self.status = 'CONFIRM'
            self.info = 'delivery_type'
            self.confirm_saved_info = newSemanticFrame.Slots
        elif newSemanticFrame.Intent == 'query_pizza_status':
            self.status = 'REQUEST_phone_check'
            self.info = None
        elif newSemanticFrame.Intent == 'change_order':
            self.status = 'REVISE'
            self.info = newSemanticFrame.Slots
        elif newSemanticFrame.Intent == 'confirm_previous':
            if newSemanticFrame.Slots['confirm'] == 'yes' and self.confirm_saved_info != 'ifcontinue':
                try:
                    self.DialogFrame.cur_order.fillAttribute(self.confirm_saved_info)
                except:
                    pass
            elif newSemanticFrame.Slots['confirm'] == 'no' and self.confirm_saved_info == 'ifcontinue':
                raise InterruptedError('Your order is canceled.')
            self.status = 'NEXT_THING_TO_ASK'
            self.info = 'ok'
            self.confirm_saved_info = None
        elif newSemanticFrame.Intent == 'ask_for_recommend':
            self.status = 'GIVE_RECOMMEND'
            self.info = []
            if not newSemanticFrame.Slots['recommend']:
                self.info.append('pizza')
            else:
                self.info.extend(newSemanticFrame.Slots['recommend'])
        else:
            self.status = 'NEXT_THING_TO_ASK'
            if sentiment_score >= 0.1:
                self.info = 'compliment'
                self.confirm_saved_info = None
            elif -0.1 >= sentiment_score > 0.5:
                self.info = 'apology'
                self.confirm_saved_info = None
            elif sentiment_score <= -0.5:
                self.status = 'CONFIRM'
                self.info = 'ifcontinue'
                self.confirm_saved_info = 'ifcontinue'
            else:
                self.info = 'confused'
                self.confirm_saved_info = None


    def selectDialogAct(self):
        # decide on what dialog act to execute
        dialogAct = DialogAct()
        if self.status == 'CONFIRM':
            dialogAct.DialogActType = DialogActTypes.CONFIRM
            dialogAct.info = self.confirm_saved_info
        elif self.status == 'NEXT_THING_TO_ASK':
            next_unfilled_item = self.DialogFrame.curUnfilledItem()
            if not next_unfilled_item:
                dialogAct.DialogActType = DialogActTypes.GOODBYE
                dialogAct.info = str(self.DialogFrame.cur_order)
                self.DialogFrame.addCurOrderToArchive()
            else:
                dialogAct.DialogActType = DialogActTypes.REQUEST
                if self.info == 'ok':
                    dialogAct.info = (next_unfilled_item, 'Okay. ')
                    self.info = None
                elif self.info == 'confused':
                    dialogAct.info = (next_unfilled_item, 'I am confused. ')
                    self.info = None
                elif self.info == 'compliment':
                    dialogAct.info = (next_unfilled_item, 'Good for you! ')
                    self.info = None
                elif self.info == 'apology':
                    dialogAct.info = (next_unfilled_item, 'I am so sorry for what have happened. ')
                    self.info = None
                elif self.info == 'no_reorder':
                    dialogAct.info = (next_unfilled_item, 'You have no preferred order. ')
                    self.info = None
                elif self.info == 'no_check':
                    dialogAct.info = (next_unfilled_item, 'You have no ongoing order. ')
                    self.info = None
                else:
                    dialogAct.info = (next_unfilled_item, None)
        elif self.status == 'REVISE':
            dialogAct.DialogActType = DialogActTypes.REVISE
            dialogAct.info = self.info
        elif self.status == 'REQUEST_phone_reorder' or self.status == 'REQUEST_phone_check':
            dialogAct.DialogActType = DialogActTypes.REORDER
        elif self.status == 'RETURN_check':
            dialogAct.DialogActType = DialogActTypes.RETURN_CHECK
            dialogAct.info = self.info
        elif self.status == 'GIVE_RECOMMEND':
            dialogAct.DialogActType = DialogActTypes.RECOMMEND
            dialogAct.info = self.info
        if self.NLG_output:
            dialogAct.general_info = self.NLG_output
            self.NLG_output = None
        return dialogAct
