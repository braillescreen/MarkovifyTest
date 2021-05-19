Scrolling Battles, Your World!
By Colton Hill and Ivan Soto
Credits
Thanks to NS Studios and Mason Armstrong for initial sound design, music, testing, and coding.
Thanks to Tunmi for providing (making/recording) some of the music and sound source loops.

This is a quickly thrown together readme.
Welcome to Scrolling Battles, Your World! This isn't exactly a game per say, but it's more like a platforming life simulator. You get to create the world and choose what happens. Which, right now, isn't much.

Notes
To start off with, this game is played online. That means, if you don't have an internet connection, you cannot join in.
Anyone can build maps, but in order for them to show up on menus, they must be added by me. Get in touch if you'd like your map to be approved.
If you want a list of the possible chat commands, type /help

Keys:
Up, down, left and right: Move/climb
Space: Jump
Control arrows: Run, or while jumping, perform a running jump (Moves faster in the air)
Shift arrows: Look in directions
G and arrows: Use camera
F1: Check server version
F2: MOTD
F3: Toggle beacons
Shift F2. Toggle if sonar follows you or not.
Shift F3. Toggle between sonar modes. Step will play per step, and loop will play programatically.
Shift F4. Toggles sonar looping mode speed. Slow, medium, or fast.
F5. Toggle buffer muted or unmuted.
Shift F5: Toggle speech interrupt for a buffer.
f6. Change say (Alt Slash) voice.
f7. Ping to test your lag.
F8: Change online and offline sounds. Must have files in onoffs, on.ogg and off.ogg, smaller than 80 KB
F9. Open a list of all players on the server in order to copy one.
F10: Opens a menu for you to track somebody.
u: Reports the location of the player you're tracking.
f11: Toggle hearing other players' cameras.
slash: Chat
alt slash: Send a SAPI message
alt comma: Slow down say voice
alt period: Speed up say voice
shift slash: Send a map (local) message. Same as prefixing a message with /m
control slash. See who's online
I, J, K, and L. Face the sonar in a different direction when it's not following you.
H: Check health
O: Use Voicechat
Enter: Interact with signs, travelpoints, or doors. Also opens the main menu if in the menu area of a world.
tab. Cycle through inventory forward.
Shift+Tab. Cycle through inventory backward.
Shift+Enter. Use item.
left and right brackets: Switch buffers
backslash. Speak total amount of items in all buffers plus their size.
shift backslash. Export buffers to log files. Warning! This will clear all buffers! Note this is automatically done upon logging out of the game.
Comma and Dot: Switch between buffer items
shift comma and dot: Move to the top and bottom of the buffer.
Shift c: Copy buffer item.
P. If you are a contributor of a map, open the builder.
F: If you have it, attempt to hook upwards.
V: If you have it, attempt to hook downwards.
Up/Down climb on a hook once it has hooked.
home and end: Adjust master volume.
page up and down: Adjust ambience volume.
control page up and down: Adjust music volume for in-map music

If you are in a list of surfaces, holding spacebar will preview the selected surface. (Builder)
If you are in a list of ambiences, space will read you the currently selected ambience.
If you are in a list of maps, up and down arrows will move up and down by 10 maps.

Virtual input
As of 4.7.5, the virtual input, the programatic text box that doesn't actually show up on the screen, has been dramatically improved. Version 4.7.6 saw selection features. Version 4.7.7 saw more robust features and better standardization of controls.
Keystrokes are as follows:
left/right arrows: move by character.
control+left/right arrows: move by word.
up/down arrows: In multiline inputs, move by line. In single-line inputs, reads the contents of the input without affecting the cursor position.
Note: As with standard behavior in multiline edit controls with only one line in them, pressing up and down arrow will navigate to the beginning and end of this line respectively.
home/end: go to the beginning and end of the current line respectively, when in multiline inputs. If in single line input, acts as control+home/end.
control+home/end: Go to the beginning and end of the whole text respectively.
If shift is held with these movement gestures, extends selection in said direction and size.
control+up/down arrows: In multiline inputs, read out the contents of the input. With shift, reads selected text, if any.
shift+enter: Insert a line break in multiline inputs.
backspace: Delete character behind the cursor and back up the cursor,, as backspace normally does in edit controls. Reports the deleted character. Alternatively if there is a selection, acts as delete.
delete: Delete character at the cursor and report the new character at the cursor. Alternatively if there is a selection, deletes the selection and moves the cursor to the beginning of the area where the selection would have been.
shift+delete or shift+backspace: Clear the input. The same may be accomplished with control+a, backspace/delete.
control+a: Select all of the text in the input.
control+x: Copies the selection to the clipboard and removes it from the input (cut).
control+c: Copy selected text, if there is a selection, otherwise the whole input, to the clipboard.
control+v: Paste text from the clipboard at the cursor position. Note: if the clipboard contains multiline text but you are pasting into a single line input, the text will be truncated at the first line break.
enter: Submit input.
escape: Cancel input.
f2: Cycle through echo options. None, characters, words, or both characters and words. Useful if you normally use this function but your screen reader is hooked or asleep.
f3: Toggle reporting of capital letters. Either beep and speak letter, speak cap letter, or no change. It's usually necessary to have this make a distinction between capital and lowercase because the screen reader isn't naturally in character mode when passing over characters in these inputs.
tab: Read the prompting message presented with this input. E.G. Enter your username.
Note: If there is a selection, any addition of text to the input by typing or pasting automatically deletes the selected text, replacing it with that which was entered.
Note 2: If instead the cursor is just moved by a navigation gesture but without holding shift, unselects the selected text.

