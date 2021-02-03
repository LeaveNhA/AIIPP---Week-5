Mini-project Description
A reminder about the Honor Code 

For previous mini-projects, we have had instances of students submitting solutions that have been copied from the web. Remember, if you can find code on the web for one of the mini-projects, we can also find that code. Submitting copied code violates the Honor Code for this class as well as Coursera's Terms of Service. Please write your own code and refrain from copying. If, during peer evaluation, you suspect a submitted mini-project includes copied code, please evaluate as usual and email the assignment details to iipphonorcode@online.rice.edu. We will investigate and handle as appropriate.

Mini-project description - Pong

In this project, we will build a version of Pong, one of the first arcade video games (1972). While Pong is not particularly exciting compared to today's video games, Pong is relatively simple to build and provides a nice opportunity to work on the skills that you will need to build a game like Asteroids. As usual, we have provided a program template that can be used to guide your development of Pong.

Mini-project development process

Add code to the program template that draws a ball moving across the Pong table. We recommend that you add the positional update for the ball to the draw handler as shown in the second part of the "Motion" video.
Add code to the function 𝚜𝚙𝚊𝚠𝚗_𝚋𝚊𝚕𝚕 that spawns a ball in the middle of the table and assigns the ball a fixed velocity (for now). Ignore the parameter 𝚍𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗 at this point.
Add a call to 𝚜𝚙𝚊𝚠𝚗_𝚋𝚊𝚕𝚕 in the function 𝚗𝚎𝚠_𝚐𝚊𝚖𝚎 which starts a game of Pong. Note that the program template also includes an initial call to 𝚗𝚎𝚠_𝚐𝚊𝚖𝚎 in the main body of your program to get a game going immediately.
Modify your code such that the ball collides with and bounces off of the top and bottom walls. Experiment with different hard-coded initial velocities to test your code.
Add randomization to the velocity in 𝚜𝚙𝚊𝚠𝚗_𝚋𝚊𝚕𝚕(𝚍𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗) The velocity of the ball should be upwards and towards the right if 𝚍𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗 == 𝚁𝙸𝙶𝙷𝚃 and upwards and towards the left if 𝚍𝚒𝚛𝚎𝚌𝚝𝚒𝚘𝚗 == 𝙻𝙴𝙵𝚃. The exact values for the horizontal and vertical components of this velocity should be generated using 𝚛𝚊𝚗𝚍𝚘𝚖.𝚛𝚊𝚗𝚍𝚛𝚊𝚗𝚐𝚎(). For the horizontal velocity, we suggest a speed of around 𝚛𝚊𝚗𝚍𝚘𝚖.𝚛𝚊𝚗𝚍𝚛𝚊𝚗𝚐𝚎(𝟷𝟸𝟶, 𝟸𝟺𝟶) pixels per second. For the vertical velocity, we suggest a speed of around 𝚛𝚊𝚗𝚍𝚘𝚖.𝚛𝚊𝚗𝚍𝚛𝚊𝚗𝚐𝚎(𝟼𝟶, 𝟷𝟾𝟶) pixels per second. (You will need to set the signs of velocities appropriately.)
Add code to the draw handler that tests whether the ball touches/collides with the left and right gutters. (Remember that the gutters are offset from the left and right edges of the canvas by the width of the paddle as described in the "Pong" video.) When the ball touches a gutter, use either 𝚜𝚙𝚊𝚠𝚗_𝚋𝚊𝚕𝚕(𝙻𝙴𝙵𝚃) or 𝚜𝚙𝚊𝚠𝚗_𝚋𝚊𝚕𝚕(𝚁𝙸𝙶𝙷𝚃) to respawn the ball in the center of the table headed towards the opposite gutter.
Next, add code that draws the left and right paddles in their respective gutters. The vertical positions of these two paddles should depend on two global variables. (In the template, the variables were 𝚙𝚊𝚍𝚍𝚕𝚎𝟷_𝚙𝚘𝚜 and 𝚙𝚊𝚍𝚍𝚕𝚎𝟸_𝚙𝚘𝚜.)
Add code that modifies the values of these vertical positions via an update in the draw handler.  The update should reference two global variables that contain the vertical velocities of the paddles. (In the template, the variables were 𝚙𝚊𝚍𝚍𝚕𝚎𝟷_𝚟𝚎𝚕 and 𝚙𝚊𝚍𝚍𝚕𝚎𝟸_𝚟𝚎𝚕.)
Update the values of these two vertical velocities using key handlers. The "w" and "s" keys should control the vertical velocity of the left paddle while the "Up arrow" and "Down arrow" key should control the velocity of the right paddle. In our version of Pong, the left paddle moves up at a constant velocity if the "w" key is pressed and moves down at a constant velocity if the "s" is pressed and is motionless if neither is pressed. (The motion if both are pressed is up to you.) To achieve this effect, you will need to use both a keydown and a keyup handler to increase/decrease the vertical velocity in an appropriate manner.
Restrict your paddles to stay entirely on the canvas by adding a check before you update the paddles' vertical positions in the draw handler. In particular, test whether the current update for a paddle's position will move part of the paddle off of the screen. If it does, don't allow the update.
Modify your collision code for the left and right gutters in step 6 to check whether the ball is actually striking a paddle when it touches a gutter. If so, reflect the ball back into play. This collision model eliminates the possibility of the ball striking the edge of the paddle and greatly simplifies your collision/reflection code.
To moderately increase the difficulty of your game, increase the velocity of the ball by 10% each time it strikes a paddle.
Add scoring to the game as shown in the Pong video lecture. Each time the ball strikes the left or right gutter (but not a paddle), the opposite player receives a point and ball is respawned appropriately.
Finally, add code to 𝚗𝚎𝚠_𝚐𝚊𝚖𝚎 which resets the score before calling 𝚜𝚙𝚊𝚠𝚗_𝚋𝚊𝚕𝚕. Add a "Restart" button that calls 𝚗𝚎𝚠_𝚐𝚊𝚖𝚎 to reset the score and relaunch the ball.
Your final version of Pong should be remarkably similar to the original arcade Pong game. Our full implementation of Pong took a little more than 100 lines of code with comments. For more helpful tips on implementing this mini-project, please visit the Code Clinic Tips page for this mini-project.

Grading Rubric - 19 pts total (scaled to 100 pts)

1 pt - The ball spawns in the middle of the canvas with either an upward left or an upward right velocity. No credit if the ball moves only horizontally left or right. Bleh, that would be boring!
2 pts - The ball bounces off of the top and bottom walls correctly. (1 pt each)
2 pts - The ball respawns in the middle of the screen when it strikes the left or right gutter but not the paddles. (1 pt for each side) Give credit for this item even if the ball hits the edge of the canvas instead of the gutter.
1 pt - The left and right gutters (instead of the edges of the canvas) are properly used as the edges of the table.
1 pt - The ball spawns moving towards the player that won the last point.
2 pts - The 'w' and 's' keys correctly control the velocity of the left paddle as described above. Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to 'w' and 's' key presses.)
2 pts - The up and down arrows keys correctly control the velocity of the right paddle as described above. Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to up and down arrow key presses.)
2 pts - The edge of each paddle is flush with the gutter. (1 pt per paddle)
2 pts - The paddles stay on the canvas at all times. (1 pt per paddle)
2 pts - The ball correctly bounces off the left and right paddles. (1 pt per paddle)
1 pt - The scoring text is positioned and updated appropriately. The positioning need only approximate that in the video.
1 pt - The game includes a "Restart" button that resets the score and relaunches the ball.
