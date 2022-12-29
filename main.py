import customtkinter
from tkintermapview import TkinterMapView
import aStar
import DFS
import BFS
import Data
import tkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")      # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")   # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    

    WIDTH = 1200
    HEIGHT = 700
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        photo = tkinter.PhotoImage(file ="lol.ico")
        my_image = customtkinter.CTkImage(light_image=Image.open("logo.png"),
                                  dark_image=Image.open("logo.png"),
                                  size=(70, 40))

        self.f=0
        self.t=0
        self.iconphoto(False, photo)
        self.title(" ")
        self.geometry(f"{str(App.WIDTH)}x{str(App.HEIGHT)}")
        self.minsize(App.WIDTH, App.HEIGHT)
        # self.resizable(False,False)

        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)

        self.marker_list = []

        #                   create two CTkFrames 

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, pady=0, padx=0, sticky="nsew")


        #####################################################   from button  ##################################################
        self.image_label = customtkinter.CTkLabel(self.frame_left,image=my_image, text=None, anchor="w" )
        self.image_label.grid( padx=(20, 20), pady=(20, 0))

        #####################################################   from button  ##################################################
        self.from_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["el shohada","quwaysna","tala","birket as sab", "el-bagour","ashmun", "minuf", "shebin","el sadat city","Kafr El-Zayat","basioun","tanta","qutur","El-Mahalla El-Kubra","As Santah","Samannoud","zefta","banha","qalyub","Al Qanatir Al Khayriyyah","Shubra Al Khaymah","el khankah","kafr shokr","shibin el qanatir","toukh"],dynamic_resizing=False,command=self.change_map_from,fg_color="#087f5b")
        self.from_menu.grid( padx=(20, 20), pady=(70, 0))
        #####################################################   to button     ##################################################
        self.to_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["el shohada","quwaysna","tala","birket as sab", "el-bagour","ashmun", "minuf", "shebin","el sadat city","Kafr El-Zayat","basioun","tanta","qutur","El-Mahalla El-Kubra","As Santah","Samannoud","zefta","banha","qalyub","Al Qanatir Al Khayriyyah","Shubra Al Khaymah","el khankah","kafr shokr","shibin el qanatir","toukh"],dynamic_resizing=False,command=self.change_map_to,fg_color="#087f5b")
        self.to_menu.grid( padx=(20, 20), pady=(20, 0))
        #####################################################     BFS     ####################################################

        self.bfs = customtkinter.CTkButton(master=self.frame_left,
                                                text="BFS",
                                                command=self.show_bfs,fg_color="#087f5b",corner_radius=50)
        self.bfs.grid(pady=(250, 0), padx=(20, 20))

        #####################################################    DFS     ####################################################


        self.dfs = customtkinter.CTkButton(master=self.frame_left,
                                                text="DFS",
                                                command=self.show_dfs,fg_color="#087f5b",corner_radius=50)
        self.dfs.grid(pady=(10, 0), padx=(20, 20))
        
        #####################################################   A*     ####################################################

        self.a_star = customtkinter.CTkButton(master=self.frame_left,
                                                text="A*",
                                                command=self.show_a_star,fg_color="#087f5b",corner_radius=50)
        self.a_star.grid(pady=(10, 0), padx=(20, 20))


        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
        self.map_widget.grid(row=1, column=0, sticky="nswe", padx=(0, 0), pady=(0, 0))

        # Set default values
        self.map_widget.set_address("menouf ")
        self.map_widget.set_zoom(13)
        self.from_menu.set("From")
        self.to_menu.set("To")

    def show_a_star(self):
        self.map_widget.set_zoom(10)
        self.map_widget.delete_all_marker()
        self.map_widget.delete_all_path()
        if self.from_menu.get()!="From" and  self.to_menu.get()!="To":
            path=aStar.A_star(self.from_menu.get(),self.to_menu.get())
            path_1=[]
            for city in path:
                path_1.append(Data.Coordinates[city])
                self.map_widget.set_marker(path_1[-1][0],path_1[-1][1])
            self.map_widget.set_path(path_1)
           
    def show_bfs(self):
        self.map_widget.set_zoom(10)
        self.map_widget.delete_all_marker()
        self.map_widget.delete_all_path()
        if self.from_menu.get()!="From" and  self.to_menu.get()!="To":
            path=BFS.BFS(self.from_menu.get(),self.to_menu.get())
            path_1=[]
            for city in path:
                path_1.append(Data.Coordinates[city])
                self.map_widget.set_marker(path_1[-1][0],path_1[-1][1])
            self.map_widget.set_path(path_1)
 
    def show_dfs(self):
        self.map_widget.set_zoom(10)
        self.map_widget.delete_all_marker()
        self.map_widget.delete_all_path()
        if self.from_menu.get()!="From" and  self.to_menu.get()!="To":
            path=DFS.DFS(self.from_menu.get(),self.to_menu.get())
            path_1=[]
            for city in path:
                path_1.append(Data.Coordinates[city])
                self.map_widget.set_marker(path_1[-1][0],path_1[-1][1])
            self.map_widget.set_path(path_1)
           
            

    # def change_appearance_mode(self, new_appearance_mode: str):
    #     customtkinter.set_appearance_mode(new_appearance_mode)


    def change_map_from(self, new_map: str):
        self.map_widget.set_position(Data.Coordinates[self.from_menu.get()][0],Data.Coordinates[self.from_menu.get()][1])
        self.map_widget.set_zoom(13)
    def change_map_to(self, new_map: str):
        self.map_widget.set_position(Data.Coordinates[self.to_menu.get()][0],Data.Coordinates[self.to_menu.get()][1])
        self.map_widget.set_zoom(13)
    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()