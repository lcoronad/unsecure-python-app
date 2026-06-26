from flask import Flask, request

from app import command, crypto, deserialization, file_io, sql

app = Flask(__name__)


@app.get("/util/ping")
def ping():
    host = request.args.get("host", "")
    return command.ping_host(host)


@app.get("/db/user")
def db_user():
    name = request.args.get("name", "")
    return {"rows": sql.buscar_usuario(name)}


@app.get("/files/read")
def files_read():
    path = request.args.get("path", "")
    return file_io.read_file(path)


@app.post("/api/import/pickle")
def import_pickle():
    data = request.get_data()
    return {"result": str(deserialization.load_pickle(data))}


@app.post("/api/import/yaml")
def import_yaml():
    body = request.get_data(as_text=True)
    return {"result": str(deserialization.load_yaml(body))}


@app.post("/auth/hash")
def auth_hash():
    payload = request.get_json(silent=True) or {}
    password = payload.get("password", "")
    return {"hash": crypto.hash_password(password)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
