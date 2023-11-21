from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from tkinter.ttk import *
from add import *
from delete import *
from view import *

mypass = "Naruto@123"
mydatabase = "Music"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

def play_selected_track(track_title_var):
    selected_track_title = track_title_var.get()

    if selected_track_title:
        try:
            # Fetch additional track information (you may modify this query based on your needs)
            cur.execute(f"SELECT title, artist_name, album_name, genre_name, play_count FROM Track "
                        f"JOIN Artist ON Track.artist_id = Artist.id "
                        f"JOIN Album ON Track.album_id = Album.id "
                        f"JOIN Genre ON Track.genre_id = Genre.id "
                        f"WHERE Track.title = '{selected_track_title}'")
            track_info = cur.fetchone()

            if track_info:
                title, artist, album, genre, play_count = track_info
                messagebox.showinfo("Now Playing", f"Now playing: {title} by {artist} from album {album} (Genre: {genre})\nPlay Count: {play_count}")

                # Update play count in the database
                cur.callproc('update_play_count', (selected_track_title,))
                con.commit()

                # Add your actual audio playback logic here
                print(f"Simulating audio playback for: {title}")

            else:
                messagebox.showinfo("Error", "Track not found.")

        except Exception as e:
            print(f"Error: {e}")
            messagebox.showerror("Error", f"An error occurred while fetching track information: {e}")
    else:
        messagebox.showinfo("Error", "Please select a track.")


# ... (your existing code)

def refresh_total_songs():
    display_total_songs_by_genre()



def placeholder_play_track():
    messagebox.showinfo("Placeholder", "This is a placeholder for playing a track. Add your audio playback logic here.")

def update_total_songs_by_genre(genre_name, increment):
    try:
        cur.callproc('update_total_songs', (genre_name, increment))
        con.commit()
    except Exception as e:
        con.rollback()
        print(f"Error: {e}")

def display_total_songs_by_genre():
    try:
        # Fetch data dynamically from the Track table
        cur.execute("SELECT Genre.genre_name, COUNT(Track.title) AS total_songs "
                    "FROM Genre "
                    "LEFT JOIN Track ON Genre.id = Track.genre_id "
                    "GROUP BY Genre.genre_name;")
        data = cur.fetchall()

        if data:
            messagebox.showinfo("Total Songs by Genre", "\n".join([f"{genre}: {total_songs} songs" for genre, total_songs in data]))
        else:
            messagebox.showinfo("Total Songs by Genre", "No data available.")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", "An error occurred while fetching data.")


def display_most_pop_song():
    try:
        cur.execute("SELECT total_songs_by_genre();")
        most_popular_genre = cur.fetchone()[0]

        if most_popular_genre:
            messagebox.showinfo("Most Popular Genre", f"Most Popular Genre: {most_popular_genre}")
        else:
            messagebox.showinfo("Genre", "No data available.")
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "An error occurred while fetching data.")
    



# Fetch all tracks for the dropdown
cur.execute("SELECT title FROM Track;")
tracks_data = cur.fetchall()
tracks_list = [track[0] for track in tracks_data]

root = Tk()
root.title("Music Library Management System")
root.minsize(width=700, height=700)
root.geometry("800x600")

background_image = Image.open("images\main.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth * 0.7)
newImageSizeHeight = int(imageSizeHeight * 0.7)
background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight))
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#dfdee2", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to\nMusic Library Management System", bg="black", fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

selected_track_id_var = StringVar()

btn1 = Button(root, text="Add Track", font='Helvetica 10 bold', bg='black', fg='white', command=addsong)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Track", font='Helvetica 10 bold', bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Tracks", font='Helvetica 10 bold', bg='black', fg='white', command=view)
btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Total Songs by Genre", font='Helvetica 10 bold', bg='black', fg='white',
              command=display_total_songs_by_genre)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Most Pop Genre", font='Helvetica 10 bold', bg='black', fg='white',
              command=display_most_pop_song)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

track_combobox = Combobox(root, textvariable=selected_track_id_var, values=tracks_list, state="readonly", font='Helvetica 10 bold')
track_combobox.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

btn_play = Button(root, text="Play Track", font='Helvetica 10 bold', bg='black', fg='white', command=lambda: play_selected_track(selected_track_id_var))
btn_play.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)


btn_refresh = Button(root, text="Refresh", font='Helvetica 10 bold', bg='black', fg='white', command=refresh_total_songs)
btn_refresh.place(relx=0.75, rely=0.6, relwidth=0.1, relheight=0.1)



root.mainloop()
