from flask import Flask, render_template, request, redirect
from prometheus_client import Counter, generate_latest, Gauge

app = Flask(__name__)

tasks = []  # Temporary list (no DB)

# 🔥 Metrics
TASKS_TOTAL = Counter('tasks_created_total', 'Total number of tasks created')
TASKS_DELETED = Counter('tasks_deleted_total', 'Total number of tasks deleted')
TASKS_COUNT = Gauge('tasks_count', 'Current number of tasks')

@app.route('/')
def home():
    TASKS_COUNT.set(len(tasks))  # update gauge
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:
        tasks.append(task)
        TASKS_TOTAL.inc()     # 🔥 increase counter
    TASKS_COUNT.set(len(tasks))
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    TASKS_DELETED.inc()        # 🔥 increase counter
    TASKS_COUNT.set(len(tasks))
    return redirect('/')

# 🔥 Prometheus endpoint
@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
