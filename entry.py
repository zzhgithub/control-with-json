from flask import Flask, request
from scheduler_composer import SchedulerComposer
from scheduler_builder import build

app = Flask(__name__)
scheduler_composer = SchedulerComposer()


@app.route("/run")
def run():
    filename = request.args.get("file")
    if scheduler_composer.has(filename):
        schedule = build(filename)
        scheduler_composer.add(filename, schedule)
        schedule.start()
    else:
        pass


@app.route("/pause")
def pause():
    filename = request.args.get("file")
    if scheduler_composer.has(filename):
        scheduler_composer.pause(filename)


@app.route("/resume")
def pause():
    filename = request.args.get("file")
    if scheduler_composer.has(filename):
        scheduler_composer.resume(filename)


if __name__ == "__main__":
    app.run()
