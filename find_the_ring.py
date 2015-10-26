
from sys import exit
from random import randint
import subprocess as sp

backpack_contents = ['gun', 'knife', 'flashlight']


def print_backpack_contents():
    print "\n"
    print "You have the following items in your backpack:"
    print "\n"
    for i in range(0, len(backpack_contents)):
        print backpack_contents[i]
    print "\n"


class Scene(object):

   def enter(self):
      print "This scene is not yet configured. Subclass it and implement enter()" 
      exit(1)


class Engine(object):
   
   def __init__(self, scene_map):
      self.scene_map = scene_map

   def play(self):
      current_scene = self.scene_map.opening_scene()

      while True:
         print "\n-----------"
         next_scene_name = current_scene.enter()
         current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
      quips = [
         "Game over. Try again",
         "You lost Try again.",
      ]

      def enter(self):
         #sp.call('clear', shell=True)
         print Death.quips[randint(0, len(self.quips) -1)]
         exit(1)


class UndergroundLake(Scene):

   def enter(self):
   
      sp.call('clear', shell=True)
      print "Your mission is to go in the Cave of Mystery, find the Golder Ring "
      print "and exit the cave." 
      print "\n"
      print "You can only carry 3 items at a time"
      print "You start with a gun, flashlight and a knife"
      print "\n"
      print "You enter the Cave of Mystery and see a huge underground lake and you"
      print "are near a boat."
      print "\n"
      print_backpack_contents()
      print "Your choices are:"
      print "1. Take the boat across the lake."
      print "2. Walk along the shore of the lake to the other side."
      print "\n"

      action = raw_input(">")

      if action == "1":
         print "Halfway across the lake, the boat starts to sink. You decide"
         print "to throw the gun overboard. You proceed to next corridor" 
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'volcano'

      elif action == "2":
         print "You walk along the shore of the lake and proceed to the next corridor"
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'volcano'

      else:
         print "DOES NOT COMPUTE!"
         return 'underground_lake'


class Volcano(Scene):

   def enter(self):
      sp.call('clear', shell=True)
      print "You enter an area with a large volcano.  It is erupting occassionally spewing "
      print "out lava that will kill you."
      print "\n"
      print_backpack_contents()
      
      print "Your choices are:"
      print "1. Walk on the west side around the volcano"
      print "2. Walk on the east side around the volcano."
      print "\n"

      action = raw_input("> ")   

      if action == "1":
         print "As you walk along the west side, the volcano erupts sending a river " 
         print "of lava at you covering you and killing you instantly." 
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'death'

      elif action == "2":
         print "As you walk along the east side, you feel the heat from the nearby "
         print "lava.  The heat is intense and threatens to overwhelm you but you push "
         print "on. You proceed to the next corridor but you realize that your knife has"
         print "melted.  You no longer have a knife."
         backpack_contents.remove('knife')
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'dark_cave'

      else:
         print "DOES NOT COMPUTE!"
         return "volcano"


class DarkCave(Scene):

   def enter(self):
      sp.call('clear', shell=True)
      print "You enter an area that is completely dark.  You turn on your flashlight. "
      print "You see 2 paths.  One goes uphill and west.  The other is flat and goes east."
      print "\n"
      print_backpack_contents()
      print "Your choices are:"
      print "1. Walk on the west side up the hill"
      print "2. Walk on the east side"


      action = raw_input("> ")   

      if action == "1":
         print "As you walk up the hill, you find a glowing sword. You pick it up and proceed" 
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'statue'

      elif action == "2":
         print "As you walk along the east side, you hear noises from further up the "
         print "path. It could be orcs. You need to turn off your flashlight and hide in  "
         print "the bushes. The sounds fade away and you proceed cautiously."
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'river'

      else:
         print "DOES NOT COMPUTE!"
         return "dark_cave"


class Statue(Scene):

   def enter(self):
      #sp.call('clear', shell=True)
      print "You enter a wide open area with a huge statue of a golden monkey. "
      print "At the feet of the golden monkey are many beautiful gems and jewels"
      print "but they are guarded by poisonous snakes whose venom will kill you in a minute."
      print "\n"
      print_backpack_contents() 
      print "Your choices are:"
      print "1. Walk on the right side of the monkey statue staying far away from the snakes"
      print "2. Walk on the left side of the monkey statue staying faw away from the snakes"
      print "\n"

      action = raw_input("> ")   

      if action == "1":
         print "As you walk on the right side of the huge statue you find a small bag " 
         print "with 10 gold coins in it.  You pick it up and proceed."
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return "bird_room"

      elif action == "2":
         print "As you walk on the left side, you find a small bottle with blue potion "
         print "You pick it up and proceed. Suddenly a giant net is dropped on you, wraps "
         print "you up and lifts you in the air.  You are suspended in the air unable to  "
         print "break free from the net. You reach for the blue potion and drink it all. " 
         print "The potion kills you instantly."
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'death'

      else:
         print "DOES NOT COMPUTE!"
         return "statue"


class River(Scene):

   def enter(self):
      #sp.call('clear', shell=True)
      print "You find yourself on a tall cliff overlooking a rapidly flowing river. "
      print "In the distance you see a gold bridge over the river to the east and a "   
      print "silver bridge over the river to the west. Both bridges are about a mile away."
      print "\n"
      print_backpack_contents()
      print "Your choices are:"
      print "1. Walk to the gold bridge"
      print "2. Walk to the silver bridge"
      print "\n"

      action = raw_input("> ")   

      if action == "1":
         print "As you walk over the gold bridge, you see what appears to be a dead body " 
         print "at the end of the bridge. You proceed slowly and see that it is a dead orc." 
         print "You proceed to take the dead orc's sword and notice something glowing in "
         print "its clenched right hand.  You open its hand and find a golden ring!"
         print "You pick up the golden ring and proceed to a cave entrance"
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return "the_end"

      elif action == "2":
         print "As you walk over the silver bridge, you suddenly see 10 orcs at "
         print "the end of the bridge waiting for you with their swords drawn."
         print "You turn around to get off the bridge and see 20 orcs behind you."
         print "You are trapped!  The orcs on both sides start running toward you."
         print "The only choice you see is to jump off the bridge.  You jump off into"
         print "the rapidly flowing river.  The orcs shoot arrows at you but they all"
         print "miss.  The river carries you along and the current is too strong to swim to"
         print "one side or the other. Then you realize the river is leading to a huge " 
         print "waterfall.  You try to get out of the river before it carries you over"
         print "the side but it is too late.  You go over the edge and are crushed on"
         print "rocks below dying instantly" 
         print "\n"
         print "Enter any key to continue"
         action = raw_input(">")
         return 'death'

      else:
         print "DOES NOT COMPUTE!"
         return "statue"



class Map(object):

   scenes = {
      'underground_lake': UndergroundLake(),
      'volcano': Volcano(),
      # 'ice_cave':  IceCave(),
      'dark_cave': DarkCave(),
      'statue_cave' : Statue(),
      # 'bird_cave' : BirdCave(),
      #'bottomless_hole' : BottomlessHole(),
      'river' : River(),
      #'waterfall' : Waterfall(),
      'death': Death()
   } 

   def __init__(self, start_scene):
      self.start_scene = start_scene

   def next_scene(self, scene_name):
      return Map.scenes.get(scene_name)

   def opening_scene(self):
      return self.next_scene(self.start_scene)


a_map = Map('underground_lake')
a_game = Engine(a_map)
a_game.play()