Builder points (paid users only)
Builder points as of version 4.7, allow you to use the camera to set min x, max x, min y and max y values.
Hold down the G key to activate the camera and move the camera around to your liking.
Once the camera is where you want it, press J, L, K and I to place selection points.
You can press APOSTROPHE to here where the selection points are set, or press the semicolon key to clear the selection points all at once.
Do note that whenever the selection points are used, I.E, if a staircase or hazard is built using these selection points, they are cleared.

Sonar
The sonar, new in 3.0.7, plays sounds based on what's around you. It will scan in the direction you are facing and play a sound where there is an object (Either a hazard, a wall, air, a staircase (Up or down), and a new surface.
If you toggle off the sonar following you, you can face it in whatever direction you want, and walk, and it will scan in the direction you want rather than your current direction.
When you are jumping or falling, the sonar will scan both above, below, and if you start moving, in the direction you are moving. This will allow you to see if you are falling into a hazard or a platform.

The Builder
New in 2.4.0, the builder will allow you to easily and efficiently create maps. Just select what you would like to spawn, and press enter. It will guide you through a wizard asking you for the things it needs to successfully spawn the selected item.
If you would like to remove an item, type slash rawmap. Go to the end of the buffer, and press control C. Now, open notepad or your prefered editor of choice, and paste in the text. Review the lines that you would like to remove or edit, edit them, copy the text back to your clipboard, not one line, all of the text, and in the game chat box, type /rawdata, space, and paste. Then hit enter, and your changes will be made.


Spawn points
Adds a spawn point (Where the server will spawn you when the map loads). You don't need one for the map to work.

Signs
Signs make a periodical beeping noise notifying you of their presence. Press enter on one to read it's text.

How to build a map.
you first need to type /newmap nameOfMapWithNoSpaces maxx defaultTile
Example
/newmap forest 500 grass

Description of perametors, in order
perametor one, name.
This is what your map will be called. It may not contain spaces.
perametor 2, maxx
how long your map is.
perametor 3, default tile
the surface your map is.

Your new map will then be created and you will be placed on it.

Your map can be edited one of two ways. With the builder, previously discussed above, or the raw text of your map. We strongly recommend you use the builder.

If you wish to use text, you can type
/rawmap
This will send the code of your current map into a chat, which then can be copied into a notepad and edited.

Once you've finished editing your map, you can type:
/rawdata 
then paste the contents back. This will send the map to the server and update you and any other players on that map with the new map.

You can change your map by typing: /changemap mapNameWithoutExtension
If you want to change your map to your map and to a certain set of coordinates, type /changemap mapname x y
You can only change your map to a map created by you or a map you have rights to edit.

If you are creating a map, and you would like to allow a specific person to visit or edit it, you can add a line to the bottom of your map code, by first copying it by typing /rawmap, going to the bottom of your buffer, pressing control C, and pasting it into notepad. Create a new line at the bottom and type contributor person. example: contributor masonasons
Then, copy all the text and type /rawdata space and then paste. (When I say space, I mean actually press the space bar, not type out the word space.)
If you would no longer like this person to be able to contribute, remove that line from your map.

Likewise, if you would like your map to be publicly available to anyone, either select publicize map from the builder, or add a line that says public to your map.

If you want to delete a map, type
/delmap mapNameWithoutExtension

/contributions will give you a list of all maps on the server that you can contribute to.

Contact
Email: ivansoto9923@gmail.com
skype: isoto680
twitter: ivan_soto00

Enjoy!