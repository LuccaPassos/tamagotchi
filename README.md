# tamagotchicro:bit
A tamagotchi inspired code for BBC's micro:bit. The main objective is to keep the virtual pet alive and happy for as long as possible.

The code is not commented and the variable's names are not intuitive because of the way microbit's memory works. Big variable names and comments actually make the code's size bigger and sometimes the board can't handle it. 

## Gameplay
All interactions must happen while the pet is looking at the player, otherwise they'll not work.

### Beginning
The tamagotchicro:bit starts with 100 health (or happiness) and it has a 10% chance of dropping by 10 every 10 seconds. At this stage, it's happy and very interested, looking often at the player. Its face changes by pressing Button A or button B as if the player was pinching its cheeks (but it has no real effects).

### Menu
There's a menu and it can be accessed by pressing buttons A and B simultaneously. Then button A moves it to the left and B moves it to the right. There are two options, one is a pacman and the other is a cross and they can be selected by pressing A and B simultaneously again.

### Health
The player is able to give the tamagotchicro:bit some love by petting it or playing with it. 
- To pet, the GND and 0 pins should be touched simultaneously and a heart should appear. This makes its health go up by 2.
- To play, the menu must be opened by pressing buttons A and B at the same time and then selec the pacman. This makes its health go up by 10.

### Anger
The tamagotchicro:bit can get a little angry when it's shook. It displays an angry face and its health drops by 20.

### Sickness
The tamagotchicro:bit can get sick if it's held face side down. It must be healed and it can be done by chosing the cross option at the menu.

### Sleep
The tamagotchicro:bit starts to sleep if it's not moving. To wake it up, just move it around.


## Stages
The tamagotchicro:bit has 4 stages of emotions (except sick), directly based on its health. They are expressed by different animations shown on the 5 led matrix.
As it gets sadder, it gets harder to make it happy again.

### Stage 1
The first stage happens when the health is higher or equal to 70. It randomly looks around, but it looks more at the player as it's more interested.

### Stage 2
This stage happens when the health between 70 and 40. It randomly looks around but spends more time at it, not very interested in the player.

### Stage 3
This stage happens when the health between 40 and 10. At this stage it's crying a lot and it is very difficult to interact with it. Its time is near.

### Stage 4
If the health drops below 10, the tamagotchicro:bit dies, and its age is shown in milliseconds.
