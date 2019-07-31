from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

#room description 01
room_01 = Room(title="room_01",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_02 = Room(title="room_02",
              description="This grassy patch seems to dense to walk across, you must find a new route")
room_03 = Room(title="room_03",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_04 = Room(title="room_04",
              description="This pebble walkway might lead to somewhere that has treasure")
room_05 = Room(title="room_05",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_06 = Room(title="room_06",
              description="This pebble walkway might lead to somewhere that has treasure")
room_07 = Room(title="room_07",
              description="This pebble walkway might lead to somewhere that has treasure")
room_08 = Room(title="room_08",
              description="This pebble walkway might lead to somewhere that has treasure")
room_09 = Room(title="room_09",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_10 = Room(title="room_10",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind") 
#room description 02
room_11 = Room(title="room_11",
              description="This pebble walkway might lead to somewhere that has treasure")
room_12 = Room(title="room_12",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_13 = Room(title="room_13",
              description="This pebble walkway might lead to somewhere that has treasure")
room_14 = Room(title="room_14",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_15 = Room(title="room_15",
              description="lThis pebble walkway might lead to somewhere that has treasure")                
room_16 = Room(title="room_16",
              description="This stump seems to tall and large to move past, you must find a new route")
room_17 = Room(title="room_17",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_18 = Room(title="room_18",
              description="This pebble walkway might lead to somewhere that has treasure")
room_19 = Room(title="room_19",
              description="This pebble walkway might lead to somewhere that has treasure")
room_20 = Room(title="room_20",
              description="This pebble walkway might lead to somewhere that has treasure")
#room description 03
room_21 = Room(title="room_21",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_22 = Room(title="room_22",
              description="This pebble walkway might lead to somewhere that has treasure")
room_23 = Room(title="room_23",
              description="This giant rock seems to wide to walk across, you must find a new route")
room_24 = Room(title="room_24",
              description="This pebble walkway might lead to somewhere that has treasure")
room_25 = Room(title="room_25",
              description="This pebble walkway might lead to somewhere that has treasure")                
room_26 = Room(title="room_26",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_27 = Room(title="room_27",
              description="This pebble walkway might lead to somewhere that has treasure")
room_28 = Room(title="room_28",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_29 = Room(title="room_29",
              description="This stump seems to tall and large to move past, you must find a new route")
room_30 = Room(title="room_20",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")            
#room description 04
room_31 = Room(title="room_31",
              description="This pebble walkway might lead to somewhere that has treasure")
room_32 = Room(title="room_32",
              description="This fernace is still hot, there might be food somewhere around here")
room_33 = Room(title="room_33",
              description="This grassy patch seems to dense to walk across, you must find a new route")
room_34 = Room(title="room_34",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_35 = Room(title="room_35",
              description="This pebble walkway might lead to somewhere that has treasure")
room_36 = Room(title="room_36",
              description="This pebble walkway might lead to somewhere that has treasure")
room_37 = Room(title="room_37",
              description="This giant rock seems to wide to walk across, you must find a new route")
room_38 = Room(title="room_38",
              description="This pebble walkway might lead to somewhere that has treasure")
room_39 = Room(title="room_39",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_40 = Room(title="room_40",
              description="This pebble walkway might lead to somewhere that has treasure")
#room description 05
room_41 = Room(title="room_41",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_42 = Room(title="room_42",
              description="This pebble walkway might lead to somewhere that has treasure")
room_43 = Room(title="room_43",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_44 = Room(title="room_44",
              description="This pebble walkway might lead to somewhere that has treasure")
room_45 = Room(title="room_45",
              description="This pebble walkway might lead to somewhere that has treasure")                
room_46 = Room(title="room_46",
              description="Looking around, the house looks like someone used to live hear. They might have left valuables behind")
room_47 = Room(title="room_47",
              description="This pebble walkway might lead to somewhere that has treasure")
room_48 = Room(title="room_48",
              description="This pebble walkway might lead to somewhere that has treasure")
room_49 = Room(title="room_49",
              description="This fernace is still hot, there might be food somewhere around here")
room_50 = Room(title="room_50",
              description="This grassy patch seems to dense to walk across, you must find a new route")                                                         
#--------------------------------------------------------------------------------------------------------

room_01.save()
room_02.save()
room_03.save()
room_04.save()
room_05.save()
room_06.save()
room_07.save()
room_08.save()
room_09.save()
room_10.save()

room_11.save()
room_12.save()
room_13.save()
room_14.save()
room_15.save()
room_16.save()
room_17.save()
room_18.save()
room_19.save()
room_20.save()

room_21.save()
room_22.save()
room_23.save()
room_24.save()
room_25.save()
room_26.save()
room_27.save()
room_28.save()
room_29.save()
room_30.save()

room_31.save()
room_32.save()
room_33.save()
room_34.save()
room_35.save()
room_36.save()
room_37.save()
room_38.save()
room_39.save()
room_40.save()

room_41.save()
room_42.save()
room_43.save()
room_44.save()
room_45.save()
room_46.save()
room_47.save()
room_48.save()
room_49.save()
room_50.save()

# Row 01 
room_01.connectRooms(room_11,'s')
room_11.connectRooms(room_01,'n')

room_11.connectRooms(room_21,'s')
room_21.connectRooms(room_11,'n')

room_21.connectRooms(room_31,'s')
room_31.connectRooms(room_21,'n')

room_31.connectRooms(room_41,'s')
room_41.connectRooms(room_31,'n')

# Row 02

room_12.connectRooms(room_22,'s')
room_22.connectRooms(room_12,'n')

room_22.connectRooms(room_32,'s')
room_32.connectRooms(room_22,'n')

room_32.connectRooms(room_42,'s')
room_42.connectRooms(room_32,'n')

# Row 03 
room_03.connectRooms(room_13,'s')
room_13.connectRooms(room_03,'n')

# Row 04 
room_04.connectRooms(room_14,'s')
room_14.connectRooms(room_04,'n')

room_14.connectRooms(room_24,'s')
room_24.connectRooms(room_14,'n')

room_24.connectRooms(room_34,'s')
room_34.connectRooms(room_24,'n')

room_34.connectRooms(room_44,'s')
room_44.connectRooms(room_34,'n')

# Row 05 
room_05.connectRooms(room_15,'s')
room_15.connectRooms(room_05,'n')

room_15.connectRooms(room_25,'s')
room_25.connectRooms(room_15,'n')

room_25.connectRooms(room_35,'s')
room_35.connectRooms(room_25,'n')

# Row 06 
room_26.connectRooms(room_36,'s')
room_36.connectRooms(room_26,'n')

# Row 07 
room_07.connectRooms(room_17,'s')
room_17.connectRooms(room_07,'n')

room_17.connectRooms(room_27,'s')
room_27.connectRooms(room_17,'n')

# Row 08
room_08.connectRooms(room_18,'s')
room_18.connectRooms(room_08,'n')

room_18.connectRooms(room_28,'s')
room_28.connectRooms(room_18,'n')

room_28.connectRooms(room_38,'s')
room_38.connectRooms(room_28,'n')

room_38.connectRooms(room_48,'s')
room_48.connectRooms(room_38,'n')

# Row 09
room_09.connectRooms(room_19,'s')
room_19.connectRooms(room_09,'n')

room_39.connectRooms(room_49,'s')
room_49.connectRooms(room_39,'n')

# Row 10
room_10.connectRooms(room_20,'s')
room_20.connectRooms(room_10,'n')

room_20.connectRooms(room_30,'s')
room_30.connectRooms(room_20,'n')

room_30.connectRooms(room_40,'s')
room_40.connectRooms(room_30,'n')

# 0-10 e-w connections

room_03.connectRooms(room_04,'e')
room_04.connectRooms(room_03,'w')

room_04.connectRooms(room_05,'e')
room_05.connectRooms(room_04,'w')

room_05.connectRooms(room_06,'e')
room_06.connectRooms(room_05,'w')

room_06.connectRooms(room_07,'e')
room_07.connectRooms(room_06,'w')

room_08.connectRooms(room_09,'e')
room_09.connectRooms(room_08,'w')

room_09.connectRooms(room_10,'e')
room_10.connectRooms(room_09,'w')

# 10-20 e-w connections

room_11.connectRooms(room_12,'e')
room_12.connectRooms(room_11,'w')

room_12.connectRooms(room_13,'e')
room_13.connectRooms(room_12,'w')

room_13.connectRooms(room_14,'e')
room_14.connectRooms(room_13,'w')

room_14.connectRooms(room_15,'e')
room_15.connectRooms(room_14,'w')


room_18.connectRooms(room_19,'e')
room_19.connectRooms(room_18,'w')

room_19.connectRooms(room_20,'e')
room_20.connectRooms(room_19,'w')

# 20-30 e-w connections

room_21.connectRooms(room_22,'e')
room_22.connectRooms(room_21,'w')

room_24.connectRooms(room_25,'e')
room_25.connectRooms(room_24,'w')

room_25.connectRooms(room_26,'e')
room_26.connectRooms(room_25,'w')

room_26.connectRooms(room_27,'e')
room_27.connectRooms(room_26,'w')

room_27.connectRooms(room_28,'e')
room_28.connectRooms(room_27,'w')


# 30-40 e-w connections

room_31.connectRooms(room_32,'e')
room_32.connectRooms(room_31,'w')

room_34.connectRooms(room_35,'e')
room_35.connectRooms(room_34,'w')

room_35.connectRooms(room_36,'e')
room_36.connectRooms(room_35,'w')

room_38.connectRooms(room_39,'e')
room_39.connectRooms(room_38,'w')

room_39.connectRooms(room_40,'e')
room_40.connectRooms(room_39,'w')

# 40-50 e-w connections

room_41.connectRooms(room_42,'e')
room_42.connectRooms(room_41,'w')

room_42.connectRooms(room_43,'e')
room_43.connectRooms(room_42,'w')

room_43.connectRooms(room_44,'e')
room_44.connectRooms(room_43,'w')

room_44.connectRooms(room_45,'e')
room_45.connectRooms(room_44,'w')

room_45.connectRooms(room_46,'e')
room_46.connectRooms(room_45,'w')

room_46.connectRooms(room_47,'e')
room_47.connectRooms(room_46,'w')

room_47.connectRooms(room_48,'e')
room_48.connectRooms(room_47,'w')

room_48.connectRooms(room_49,'e')
room_49.connectRooms(room_48,'w')



players=Player.objects.all()
for p in players:
  p.currentRoom=room_01.id
  p.save()
