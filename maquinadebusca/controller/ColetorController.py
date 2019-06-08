from flask import Flask, jsonify
app = Flask (__name__)

@app.route("/coleta01")
def iniciar_GET_implicito ():
    return jsonify({"resp": "Coletor iniciado através do método GET IMplicitamente"})

@app.route("/coleta02", methods=['GET'])
def iniciar_GET_explicito ():
    return jsonify({"resp": "Coletor iniciado através do método GET EXplicitamente"})

@app.route("/coleta03", methods=['POST'])
def iniciar_POST ():
    return jsonify({"resp": "Coletor iniciado através do método POST"})

@app.route("/coleta04", methods=['GET', 'POST'])
def iniciar_GET_POST ():
    return jsonify({"resp": "Coletor iniciado através do método GET ou POST"})

if __name__ == "__main__":
    app.run ()