from PyQt6.QtWidgets import QHBoxLayout, QScrollArea, QVBoxLayout, QWidget, QFrame
from qfluentwidgets import (InfoBar, 
    InfoBarPosition, 
    PrimaryPushButton,
    ProgressRing, 
    TransparentPushButton,
    FluentIcon as FI
)
from config import INFO_BAR_DURATION_SHORT, current_day
from core.data_loader import load_todays_tasks, save_todays_tasks
from core.models.task import Task
# from ui.widgets.add_task_dialog import AddTaskDialog
from ui.widgets.card import SimpleCard, TaskCard
from ui.widgets.title_bar import TitleBar
from core.utils.logger import logger

class DailyPage(QWidget):
    """Daily page showing today's tasks with progress tracking and also many features."""
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        logger.info("Initializing DailyPage")
        # main Layout of this page
        self.page_layout = QVBoxLayout(self)
        self.page_layout.setContentsMargins(0,0,0,0)
        self.tasks = load_todays_tasks(current_day)
        
        self._build_ui()
        logger.info(f"DailyPage initialized with {len(self.tasks)} tasks")

    def _build_ui(self):
        """Build the UI components for the daily page."""
        # ======= Header =========
        # title shown on top of the page
        self.title = TitleBar(self,"My Task")
        self.page_layout.addWidget(self.title)

        # ======= Header Area ========
        self.progress_ring = ProgressRing()
        self.progress_ring.setFixedSize(48, 48)
        self.progress_ring.setTextVisible(True)
        progress_card = SimpleCard()
        progress_card.setWidget(self.progress_ring)
        self.page_layout.addWidget(progress_card)

        # ======= Main Content ======
        # Scroll Area for the Tasks List
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setStyleSheet("QScrollArea{background: transparent; border: none;}")

        # main container for Tasks List
        self.list_container = QWidget()
        self.list_container.setStyleSheet("background: transparent;")
        self.list_layout = QVBoxLayout(self.list_container)
        self.list_layout.setContentsMargins(6, 4, 6, 4)
        self.list_layout.setSpacing(8)

        self.scroll_area.setWidget(self.list_container)
        self.page_layout.addWidget(self.scroll_area)

        # ========== Footer =========
        # clear complete and Add Task Button Area
        footer = QHBoxLayout()
        self.clr_task_btn = TransparentPushButton("Clear Completed")
        self.clr_task_btn.clicked.connect(self._on_clear_completed)
        footer.addWidget(self.clr_task_btn)
        footer.addStretch(1)
        add_btn = PrimaryPushButton(FI.ADD,"Add Task")
        footer.addWidget(add_btn)
        self.page_layout.addLayout(footer)

        for task in self.tasks:
            card = TaskCard(task)
            card.checkbox_changed.connect(self.update_stats)
            card.edit_clicked.connect(self._on_edit_task)
            card.delete_clicked.connect(self._on_delete_task)
            self.list_layout.addWidget(card)
            
        self.list_layout.addStretch(1)

    def _add_task(self, time,task_name, priority):
        """Add a new task to the task list."""
        
        task = Task(
            time = time,
            task = task_name,
            priority = priority,
            done = False,
        )
        self.tasks.append(task)
        save_todays_tasks(self.tasks)
        
        InfoBar.success(
            title="Task added",
            content=task.task,
            duration=INFO_BAR_DURATION_SHORT,
            position=InfoBarPosition.TOP,
            parent=self,
        )
        
    def update_stats(self, checked=None):
        """Update progress ring based on completed tasks."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.done)
        percent = int(completed / total * 100) if total else 0
        
        self.progress_ring.setValue(percent)

    def _on_edit_task(self, task: dict):
        ...
    def _on_delete_task(self, task: dict):
        ...
    def _on_clear_completed(self):
        ...

    def _refresh_task_list(self):
        ...
