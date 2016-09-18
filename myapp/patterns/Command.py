from django.utils import timezone

#from myapp.records import BidRecord, ProductRecord, PartnerRecord

class BidDomain(object):
    def turn_on(self):
        print 'Включить свет'

    def turn_off(self):
        print 'Выключить свет'


class CommandBase(object):
    def execute(self):
        raise NotImplementedError()


class LightCommandBase(CommandBase):
    def __init__(self, light):
        self.light = light


class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Action(object):
    def __init__(self, create_cmd, edit_cmd, read_cmd, delete_cmd, all_cmd):
        self.create_cmd = create_cmd
        self.edit_cmd = edit_cmd
        self.read_cmd= read_cmd
        self.delete_cmd = delete_cmd
        self.all_cmd = all_cmd

    def create(self):
        self.create_cmd.execute()

    def edit(self):
        self.edit_cmd.execute()

    def read(self):
        self.read_cmd.execute()

    def delete(self):
        self.delete_cmd.execute()

    def all(self):
        self.all_cmd.execute()


light = Light()
switch = Switch(on_cmd=TurnOnLightCommand(light),
                off_cmd=TurnOffLightCommand(light))
switch.on()  # Включить свет
switch.off() # Выключить свет
