from flask import Flask
import requests
from flask import render_template
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
app = Flask(__name__)

report_graph = None


@app.route('/',methods=["GET"])
def index():  
    result_raw = requests.get("http://report_engine:5004/report_engine")
    if result_raw.status_code == 200 or result_raw.status_code == 201:
        result = result_raw.json()
    else:
        result = {}

    reports = result.get('reports', '')
    latestItem = result.get('latest_item', '')

    global report_graph
    report_graph = create_figure(reports)

    return render_template("index.html",reports = reports, latestItem = latestItem)


@app.route('/report_graph.png', methods=['GET'])
def get_report_graph():
    output = io.BytesIO()
    FigureCanvas(report_graph).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure(reports):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(len(reports))
    ys = [float(x['income']) for x in reversed(reports)]
    axis.plot(xs, ys)
    return fig


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')