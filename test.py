import os_image_handler.image_handler as ih

# create a background canvas with a background gradient color
background = ih.create_new_image(1024, 500, None, '#FFC1B', '#FF881B')

# add text
ih.draw_text_on_img(background, 'Ball Game!', 20, 20, '#FFFFFF', '/Users/home/Library/Fonts/Consolas.ttf', 150)

# add the ball image
ball = ih.load_img('/Users/home/Desktop/icons/ball.png')
ball = ih.resize_img_by_width(ball, 250)
ih.paste_image(background, ball, 150, 200)

# add the happy lady image
happy_lady = ih.load_img('/Users/home/Desktop/icons/happy.png')
happy_lady = ih.resize_img_by_width(happy_lady, 250)
happy_lady = ih.tilt_image(happy_lady, 45)
ih.paste_image(background, happy_lady, background.width-happy_lady.width*0.7, background.height/2)

# save
ih.save_img(background, '/Users/home/Desktop/ball_game_img.png')
