from flask import Flask
from flask import request
from find_graph import *
from networkx.readwrite import json_graph
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def signin_form():
    webform = '<form action="/result" method="post">'
    webform += '''<div style="margin: auto;width: 100px;padding: 10px;">
<button type="submit" style="background-color: #535456;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;">Submit</button></div>'''
    webform += '<p style="margin: auto;width: 300px;padding: 10px; font-size:20px">num_vertex:<input name="vertex"></p>'
    webform += '<p style="margin: auto;width: 300px; font-size:20px">proprieties to vary: <select name="s_t_v"></p>'
    webform += '''
            <p><option></option>
            <option value="0">GCC</option>
            <option value="1">ACC</option>
            <option value="2">SCC</option>
            <option value="3">APL</option>
            <option value="4">r</option>
            <option value="5">diam</option>
            <option value="6">den</option>
            <option value="7">Rt</option>
            <option value="8">Cv</option>
            <option value="9">Ce</option>
          </select></p>
    '''
    webform += '<h3>please pick some proprieties to fix: </h3>'
    for i in range(10):
        webform += '''<div style="margin: 5px; border: 2px solid black;border-radius: 12px; 
        width: 240px; padding-left: 10px;float: left">'''
        webform += '<p>proprieties ' + str(i) + ': <select name="s' + str(i) + '">'
        webform += '''
                <option></option>
                <option value="0">GCC</option>
                <option value="1">ACC</option>
                <option value="2">SCC</option>
                <option value="3">APL</option>
                <option value="4">r</option>
                <option value="5">diam</option>
                <option value="6">den</option>
                <option value="7">Rt</option>
                <option value="8">Cv</option>
                <option value="9">Ce</option>
              </select></p>
        '''
        webform += '<p>min:<input name="min' + str(i) + '"></p>'
        webform += '<p>max:<input name="max' + str(i) + '"></p></div>'
    webform += '</form>'

    return webform


@app.route('/result', methods=['POST'])
def signin():
    graph_dict = {}
    vertex_num = int(request.form["vertex"])
    global stat_to_vary
    stat_to_vary = str(request.form['s_t_v'])
    result = ''
    for i in range(10):
        s = str(request.form['s' + str(i)])
        min = str(request.form['min' + str(i)])
        max = str(request.form['max' + str(i)])
        if s == '':
            continue
        elif min == '' and max == '':
            continue
        elif min == '':
            min = '-1.0'
        elif max == '':
            max = '1.0'
        if s in graph_dict:
            return '<h3> Invalid Input</h3>'
        graph_dict[s] = min + '~' + max

    for key in graph_dict:
        result += key + ':' + graph_dict[key] + ' '
    astring = result.strip(' ')
    gp = GraphProcessor()
    global g_list

    if stat_to_vary == '':
        g_list = gp.find_graph(vertex_num, astring, 4)
    else:
        g_list = gp.find_same_stat_graph(vertex_num, astring, int(stat_to_vary))

    # g_list = gp.find_graph(3, "0:0~0 1:0~0 2:0~0")
    result = ''
    stat_list = ['GCC', 'ACC', 'SCC', 'APL', 'r', 'diam', 'den', 'Rt', 'Cv', 'Ce']
    for i in range(len(g_list)):
        result += '''<div style="margin: 5px; border: 2px solid black; 
        padding: 10px;float: left"><iframe src="/graph'''
        result += str(i) + '.html" height="275" width="325"></iframe>'
        result += '<p>' + stat_list[int(stat_to_vary)] + ' in range of: '
        if stat_to_vary == '4':
            result += "{0:.1f}".format(-1 + 0.2 * i) + '~' + "{0:.1f}".format(-0.8 + 0.2 * i) + '</p></div>'
        else:
            result += "{0:.1f}".format(0.1 * i) + '~' + "{0:.1f}".format(0.1 + 0.1 * i) + '</p></div>'
    return result


@app.route('/graph0.json', methods=['GET', 'POST'])
def g0json():
    graph = g_list[0]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph0.html', methods=['GET', 'POST'])
def g0html():
    return write_html('/graph0.json')


@app.route('/graph1.json', methods=['GET', 'POST'])
def g1json():
    graph = g_list[1]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph1.html', methods=['GET', 'POST'])
def g1html():
    return write_html('/graph1.json')


@app.route('/graph2.json', methods=['GET', 'POST'])
def g2json():
    graph = g_list[2]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph2.html', methods=['GET', 'POST'])
def g2html():
    return write_html('/graph2.json')


@app.route('/graph3.json', methods=['GET', 'POST'])
def g3json():
    graph = g_list[3]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph3.html', methods=['GET', 'POST'])
def g3html():
    return write_html('/graph3.json')


@app.route('/graph4.json', methods=['GET', 'POST'])
def g4json():
    graph = g_list[4]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph4.html', methods=['GET', 'POST'])
def g4html():
    return write_html('/graph4.json')


@app.route('/graph5.json', methods=['GET', 'POST'])
def g5json():
    graph = g_list[5]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph5.html', methods=['GET', 'POST'])
def g5html():
    return write_html('/graph5.json')


@app.route('/graph6.json', methods=['GET', 'POST'])
def g6json():
    graph = g_list[6]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph6.html', methods=['GET', 'POST'])
def g6html():
    return write_html('/graph6.json')


@app.route('/graph7.json', methods=['GET', 'POST'])
def g7json():
    graph = g_list[7]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph7.html', methods=['GET', 'POST'])
def g7html():
    return write_html('/graph7.json')


@app.route('/graph8.json', methods=['GET', 'POST'])
def g8json():
    graph = g_list[8]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph8.html', methods=['GET', 'POST'])
def g8html():
    return write_html('/graph8.json')


@app.route('/graph9.json', methods=['GET', 'POST'])
def g9json():
    graph = g_list[9]
    json_g = json.dumps(json_graph.node_link_data(graph))
    return json_g


@app.route('/graph9.html', methods=['GET', 'POST'])
def g9html():
    return write_html('/graph9.json')


def write_html(f_name):
    result = '''<script src="http://d3js.org/d3.v2.min.js?2.9.3"></script>
<style>

.link {
  stroke: #aaa;
}

.node text {
stroke:#333;
cursos:pointer;
}

.node circle{
stroke:#fff;
stroke-width:3px;
fill:#555;
}


</style>
<body>
<script>

var width = 300,
    height = 250

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

var force = d3.layout.force()
    .gravity(.1)
    .distance(100)
    .charge(-100)
    .size([width, height]);

'''
    result += 'd3.json("' + f_name + '", function(json) {'
    result += '''force
      .nodes(json.nodes)
      .links(json.links)
      .start();

  var link = svg.selectAll(".link")
      .data(json.links)
    .enter().append("line")
      .attr("class", "link")
    .style("stroke-width", function(d) { return Math.sqrt(d.weight); });

  var node = svg.selectAll(".node")
      .data(json.nodes)
    .enter().append("g")
      .attr("class", "node")
      .call(force.drag);

  node.append("circle")
      .attr("r","5");

  node.append("text")
      .attr("dx", 12)
      .attr("dy", ".35em")
      .text(function(d) { return d.name });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
  });
});


</script>
'''
    return result


if __name__ == '__main__':
    app.run(port=4000)
