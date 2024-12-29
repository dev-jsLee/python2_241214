import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class TodoList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 레이아웃 설정
        layout = QVBoxLayout(central_widget)
        
        # 입력 부분 레이아웃
        input_layout = QHBoxLayout()
        
        # 할 일 입력창
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText('할 일을 입력하세요')
        
        # 추가 버튼
        add_button = QPushButton('추가')
        add_button.clicked.connect(self.add_task)
        
        # 입력 레이아웃에 위젯 추가
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_button)
        
        # 할 일 목록
        self.task_list = QListWidget()
        
        # 삭제 버튼
        delete_button = QPushButton('체크된 항목 삭제')
        delete_button.clicked.connect(self.delete_task)
        
        # 메인 레이아웃에 모든 요소 추가
        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)
        layout.addWidget(delete_button)
        
        # 창 설정
        self.setWindowTitle('Todo List')
        self.setGeometry(300, 300, 400, 500)
        
    def add_task(self):
        task = self.task_input.text()
        if task:
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.task_list.addItem(item)
            self.task_input.clear()
            
    def delete_task(self):
        items_to_remove = []
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            if item.checkState() == Qt.Checked:
                items_to_remove.append(item)
        
        for item in items_to_remove:
            self.task_list.takeItem(self.task_list.row(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_list = TodoList()
    todo_list.show()
    sys.exit(app.exec_())