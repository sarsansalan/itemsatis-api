from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/clean_duplicates')
def clean_duplicates():
    try:
        with open("itemsatis.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        
        unique_lines = list(dict.fromkeys(lines))
        
        with open("itemsatis.txt", "w", encoding="utf-8") as f:
            for line in unique_lines:
                f.write(line + "\n")
        
        return jsonify({
            "status": "success",
            "message": "Duplicate hesaplar silindi",
            "unique_count": len(unique_lines),
            "accounts": unique_lines
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
