# open powershell
# iwr https://fly.io/install.ps1 -useb|iex
# flyctl auth login

# fly apps create --name unclelist555

# cd to source code directory
# change name  python file too , main.py
# fly deploy
# fly open


#git clone https://github.com/fly-apps/hello-fly.git
#cd hello-fly
#fly launch --now



from flet import *

def main(page: Page):
    page.title = "Uncle To Do by Uncle Engineer"  # ชื่อหน้าต่าง (Desktop)
    
    tasks = Column()
    task_input = TextField(label="พิมพ์รายการใหม่")

    # ฟังก์ชันลบ task
    def delete_task(e):
        task_row = e.control.data  # ดึง Row ที่ผูกไว้ในปุ่มลบ
        tasks.controls.remove(task_row)
        page.update()

    def add_task(e):
        if task_input.value.strip() == "":
            return

        # สร้างแถว Row ที่เก็บ checkbox และปุ่มลบ
        task_row = Row(
            controls=[
                Checkbox(label=task_input.value),
                IconButton(icon=icons.DELETE, on_click=delete_task)
            ]
        )
        task_row.controls[1].data = task_row

        tasks.controls.append(task_row)
        task_input.value = ""
        page.update()

    # เพิ่มหัวข้อแอปบนสุด
    app_title = Text("📝 Uncle To Do by Uncle Engineer", size=20, weight="bold")

    # เพิ่มทุกอย่างลงหน้า
    page.add(
        Container(height=50),
        app_title,
        task_input,
        ElevatedButton("เพิ่มรายการ", on_click=add_task, color='blue'),
        tasks
    )

app(target=main)