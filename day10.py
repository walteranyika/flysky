from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    names="John Mark"
    age =88
    #jinja ==tempalating
    return render_template("index.html", names=names, age=age)

@app.route('/users')
def users():
    people =["John Mwangi","Mary Keitany","Robert Oliech","Wayne Rooney","Ting Lee"]
    return  render_template("users.html", people=people)

@app.route('/results')
def results():
    students = [{"names": "Denise Rollins", "MATH": 74, "ENGLISH": 97, "SWAHILI": 47},
                {"names": "Sydney Salas", "MATH": 56, "ENGLISH": 55, "SWAHILI": 90},
                {"names": "Curran Duffy", "MATH": 53, "ENGLISH": 95, "SWAHILI": 48},
                {"names": "Megan Ayala", "MATH": 81, "ENGLISH": 53, "SWAHILI": 73},
                {"names": "Anika Day", "MATH": 90, "ENGLISH": 42, "SWAHILI": 69},
                {"names": "Julian Buckley", "MATH": 61, "ENGLISH": 74, "SWAHILI": 89},
                {"names": "Jin Salas", "MATH": 50, "ENGLISH": 57, "SWAHILI": 53},
                {"names": "Sarah Coleman", "MATH": 98, "ENGLISH": 77, "SWAHILI": 72},
                {"names": "Lillith Turner", "MATH": 49, "ENGLISH": 74, "SWAHILI": 69},
                {"names": "Grant Gutierrez", "MATH": 40, "ENGLISH": 97, "SWAHILI": 91},
                {"names": "Xantha Best", "MATH": 47, "ENGLISH": 79, "SWAHILI": 92},
                {"names": "Bertha Graves", "MATH": 79, "ENGLISH": 49, "SWAHILI": 69},
                {"names": "Laith Sparks", "MATH": 94, "ENGLISH": 79, "SWAHILI": 99},
                {"names": "Alan Robbins", "MATH": 87, "ENGLISH": 87, "SWAHILI": 76},
                {"names": "Rooney Francis", "MATH": 86, "ENGLISH": 100, "SWAHILI": 86},
                {"names": "Vaughan Humphrey", "MATH": 64, "ENGLISH": 41, "SWAHILI": 93},
                {"names": "Rooney Downs", "MATH": 70, "ENGLISH": 97, "SWAHILI": 45},
                {"names": "Elvis Alexander", "MATH": 83, "ENGLISH": 99, "SWAHILI": 97},
                {"names": "Katelyn Hardy", "MATH": 82, "ENGLISH": 89, "SWAHILI": 67},
                {"names": "Marcia Yang", "MATH": 78, "ENGLISH": 100, "SWAHILI": 76},
                {"names": "Quincy Mcclure", "MATH": 50, "ENGLISH": 55, "SWAHILI": 69},
                {"names": "Clarke Campos", "MATH": 44, "ENGLISH": 45, "SWAHILI": 67},
                {"names": "Eleanor Hill", "MATH": 53, "ENGLISH": 83, "SWAHILI": 84},
                {"names": "Kirestin Hinton", "MATH": 60, "ENGLISH": 89, "SWAHILI": 40},
                {"names": "Stacy Case", "MATH": 61, "ENGLISH": 72, "SWAHILI": 94},
                {"names": "Sebastian Graves", "MATH": 95, "ENGLISH": 59, "SWAHILI": 68},
                {"names": "Beverly Roman", "MATH": 92, "ENGLISH": 73, "SWAHILI": 91},
                {"names": "Katelyn Roberson", "MATH": 64, "ENGLISH": 71, "SWAHILI": 63},
                {"names": "Amir Haney", "MATH": 63, "ENGLISH": 76, "SWAHILI": 75},
                {"names": "Remedios Alvarado", "MATH": 55, "ENGLISH": 92, "SWAHILI": 99},
                {"names": "Anika Bernard", "MATH": 50, "ENGLISH": 81, "SWAHILI": 90},
                {"names": "Patience Ortega", "MATH": 51, "ENGLISH": 56, "SWAHILI": 84},
                {"names": "Zephania Middleton", "MATH": 40, "ENGLISH": 86, "SWAHILI": 42},
                {"names": "Nolan Duran", "MATH": 44, "ENGLISH": 68, "SWAHILI": 79},
                {"names": "Orla Casey", "MATH": 66, "ENGLISH": 47, "SWAHILI": 97},
                {"names": "Thor Day", "MATH": 58, "ENGLISH": 47, "SWAHILI": 97},
                {"names": "Rogan Alvarez", "MATH": 82, "ENGLISH": 91, "SWAHILI": 74},
                {"names": "Olga Strickland", "MATH": 41, "ENGLISH": 68, "SWAHILI": 87},
                {"names": "Nyssa Beard", "MATH": 59, "ENGLISH": 49, "SWAHILI": 52},
                {"names": "Keane Stark", "MATH": 85, "ENGLISH": 50, "SWAHILI": 83},
                {"names": "Sylvester Whitaker", "MATH": 71, "ENGLISH": 89, "SWAHILI": 57},
                {"names": "Jakeem Beasley", "MATH": 100, "ENGLISH": 89, "SWAHILI": 80},
                {"names": "Vivian Talley", "MATH": 89, "ENGLISH": 53, "SWAHILI": 57},
                {"names": "Germane Short", "MATH": 83, "ENGLISH": 60, "SWAHILI": 98},
                {"names": "Ursula Wise", "MATH": 65, "ENGLISH": 63, "SWAHILI": 82},
                {"names": "Amal Mack", "MATH": 56, "ENGLISH": 77, "SWAHILI": 70},
                {"names": "Odysseus Key", "MATH": 62, "ENGLISH": 98, "SWAHILI": 53},
                {"names": "Chadwick Buckner", "MATH": 100, "ENGLISH": 51, "SWAHILI": 88},
                {"names": "Elvis Stuart", "MATH": 87, "ENGLISH": 42, "SWAHILI": 44},
                {"names": "Cameran Butler", "MATH": 54, "ENGLISH": 94, "SWAHILI": 93},
                {"names": "Buckminster Bowman", "MATH": 72, "ENGLISH": 73, "SWAHILI": 75},
                {"names": "Signe Stein", "MATH": 83, "ENGLISH": 77, "SWAHILI": 68},
                {"names": "Malcolm Conrad", "MATH": 93, "ENGLISH": 48, "SWAHILI": 75},
                {"names": "Tatyana Patrick", "MATH": 54, "ENGLISH": 60, "SWAHILI": 69},
                {"names": "Glenna Watkins", "MATH": 86, "ENGLISH": 78, "SWAHILI": 65},
                {"names": "Ina Acosta", "MATH": 53, "ENGLISH": 58, "SWAHILI": 84},
                {"names": "Emmanuel Huffman", "MATH": 60, "ENGLISH": 64, "SWAHILI": 92},
                {"names": "Uriah Odonnell", "MATH": 45, "ENGLISH": 83, "SWAHILI": 93},
                {"names": "Preston Terrell", "MATH": 47, "ENGLISH": 89, "SWAHILI": 74},
                {"names": "Erich Bender", "MATH": 81, "ENGLISH": 56, "SWAHILI": 47},
                {"names": "Erasmus Randall", "MATH": 47, "ENGLISH": 40, "SWAHILI": 77},
                {"names": "Ramona Patterson", "MATH": 88, "ENGLISH": 92, "SWAHILI": 91},
                {"names": "Signe Cooke", "MATH": 95, "ENGLISH": 74, "SWAHILI": 73},
                {"names": "Tobias Lowe", "MATH": 90, "ENGLISH": 54, "SWAHILI": 75},
                {"names": "Ulric Carter", "MATH": 80, "ENGLISH": 67, "SWAHILI": 49},
                {"names": "Elijah Bender", "MATH": 70, "ENGLISH": 45, "SWAHILI": 49},
                {"names": "Gavin Tyler", "MATH": 94, "ENGLISH": 58, "SWAHILI": 90},
                {"names": "Isadora Saunders", "MATH": 72, "ENGLISH": 62, "SWAHILI": 71},
                {"names": "Sacha Glover", "MATH": 93, "ENGLISH": 49, "SWAHILI": 75},
                {"names": "Holly Sharp", "MATH": 78, "ENGLISH": 98, "SWAHILI": 90},
                {"names": "Abraham Petersen", "MATH": 84, "ENGLISH": 52, "SWAHILI": 70},
                {"names": "Velma Rivers", "MATH": 94, "ENGLISH": 67, "SWAHILI": 64},
                {"names": "Risa Walton", "MATH": 75, "ENGLISH": 48, "SWAHILI": 44},
                {"names": "Tatum Shaffer", "MATH": 89, "ENGLISH": 46, "SWAHILI": 100},
                {"names": "Winter Tyson", "MATH": 54, "ENGLISH": 92, "SWAHILI": 69},
                {"names": "Arsenio Williams", "MATH": 92, "ENGLISH": 46, "SWAHILI": 72},
                {"names": "Ciaran Best", "MATH": 74, "ENGLISH": 67, "SWAHILI": 49},
                {"names": "Paula Cabrera", "MATH": 78, "ENGLISH": 48, "SWAHILI": 45},
                {"names": "Mary Juarez", "MATH": 60, "ENGLISH": 47, "SWAHILI": 96},
                {"names": "Kane Talley", "MATH": 63, "ENGLISH": 89, "SWAHILI": 93},
                {"names": "Nayda Harvey", "MATH": 99, "ENGLISH": 70, "SWAHILI": 74},
                {"names": "Barbara Rosa", "MATH": 55, "ENGLISH": 54, "SWAHILI": 53},
                {"names": "Noble Christian", "MATH": 71, "ENGLISH": 66, "SWAHILI": 57},
                {"names": "Aimee Parker", "MATH": 42, "ENGLISH": 54, "SWAHILI": 60},
                {"names": "Aimee Conway", "MATH": 98, "ENGLISH": 75, "SWAHILI": 85},
                {"names": "Molly Buckner", "MATH": 63, "ENGLISH": 83, "SWAHILI": 96},
                {"names": "Michael Butler", "MATH": 50, "ENGLISH": 68, "SWAHILI": 44},
                {"names": "Evangeline Adkins", "MATH": 60, "ENGLISH": 42, "SWAHILI": 98},
                {"names": "Fletcher Bradshaw", "MATH": 99, "ENGLISH": 45, "SWAHILI": 45},
                {"names": "Ignatius Cleveland", "MATH": 95, "ENGLISH": 83, "SWAHILI": 95},
                {"names": "Nicholas Fry", "MATH": 71, "ENGLISH": 91, "SWAHILI": 55},
                {"names": "Carlos Hewitt", "MATH": 88, "ENGLISH": 87, "SWAHILI": 71},
                {"names": "Kendall Trujillo", "MATH": 69, "ENGLISH": 87, "SWAHILI": 94},
                {"names": "Juliet Colon", "MATH": 88, "ENGLISH": 59, "SWAHILI": 65},
                {"names": "Sheila Cohen", "MATH": 56, "ENGLISH": 48, "SWAHILI": 82},
                {"names": "Connor Mccall", "MATH": 89, "ENGLISH": 95, "SWAHILI": 50},
                {"names": "Patricia Lott", "MATH": 67, "ENGLISH": 72, "SWAHILI": 85},
                {"names": "Cody Ferguson", "MATH": 98, "ENGLISH": 100, "SWAHILI": 64},
                {"names": "Kessie Lowe", "MATH": 49, "ENGLISH": 77, "SWAHILI": 59},
                {"names": "Sonia Merrill", "MATH": 69, "ENGLISH": 56, "SWAHILI": 83}]
    return  render_template("results.html", students=students)

if __name__ == '__main__':
    app.run()
