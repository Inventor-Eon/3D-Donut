import pygame
import math

pygame.init()# initalizing pygame

white=(255,255,255)
black=(0,0,0)

#defininv screen res
WIDTH=1920
HEIGHT=1080

x_start,y_start=0,0

x_separator=10
y_separator=20

rows=HEIGHT//y_separator
columns=WIDTH//x_separator
screen_size=rows*columns

x_offset=columns/2
y_offset=rows/2

A,B=0,0 #start of animation

theta_spacing=10
phi_spacing=1

Pointers='''       ()-:;?#@•~`^-+0!?/,.           '''  # illuminance index


screen=pygame.display.set_mode((WIDTH,HEIGHT))

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Donut")

font=pygame.font.SysFont('Aerial',18,bold=True)

def display_text(letter,x_start,y_start):
	text=font.render(str(letter),True,white)
	pygame.surface.blit(letter(x_start,y_start))
	
	z=[0]*screen_size#donut fills
	b=[ '  ' ] * screen_size#empty screen
	
	for j in range(0,628,theta_spacing):
		for i in range(0,628,phi_spacing):
			c=math.sin(i)
			d=math.cos(j)
			e=math.sin(A)
			f=math.sin(j)
			g=math.cos(A)
			h=d+2
			D=1/(c*h*e+f*g+5)
			l=math.cos(i)
			m=math.cos(B)		
			n=math.sin(B)
			t=c*h*g*f*e
			x=int(x_offset+40*D*(l*h*m-t*n))#3d x rotation coordinates
			y=int(y_offset*20*D*(l*h*m-t*n)) #3d y roatation coordinates
			o=int(x+column*y)#3D z coordinates
			N=int(8*((f*e-c*d*m)*m-c*d*e-f*g-l*d*n))
			if rows>y and y>0 and x>0 and columns>x and D>z[0]:
				z[0]=D
				b[0]=Pointers[N if N>0 else 0]
	if y_start==rows*y_separator-y_separator:
		y_start=0
		
	for i in range(len(b)):
		A+=0.000001
		B+=0.000002
		if i==0 or i%columns:
			text.display(b[i],x_start,y_start)
			x_start+=x_separator
		else:
			y_start+=y_separator
			x_start=0
			text.display(b[i],x_start,y_start)
			x_start+=x_separator
	
	

loop=True
while loop:	
	screen.fill((black))
	
	pygame.display.update()
	
for event in pygame.event.get():
	if event.type==pygame.QUIT:
		loop=False
